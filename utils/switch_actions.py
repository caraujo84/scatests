class SwitchActions:

    def __init__(self, driver):
        self.driver = driver

    def switch_to_frame(self, element):
        frameElement = self.driver.find_element(*element)
        if frameElement is not None:
            self.driver.switch_to.frame(frameElement)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def switch_to_window_by_url(self, url):
        windows = self.driver.window_handles
        for win in windows:
            self.driver.switch_to.window(win)
            if url in self.driver.current_url:
                break
