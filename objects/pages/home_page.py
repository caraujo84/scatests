from selenium.webdriver.common.by import By
from objects.components.utility_nav import UtilityNav
from objects.components.footer import Footer
from objects.components.header import Header

class HomePage():

    def __init__(self, driver):
        self.driver = driver
        self.utility_nav = UtilityNav(self.driver)
        self.footer = Footer(self.driver)
        self.header = Header(self.driver)
        
    first_image = (By.XPATH, '/html/body/main/div[1]/div/div/div[2]/div/picture/img')
    learn_more_btn = (By.XPATH, '/html/body/main/div[1]/div/div/div[1]/div/div/div[3]/a')
    conteiner_recomended_products = (By.XPATH, '/html/body/main/div[2]/div/div[2]/div')
    personal_btn = (By.XPATH, '//*[@id="tab-204"]')
    business_btn = (By.XPATH, '//*[@id="tab-205"]')
    container_blog_articles = (By.XPATH, '//*[@id="panel-204"]')
    second_image = (By.XPATH,'/html/body/main/div[4]/div/div[2]/div/picture/img')
    more_rates_btn = (By.XPATH, '/html/body/main/div[4]/div/div[2]/div/a')
    start_now_btn = (By.XPATH, '/html/body/main/div[5]/div/div[1]/div[3]/a')
    third_image = (By.XPATH, '/html/body/main/div[5]/div/div[2]/div[1]/picture/img')
    book_an_appointment = (By.XPATH, '/html/body/main/div[6]/div/div/div[2]/a')
    
    
    
    
    