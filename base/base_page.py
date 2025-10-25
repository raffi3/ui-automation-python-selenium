from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import time
import os, random
from selenium.webdriver.common.keys import Keys

from utils.mobile_gestures import scroll_page_down
from utils.waiters import wait_for_page_load_complete, wait_network_to_be_idle


class BasePage:
    """
    The base class for all Page Objects.
    It contains common methods that all pages will use.
    """

    def __init__(self, driver, wait_time: int = 15):
        """
        Constructor for the BasePage.
        Increased wait time as pages like Twitch can be slow.
        """
        self.driver = driver
        self.wait = WebDriverWait(
            self.driver,
            wait_time,
            ignored_exceptions=[StaleElementReferenceException]
        )

    def _wait_element_visibility(self, locator: WebElement | tuple[str, str]):
        """Finds an element, waiting for it to be visible."""
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise TimeoutException(f"Element not found or not visible: {locator}")

    def _wait_elements_visibility(self, locator: WebElement | tuple[str, str]):
        """Finds multiple elements, waiting for them to be visible."""
        try:
            return self.wait.until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            raise TimeoutException(f"Elements not found or not visible: {locator}")

    def _click(self, locator: WebElement | tuple[str, str]):
        """Finds an element, waits for it to be clickable, and then clicks."""
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except Exception:
            # Force click with JS, when selenium click fails to add extra stability to tests
            element = self._wait_element_visibility(locator)
            self.driver.execute_script("arguments[0].click();", element)

    def _type(self, locator: WebElement | tuple[str, str], text: str):
        """Finds an element, clears it, and types text into it."""
        element = self._wait_element_visibility(locator)
        element.clear()
        element.send_keys(text)

    def _hit_key(self, locator: WebElement | tuple[str, str], key: str):
        """Finds an element, clears it, send keyboard key e.g. Keys.Enter."""
        element = self._wait_element_visibility(locator)
        element.send_keys(key)

    def _get_text(self, locator: WebElement | tuple[str, str]) -> str:
        """Finds an element and returns its text."""
        element = self._wait_element_visibility(locator)
        return element.text

    def _click_random_element_same_locator(self, locator: WebElement | tuple[str, str]):
        """
        Finds all elements matching a locator and clicks one at random.
        Useful for selecting from a list of similar items (e.g., search results).
        """
        print(f"Finding random element for locator: {locator}")
        try:
            elements = self._wait_elements_visibility(locator)
            if not elements:
                raise Exception(f"No visible elements found for locator {locator} to click randomly.")

            random_element = random.choice(elements)

            try:
                random_element.click()
            except Exception:
                # Force click with JS, when selenium click fails, to add extra stability to tests
                self.driver.execute_script("arguments[0].click();", random_element)
        except TimeoutException:
            raise TimeoutException(f"Could not find or click a random element for locator: {locator}")
        except Exception as e:
            raise f"Error clicking on element: {e}"

    def _wait_for_url_contains(self, url_fragment):
        """Waits for the URL to contain a specific fragment."""
        try:
            self.wait.until(EC.url_contains(url_fragment))
        except TimeoutException:
            raise TimeoutException(
                f"URL did not change to contain '{url_fragment}'. Current URL: '{self.driver.current_url}'")

    def _wait_for_page_load_complete(self, timeout=15):
        """Waits for the document.readyState to be 'complete'."""
        wait_for_page_load_complete(driver=self.driver, timeout=timeout)

    def _wait_network_idle(self, timeout=7, idle_time=1.5):
        """Waits for the network to be 'idle' - no ongoing calls."""
        wait_network_to_be_idle(driver=self.driver, timeout=timeout, idle_time=idle_time)

    def scroll_page_down(self, times: int = 1):
        """
        Scrolls the page down by the mobile window's inner height, 'times' number of times.
        """
        scroll_page_down(self.driver, times)

    def take_screenshot(self, filename):
        """
        Takes a screenshot and saves it to a 'screenshots' directory.
        """
        # Ensure the screenshots directory exists
        ss_dir = "screenshots"
        if not os.path.exists(ss_dir):
            os.makedirs(ss_dir)

        filepath = os.path.join(ss_dir, filename)
        try:
            self.driver.save_screenshot(filepath)
            print(f"Screenshot saved to {filepath}")
        except Exception as e:
            print(f"Error saving screenshot: {e}")
