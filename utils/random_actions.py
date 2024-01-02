import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utils.simple_actions import SimpleActions
from selenium.webdriver.common.action_chains import ActionChains


class RandomActions:

    def __init__(self, driver):
        self.driver = driver

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

    def select_random_radio_button(self, element):
        """
        To choose a random radio button from a container element.
        """
        container = self.driver.find_element(*element)
        radio_buttons = container.find_elements(By.TAG_NAME, 'input')
        selected_option = random.choice(radio_buttons)
        selected_option.click()
        return selected_option.accessible_name

    def random_click(self, elements_identifier):
        """
        Random click an element from the elements_identifier (this identifier should return more than one element)
        """
        simple_actions = SimpleActions(self.driver) 
        elements = simple_actions.get_elements(elements_identifier)
        element = elements[random.randint(0,len(elements)-1)]
        element_name = element.get_attribute('text').replace("\n", "").replace(" ", "").strip()
        element.click()
        return element_name
        
    def random_hover(self, elements_identifier):
        """
        Random hover an element from the elements_identifier (this identifier should return more than one element)
        """
        simple_actions = SimpleActions(self.driver)
        actions = ActionChains(self.driver)
        elements = simple_actions.get_elements(elements_identifier)
        element = elements[random.randint(0,len(elements)-1)]
        actions.move_to_element(element).perform()
        return element
