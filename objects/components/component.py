from selenium.webdriver.common.by import By


class Component:
    def __init__(self, driver):
        self.driver = driver

    component_element = (By.ID, "element_id")
