import os
import pathlib
from datetime import datetime

import allure


class ScreenshotActions:

    def __init__(self, driver):
        self.driver = driver

    def add_screenshot(self, test_name, screenshot_name):
        current_directory = pathlib.Path(__file__).parent.parent.resolve()
        file_name = f'{current_directory}\\reports\\{test_name}{datetime.now().strftime("%d-%m-%Y_%H-%M-%S")}.png'
        self.driver.get_screenshot_as_file(file_name)
        allure.attach.file(file_name, name=screenshot_name,
                           attachment_type=allure.attachment_type.PNG)
        os.remove(file_name)
