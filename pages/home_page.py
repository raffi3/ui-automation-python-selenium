from selenium.webdriver.common.by import By
from base.base_page import BasePage
from components.navigation_component import NavigationComponent


class HomePage(BasePage):
    """
    Page Object for the Twitch Home Page.
    It assumes the driver is already on this page when initialized.
    """

    _BROWSE_ICON = (By.CSS_SELECTOR, "a[href='/directory']")

    def __init__(self, driver):
        """
        Calls the BasePage constructor and initializes components.
        The base_url is handled by the conftest driver fixture.
        """
        super().__init__(driver)

        # Initialize the reusable navigation bar component
        self.nav_bar = NavigationComponent(driver)

        # Wait for navigation / page load completion
        self._wait_for_page_load_complete()
        self._wait_element_visibility(self._BROWSE_ICON)
        self._wait_network_idle()
        print("Home Page loaded.")
