from selenium.webdriver.common.by import By
from base.base_page import BasePage


class StreamerPage(BasePage):
    """
    Page Object for the Streamer's Page.
    """
    _STREAMER_HEADER = (By.CSS_SELECTOR, '[class*="stream-info-overlay"]')
    _VIDEO_PLAYER = (By.CSS_SELECTOR, '[data-a-target="player-overlay-click-handler"]')
    _MESSAGES_CONTAINER = (By.CSS_SELECTOR, '[data-test-selector*="message-container"]')
    _CHAT_INPUT = (By.CSS_SELECTOR, '[class*="overlayChatInputBox"]')

    def __init__(self, driver):
        super().__init__(driver)

        # Wait page content to load
        self._wait_element_visibility(self._STREAMER_HEADER)
        self._wait_element_visibility(self._VIDEO_PLAYER)
        self._wait_element_visibility(self._MESSAGES_CONTAINER)
        self._wait_element_visibility(self._CHAT_INPUT)
        self._wait_for_page_load_complete()
        print("Streamer Page loaded.")

    def take_streamer_screenshot(self, filename):
        """
        Takes a screenshot of the streamer page.
        """
        self.take_screenshot(filename)
