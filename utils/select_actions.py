import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class SelectActions:

    def __init__(self, driver):
        self.driver = driver

    def select_option_by_visible_text(self, element, text):
        Select(self.driver.find_element(*element)).select_by_visible_text(text)

    def select_random_option(self, element):
        """
        To select a random option from a select
        """
        select = self.driver.find_element(*element)
        options = [x.text for x in select.find_elements(
            By.TAG_NAME, 'option')][1:]
        selected_option = random.choice(options)
        Select(select).select_by_visible_text(selected_option)
        return selected_option
