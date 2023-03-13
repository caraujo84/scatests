from selenium.webdriver.common.by import By

class Header():

    def __init__(self, driver):
        self.driver = driver

    logo = (By.XPATH, '/html/body/header/div[2]/div/a[1]')
    menu_items = (By.CLASS_NAME, 'primary-navigation__link')
    contact_us_btn = (By.XPATH, '/html/body/header/div[1]/div/a[2]')
    