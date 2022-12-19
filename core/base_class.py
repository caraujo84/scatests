import pytest
import allure
import os
import requests
import random
from utilities.logger import Logger
from models.user import User
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from datetime import datetime

@pytest.mark.usefixtures("setup")
class BaseClass:
    
    def wait_element(self, element):
        return WebDriverWait(self.driver, 30).until(
        EC.visibility_of_element_located(element))
        
    def wait_element_clickable(self, element):
        return WebDriverWait(self.driver,30).until(
        EC.element_to_be_clickable(element))
    
    def add_screenshot(self, test_name, screenshot_name):
        file_name = f'reports/{test_name}{datetime.now().strftime("%d-%m-%Y_%H-%M-%S")}.png'
        self.driver.get_screenshot_as_file(file_name)
        allure.attach.file(file_name, name=screenshot_name, attachment_type=allure.attachment_type.PNG)
        os.remove(file_name)

    def get_logger(self):
        return Logger()
    
    def get_element(self, element):
        return self.driver.find_element(*element)
    
    def element_click(self, element):
        self.driver.find_element(*element).click()
    
    def element_send_key(self, element, inputs):
        self.driver.find_element(*element).send_keys(inputs)
    
    def select_option_by_visible_text(self, element, text):
        Select(self.driver.find_element(*element)).select_by_visible_text(text)
    
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
        
    def get_fake_user(self):
        response = requests.get("https://randomuser.me/api/")
        user_json = response.json()["results"][0]
        user = User(user_json)
        return user