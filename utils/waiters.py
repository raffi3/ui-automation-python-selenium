import time
import allure

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait


@allure.step("Waiting for document.readyState to be 'complete'")
def wait_for_page_load_complete(driver, timeout: int = 15):
    """Waits for the document.readyState to be 'complete'."""
    try:
        wait = WebDriverWait(driver, timeout)
        wait.until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
    except TimeoutException:
        print("Page did not reach document.readyState == 'complete'.")


@allure.step("Waiting for series of network requests completion")
def wait_for_matching_request_series(driver, substring: str, http_method: str = "GET",
                                     series_count: int = 5, timeout: int = 15):
    """
    Wait until a series of network requests matching the same condition occur within given timeout.

    Args:
        driver: seleniumwire.webdriver.Chrome
        substring (str): Part of URL to match
        http_method (str): e.g. GET / POST / PATCH / PUT etc.
        series_count (int): Number of requests to wait for
        timeout (int): Max seconds to wait

    Returns:
        list[Request]: List of matching requests
    """
    start = time.time()
    matching_requests = []

    while time.time() - start < timeout:
        # Filter all captured requests so far
        matching_requests = [
            req for req in driver.requests
            if req.method == http_method and substring in req.url
        ]

        if len(matching_requests) >= series_count:
            print(f"Found {len(matching_requests)} matching requests.")
            return matching_requests[:series_count]

        time.sleep(0.25)  # small polling interval

    raise TimeoutError(
        f"Timed out waiting for {series_count} GET requests containing '{substring}'. "
        f"Only found {len(matching_requests)}."
    )


@allure.step("Waiting for network to be idle")
def wait_network_to_be_idle(driver, timeout: int = 10, idle_time: int = 1.5):
    """Waits for the network to be 'idle' - no ongoing calls."""
    start_time = time.time()
    last_network_activity_time = time.time()
    active_requests = set()

    def on_request_will_be_sent(request):
        nonlocal last_network_activity_time
        active_requests.add(request.id)
        last_network_activity_time = time.time()

    def on_loading_finished(request, response):
        nonlocal last_network_activity_time
        active_requests.discard(request.id)
        last_network_activity_time = time.time()

    # Handle cases where the request fails (e.g., network error)
    def on_loading_failed(request, error):
        nonlocal last_network_activity_time
        active_requests.discard(request.id)
        last_network_activity_time = time.time()

    driver.request_interceptor = on_request_will_be_sent
    driver.response_interceptor = on_loading_finished
    driver.request_failed_interceptor = on_loading_failed  # Bonus: Also track failed requests

    while True:
        now = time.time()

        # Check if idle time has passed since the LAST network activity
        if not active_requests and (now - last_network_activity_time) > idle_time:
            print(f"Network has been idle for {idle_time} seconds.")
            break

        if now - start_time > timeout:
            raise TimeoutError(
                f"Network did not go idle in {timeout}s. {len(active_requests)} active requests remaining.")

        time.sleep(0.1)

    # Clear the interceptors after use
    del driver.request_interceptor
    del driver.response_interceptor
    del driver.request_failed_interceptor
