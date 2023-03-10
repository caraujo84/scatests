from selenium.webdriver.common.by import By

class Header():

    def __init__(self, driver):
        self.driver = driver

    logo = (By.XPATH, '/html/body/header/div[2]/div/a[1]')
    menu_personal_item = (By.XPATH, '/html/body/header/div[1]/div/nav/ul/li[1]/a')
    menu_business_item = (By.XPATH, '/html/body/header/div[1]/div/nav/ul/li[2]/a')
    menu_articles_item = (By.XPATH, '/html/body/header/div[1]/div/nav/ul/li[3]/a')
    menu_locations_item = (By.XPATH, '/html/body/header/div[1]/div/nav/ul/li[4]/a')
    contact_us_btn = (By.XPATH, '/html/body/header/div[1]/div/a[2]')
    