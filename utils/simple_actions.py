from selenium.webdriver.common.action_chains import ActionChains


class SimpleActions:

    def __init__(self, driver):
        self.driver = driver

    def check_element_exists(self, element):
        try:
            self.driver.find_element(*element)
        except:
            return False
        return True

    def get_element(self, element):
        return self.driver.find_element(*element)

    def get_elements(self, element):
        return self.driver.find_elements(*element)

    def element_click(self, element):
        self.driver.find_element(*element).click()

    def element_send_key(self, element, inputs):
        self.driver.find_element(*element).send_keys(inputs)

    def move_to_element(self, element):
        elements = self.driver.find_element(*element)
        actions = ActionChains(self.driver)
        actions.move_to_element(elements).perform()

    def switch_to_frame(self, element):
        frameElement = self.driver.find_element(*element)
        if frameElement is not None:
            self.driver.switch_to.frame(frameElement)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()
