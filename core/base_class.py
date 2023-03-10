import pytest
from utils.logger import Logger
from utils.wait_events import WaitEvents
from utils.screenshots_reports import ScreenshotsReports
from utils.simple_actions import SimpleActions
from utils.select_actions import SelectActions
from utils.random_actions import RandomActions
from utils.fake_user import FakeUser
from utils.custom import Custom
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class BaseClass:

    def get_logger(self):
        return Logger()
    
    def get_fake_user_utils(self):
        return FakeUser()
    
    def get_wait_utils(self):
        return WaitEvents(self.driver)
    
    def get_screenshot_utils(self):
        return ScreenshotsReports(self.driver)
    
    def get_simple_actions(self):
        return SimpleActions(self.driver)
    
    def get_select_actions(self):
        return SelectActions(self.driver)
    
    def get_random_actions(self):
        return RandomActions(self.driver)
    
    def get_custom_utils(self):
        return Custom(self.driver)
    
    def check_images_attributes(self, element, attribute, text):
        """
        To check the accesibility in the images 
        """
        container = self.driver.find_element(*element)
        images = container.find_elements(By.TAG_NAME , 'img')
        list = []
        for img in images:
            img_attribute = img.get_attribute(attribute)
            if img_attribute != text:
                list = [images]
        return list
    