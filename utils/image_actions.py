from selenium.webdriver.common.by import By


class ImageActions:
    def __init__(self, driver):
        self.driver = driver

    def check_images_attributes(self, element, attribute, text):
        """
        To check the accesibility in the images
        """
        container = self.driver.find_element(*element)
        images = container.find_elements(By.TAG_NAME, "img")
        list = []
        for img in images:
            img_attribute = img.get_attribute(attribute)
            if img_attribute != text:
                list = [images]
        return list
