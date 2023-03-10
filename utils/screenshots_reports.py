import allure
import os
from datetime import datetime

class ScreenshotsReports:

    def __init__(self, driver):
        self.driver = driver
    
    def add_screenshot(self, test_name, screenshot_name):
        file_name = f'reports/{test_name}{datetime.now().strftime("%d-%m-%Y_%H-%M-%S")}.png'
        self.driver.get_screenshot_as_file(file_name)
        allure.attach.file(file_name, name=screenshot_name, attachment_type=allure.attachment_type.PNG)
        os.remove(file_name)