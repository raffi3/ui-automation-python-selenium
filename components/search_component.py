import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base.base_page import BasePage


class SearchBarComponent(BasePage):
    """
    Component for the search bar (input and submit logic).
    This component is present on Navigation Component.
    """
    _SEARCH_INPUT = (By.CSS_SELECTOR, 'input[type="search"]')

    def __init__(self, driver):
        """Initializes the component."""
        super().__init__(driver)

    # Private Methods
    @allure.step("Clicking into search bar")
    def _click_into_search_bar(self):
        """
        Activates the search input field.
        This is good practice for reliability.
        """
        self._click(self._SEARCH_INPUT)

    @allure.step("Entering search query: {keyword}")
    def _enter_search_query(self, keyword: str):
        """
        Types the search query into the field.
        Note: This method does NOT submit the search.
        """
        # The _type method in BasePage handles clear() and send_keys()
        self._type(self._SEARCH_INPUT, keyword)

    @allure.step("Submitting search (hitting ENTER)")
    def _submit_search(self):
        """
        Submits the search query by pressing ENTER.
        This works for both mobile and desktop.
        """
        print("Submitting search...")
        self._hit_key(self._SEARCH_INPUT, Keys.ENTER)

    # Public Method
    @allure.step("Performing search for: {keyword}")
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
