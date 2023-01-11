import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class RandomActions:

    def select_random_option(self, element):
        """
        To select a random option from a select
        """
        select = self.driver.find_element(*element)
        options = [x.text for x in select.find_elements(By.TAG_NAME, 'option')][1:]
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
        return selected_option.text
    
    def click_random_element_with_class(self, element, element_class):
        """
        To choose a random button with a specific class from a container element
        """
        container = self.driver.find_element(*element)
        elements = container.find_elements(By.CLASS_NAME, element_class)
        selected_element = random.choice(elements)
        selected_element.click()
        return selected_element