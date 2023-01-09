from selenium.webdriver.common.by import By
from objects.components.utility_nav import UtilityNav
from objects.components.footer import Footer
from objects.components.header import Header
class ProfileSelection():

    def __init__(self, driver):
        self.driver = driver
        self.utility_nav = UtilityNav(self.driver)
        self.footer = Footer(self.driver)
        self.header = Header(self.driver)
        
    job_type_select = (By.ID, 'job-type-id')
    annual_income_select = (By.ID, 'annual-income-id')
    phone_number_input = (By.ID, 'phone-number-id')
    children_radio_buttons = (By.XPATH, '/html/body/main/dialog[1]/div/form/div[4]/div/div')
    homeowner_radio_buttons = (By.XPATH, '/html/body/main/dialog[1]/div/form/div[5]/div/div')
    submit_btn = (By.XPATH, '/html/body/main/dialog[1]/div/form/button[1]')
    thank_you_ok_btn = (By.XPATH, '//*[@id="thankYouModal"]/div/div/button')
    profiles_container = (By.XPATH, '/html/body/main/div[2]/div/div[2]') 
    profile_two = (By.XPATH, '/html/body/main/div[2]/div/div[2]/button[2]')
    choose_profile_btn = (By.XPATH, '//*[@id="312"]/div/div[1]/div[1]/div[2]/button[1]')