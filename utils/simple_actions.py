

class SimpleActions:
    def get_element(self, element):
        return self.driver.find_element(*element)
    
    def element_click(self, element):
        self.driver.find_element(*element).click()
    
    def element_send_key(self, element, inputs):
        self.driver.find_element(*element).send_keys(inputs)
    
    