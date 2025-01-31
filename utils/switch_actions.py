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

    def switch_to_new_tab(self):
        self.driver.switch_to.new_window("tab")

    def close_current_tab(self):
        self.driver.close()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[len(windows) - 1])
