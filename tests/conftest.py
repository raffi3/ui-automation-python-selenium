import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from config import IS_MOBILE, BASE_URL_MOBILE, BASE_URL_WEB


@pytest.fixture(scope="session")
def is_mobile():
    """
    Fixture to pass the IS_MOBILE config setting into tests.
    Returns:
        bool: The value of IS_MOBILE from config.py
    """
    return IS_MOBILE


@pytest.fixture(scope="function")
def driver(request, is_mobile):  # Pass the is_mobile fixture in
    """
    This fixture creates a new Chrome driver instance for each test.
    It configures the driver for mobile emulation or desktop mode
    based on the IS_MOBILE flag.
    """

    options = ChromeOptions()

    if is_mobile:
        print("\nRunning in Mobile mode.")
        # Configure Chrome for mobile emulation based on iPhone SE
        mobile_emulation = {
            "deviceName": "iPhone SE"
        }
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        base_url = BASE_URL_MOBILE

    else:
        print("\nRunning in Desktop mode.")
        options.add_argument("--start-maximized")
        # options.add_argument("--window-size=1920,1080")
        base_url = BASE_URL_WEB

    driver_instance = webdriver.Chrome(options=options)

    # Enable network tracking
    driver_instance.execute_cdp_cmd("Network.enable", {})

    # Navigate to Base URL
    # The driver will navigate to the correct URL before being passed to the test.
    print(f"Navigating to base URL: {base_url}")
    driver_instance.get(base_url)

    yield driver_instance

    # Teardown
    print("\nClosing browser...")
    driver_instance.quit()
