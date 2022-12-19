from selenium.webdriver.common.by import By

class UtilityNav():

    def __init__(self, driver):
        self.driver = driver
        
    log_In = (By.XPATH, '/html/body/header/nav/div/ul/li[1]/a') 
    refer_a_friend = (By.XPATH, '/html/body/header/nav/div/ul/li[2]/a')