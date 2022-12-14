import pytest
import allure
import os
import requests
from utilities.logger import Logger
from models.user import User
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
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
    
    def get_element_click(self, element):
        return self.driver.find_element(*element).click()
    
    def get_element_send_key(self, element, inputs):
        return self.driver.find_element(*element).send_keys(inputs)
    
    def get_select_element_by_visible_text(self, element, text):
        return Select(self.driver.find_element(*element)).select_by_visible_text(text)
    
    def get_select_element_by_value(self, element, value):
        return Select(self.driver.find_element(*element)).select_by_value(value)
    
    def get_fake_user(self):
        response = requests.get("https://randomuser.me/api/")
        user_json = response.json()["results"][0]
        user = User(user_json)
        return user