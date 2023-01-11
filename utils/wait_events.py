from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WaitEvents:

    def __init__(self, driver):
        self.driver = driver
    
    def wait_element(self, element):
        return WebDriverWait(self.driver, 30).until(
        EC.visibility_of_element_located(element))
        
    def wait_element_clickable(self, element):
        return WebDriverWait(self.driver,30).until(
        EC.element_to_be_clickable(element))
    