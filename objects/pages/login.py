from selenium.webdriver.common.by import By


class Login():

    def __init__(self, driver):
        self.driver = driver

    username = (By.NAME, "username")
    password = (By.NAME, "password")
    loginBtn = (By.XPATH, '/html/body/main/form/button')
    socialSignInBtn = (By.XPATH, '/html/body/main/form/a')
