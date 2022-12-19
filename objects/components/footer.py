from selenium.webdriver.common.by import By

class Footer():

    def __init__(self, driver):
        self.driver = driver
        
    input_name = (By.ID, 'b18b89f6-1d05-4568-9116-52973b7fd6db')
    input_last_name = (By.ID, '52ffae1f-a196-4c11-917a-aa4480abdd2a')
    input_email = (By.ID, '49edf1ab-c417-48a6-bcc4-cd604fdab747')
    submit_btn = (By.ID, '61917495-467b-4840-b92c-ef39ddeffa8b')
    correct_message = (By.XPATH, '//*[@id="b8db7f13-c83e-4505-ba5d-5c0d31e81233"]/div[1]/div')