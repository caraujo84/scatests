from selenium.webdriver.common.by import By


class SiteProtection():

    def __init__(self, driver):
        self.driver = driver

    username = (By.NAME, "username")
    password = (By.NAME, "password")
    loginBtn = (By.XPATH, '/html/body/main/form/button')
