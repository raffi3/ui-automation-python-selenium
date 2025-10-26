import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from components.navigation_component import NavigationComponent
from components.search_component import SearchBarComponent


class BrowsePage(BasePage):
    """
    Page Object for the Browse Page (/directory).
    """
    
    @allure.step("Initializing Browse Page")
    def __init__(self, driver):
        super().__init__(driver)
        self.nav_bar = NavigationComponent(driver)

        # Wait for navigation / page load completion
        self._wait_for_url_contains("/directory")
        self._wait_for_page_load_complete()
        print("Browse Page loaded.")

        self.search = SearchBarComponent(driver)
