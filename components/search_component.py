from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base.base_page import BasePage


class SearchBarComponent(BasePage):
    """
    Component for the search bar (input and submit logic).
    This component appears after clicking the search icon
    in the NavigationComponent.
    """
    _SEARCH_INPUT = (By.CSS_SELECTOR, 'input[type="search"]')

    def __init__(self, driver):
        """Initializes the component."""
        super().__init__(driver)

    def wait_for_input_ready(self):
        """Waits for the search input field to be visible."""
        print("Waiting for search input to be ready...")
        self._wait_element_visibility(self._SEARCH_INPUT)
        print("Search input is ready.")

    # Private Methods
    def _click_into_search_bar(self):
        """
        Activates the search input field.
        This is good practice for reliability.
        """
        self._click(self._SEARCH_INPUT)

    def _enter_search_query(self, keyword: str):
        """
        Types the search query into the field.
        Note: This method does NOT submit the search.
        """
        # The _type method in BasePage handles clear() and send_keys()
        self._type(self._SEARCH_INPUT, keyword)

    def _submit_search(self):
        """
        Submits the search query by pressing ENTER.
        This works for both mobile and desktop.
        """
        print("Submitting search...")
        self._hit_key(self._SEARCH_INPUT, Keys.ENTER)

    # Public Method
    def search(self, keyword: str):
        """
        Performs a full search action:
        1. Clicks the search bar
        2. Types the keyword
        3. Submits the search
        4. Returns SearchResultsPage instance
        """
        print(f"Performing search for: {keyword}")
        self._click_into_search_bar()
        self._enter_search_query(keyword)
        self._submit_search()

        from pages.search_results_page import SearchResultsPage
        return SearchResultsPage(self.driver)

