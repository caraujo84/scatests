

class SimpleActions:

    def __init__(self, driver):
        self.driver = driver

    def check_element_exists(self, element):
        try:
            self.driver.find_element(*element)
        except:
            return False
        return True
        
    def get_element(self, element):
        return self.driver.find_element(*element)
    
    def get_elements(self, element):
        return self.driver.find_elements(*element)
    
    def element_click(self, element):
        self.driver.find_element(*element).click()
    
    def element_send_key(self, element, inputs):
        self.driver.find_element(*element).send_keys(inputs)
    
    