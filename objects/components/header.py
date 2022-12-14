from selenium.webdriver.common.by import By

class Header():

    def __init__(self, driver):
        self.driver = driver

    logo = (By.XPATH, '/html/body/div[3]/div/header/div[2]/a')
    contact_us_btn = (By.XPATH, '/html/body/div[3]/div/header/div[2]/div/a')
    menu_btn = (By.XPATH, '/html/body/div[3]/div/header/div[2]/div/div/button')
    menu_item_work = (By.XPATH, '/html/body/div[4]/div/div[1]/nav/ul/li[1]/a')
    menu_work_title = (By.XPATH, '//*[@id="work"]/div[1]/h2')
    menu_item_expertise = (By.XPATH, '/html/body/div[4]/div/div[1]/nav/ul/li[2]/a')
    menu_expertise_title = (By.XPATH, '//*[@id="expertise"]/div[1]/h2')
