import allure
from utils.data_provider import get_timestamp_ms_in_past


@allure.step("Setting localStorage key '{key}'")
def set_local_storage(driver, key, value):
    driver.execute_script("localStorage.setItem(arguments[0], arguments[1]);", key, value)


@allure.step("Setting content view consent in localStorage")
def set_content_view_consent_in_local_storage(driver):
    key = "content-classification-labels-acknowledged"
    value = '{"loggedIn":{},"loggedOut":{"DrugsIntoxication":%d}}' % get_timestamp_ms_in_past()

    set_local_storage(driver=driver, key=key, value=value)
