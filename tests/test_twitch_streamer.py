import pytest
import allure
from pages.home_page import HomePage


@allure.story("Twitch tests")
@pytest.mark.usefixtures("driver")
class TestTwitch:

    @allure.title("Test: Search for a streamer, open their page, and take a screenshot")
    @allure.description(
        "1. Navigates to Twitch home page (handled by fixture)\n"
        "2. Go to browse page (if in mobile view)\n"
        "3. Search by keyword\n"
        "4. View all channels\n"
        "5. Scrolls down 2 times\n"
        "6. Selects a streamer (handle pop-up for content view)\n"
        "7. Wait streamer's page to be loaded & Takes a screenshot"
    )
    def test_search_and_select_streamer(self, driver, is_mobile):
        """
        Note: To ensure test stability all pages are waiting navigation and page content load completion,
        methods are using explict waits and hard sleeps are avoided
        """
        home_page = HomePage(driver)

        search_keyword = "StarCraft II"  # could be parametrized
        if is_mobile:
            # On mobile, Search bar is available in Brows Page Nav bar
            # 2. Go to brows page (if in mobile view)
            browse_page = home_page.nav_bar.go_to_browse_page()

            # 3. Search by keyword (using Brows Page Nav bar)
            search_results_page = (browse_page
                                   .nav_bar
                                   .search_bar
                                   .search(search_keyword))
        else:
            # On desktop, Search bar is available in Home Page Nav bar
            # 3. Search by keyword (using Home Page Nav bar)
            search_results_page = (home_page
                                   .nav_bar
                                   .search_bar
                                   .search(search_keyword))

        # 4. View all channels
        search_results_page.open_all_channels_wait_to_load()

        # 5. Scrolls down 2 times
        search_results_page.scroll_page_down(times=2)

        # 6. Select a streamer & Handle pop-up for content view
        streamer_page = search_results_page.open_streamer_page()

        # 7. On the streamer page wait until all is loaded and take a screenshot
        streamer_page.take_screenshot("streamer_page_view.png")
