import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait


def wait_network_to_be_idle(driver, timeout=7, idle_time=1.5):
    """Waits for the network to be 'idle' - no ongoing calls."""
    start = time.time()
    active_requests = set()

    def on_request_will_be_sent(params):
        active_requests.add(params.get("requestId"))

    def on_loading_finished(params):
        active_requests.discard(params.get("requestId"))

    driver.request_interceptor = on_request_will_be_sent
    driver.response_interceptor = on_loading_finished

    while True:
        if not active_requests and (time.time() - start) > idle_time:
            break
        if time.time() - start > timeout:
            raise TimeoutError(f"Network did not go idle in time. Timeout {timeout} reached.")
        time.sleep(0.2)
    print(f"Network has been idle for {idle_time} seconds.")


def wait_for_page_load_complete(driver, timeout=15):
    """Waits for the document.readyState to be 'complete'."""
    try:
        wait = WebDriverWait(driver, timeout)
        wait.until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
    except TimeoutException:
        print("Page did not reach document.readyState == 'complete'.")
