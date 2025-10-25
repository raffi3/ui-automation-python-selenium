from selenium.webdriver.common.by import By
from base.base_page import BasePage
from components.search_component import SearchBarComponent
from utils.waiters import wait_network_to_be_idle
from utils.browser_storage import set_content_view_consent_in_local_storage


class SearchResultsPage(BasePage):
    """
    Page Object for the Search Results Page.
    This page contains the search bar component and the list of results.
    """
    _SECTION_TITLE = (By.CSS_SELECTOR, 'h2[class*="CoreText"][class*="ScTitleText"]')
    _VIEW_ALL_CHANNELS = (By.CSS_SELECTOR,
                          ':is([class*="ScCoreLink"][href*="type=channels"], [data-test-selector*="show-more-channels"] p)')
    _STREAMER = (By.CSS_SELECTOR, '[class*="ScCoreLink"] p')  # Todo make one for desktop as well

    def __init__(self, driver):
        super().__init__(driver)

        # Initialize the reusable search bar component
        self.search = SearchBarComponent(driver)

        # Wait for navigation / page load completion
        self._wait_for_url_contains("/search")
        self._wait_for_page_load_complete()
        print("Search Results Page loaded.")

    def open_all_channels_wait_to_load(self):
        self._click(self._VIEW_ALL_CHANNELS)
        self._wait_for_page_load_complete()

    def open_streamer_page(self):
        set_content_view_consent_in_local_storage(self.driver)  # sets value in local storage to handle pop-up
        self._click_random_element_same_locator(self._STREAMER)
        from pages.streamer_page import StreamerPage

        return StreamerPage(self.driver)
