import pytest
from utils.logger import Logger
from utils.wait_events import WaitEvents
from utils.screenshots_reports import ScreenshotsReports
from utils.simple_actions import SimpleActions
from utils.select_actions import SelectActions
from utils.random_actions import RandomActions
from utils.fake_user import FakeUser
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class BaseClass:
    
    def get_wait_utils(self):
        return WaitEvents()
    
    def get_screenshot(self):
        return ScreenshotsReports()

    def get_logger(self):
        return Logger()
    
    def get_simple_actions(self):
        return SimpleActions()
    
    def get_select_actions(self):
        return SelectActions()
    
    def get_random_action(self):
        return RandomActions()
    
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
                
        
    def get_fake_user(self):
        return FakeUser
    