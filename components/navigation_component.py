from selenium.webdriver.common.by import By
from base.base_page import BasePage
from components.search_component import SearchBarComponent


class NavigationComponent(BasePage):
    """
    Models the top navigation bar.
    This component is present on most pages.
    """
    _BROWSE_ICON_LINK = (By.CSS_SELECTOR, "a[href='/directory']")

    def __init__(self, driver):
        super().__init__(driver)
        self.search_bar = SearchBarComponent(driver)


    def go_to_browse_page(self):
        """Clicks the Browse icon and returns the BrowsePage object."""
        self._click(self._BROWSE_ICON_LINK)
        from pages.browse_page import BrowsePage

        return BrowsePage(self.driver)