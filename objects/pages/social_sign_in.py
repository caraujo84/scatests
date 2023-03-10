from selenium.webdriver.common.by import By

class SocialSignIn():

    def __init__(self, driver):
        self.driver = driver
        
    email_input = (By.ID, 'email')
    password_input = (By.ID, 'password')
    login_btn = (By.ID, 'u_0_5_z9')
    continue_btn = (By.ID, 'btnSignUp')
    