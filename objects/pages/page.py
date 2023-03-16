from selenium.webdriver.common.by import By
from objects.components.component import Component


class Page():

    def __init__(self, driver):
        self.driver = driver
        self.component = Component(self.driver)

    page_element = (By.ID, "element_id")
