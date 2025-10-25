from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH


def scroll_page_down(driver, times: int = 1):
    """
    Scrolls the page down by the mobile window's inner height, 'times' number of times.
    """
    # Get window size
    size = driver.execute_script("return { 'width': window.innerWidth, 'height': window.innerHeight };")
    width = size['width']
    height = size['height']

    # Set swipe start and end points
    start_x = width // 2
    start_y = int(height * 0.7)  # 70% from the top
    end_y = int(height * 0.3)  # 30% from the top

    for _ in range(times):
        # 1. Create ActionChains and get the ActionBuilder
        actions = ActionChains(driver)
        action_builder = actions.w3c_actions

        # 2. Add a new touch pointer device (our "finger")
        finger = action_builder.add_pointer_input(POINTER_TOUCH, "finger")

        # 3. Start the sequence of actions for the finger
        finger.create_pointer_move(x=start_x, y=start_y, duration=0)
        finger.create_pointer_down(button=0)
        finger.create_pointer_move(x=start_x, y=end_y, duration=250)
        finger.create_pointer_up(button=0)

        actions.perform()
