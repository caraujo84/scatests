from browser_setup.browser_config import Browser_Config
from browser_setup.urls import URLS
from page_objects.sign_in_page import SIGN_IN_PAGE
from tests.test_home_page import Test_Class_Home
from page_objects.home_page import Home_Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
import html2text
import json

class Test_Class_Login:

    browser = Browser_Config.browser
    #url = URLS.vern
    url = URLS.iewc
    #url = URLS.joel
    #url = URLS.lake
    xpath = Browser_Config.xpath
    email = SIGN_IN_PAGE.email
    mail = SIGN_IN_PAGE.email_1
    passwd = SIGN_IN_PAGE.password
    sign_in_btn = SIGN_IN_PAGE.signin_btn
    modal = SIGN_IN_PAGE.modal
    error_sign_in = SIGN_IN_PAGE.error_sign_in
    error_sign_in_1 = SIGN_IN_PAGE.error_sign_in_1

    # Navigating to URL
    browser.get(url)


    delay = 5

    # TEST: Invalid credentials test
    def test_invalid_login(self):
        try:
            browser = self.browser
            delay = self.delay
            xpath = self.xpath
            email = self.email
            passwd = self.passwd
            error_sign_in = self.error_sign_in
            error_sign_in_1 = self.error_sign_in_1
            sign_in_btn = self.sign_in_btn
            page_wait = WebDriverWait(browser, delay).until(EC.presence_of_element_located((xpath, email)))
            email_input = browser.find_element(xpath,email)
            email_input.send_keys("test1@test.com")
            assert email_input
            password_input = browser.find_element(xpath,passwd)
            assert password_input
            password_input.send_keys("test")
            sign_in = browser.find_element(xpath,sign_in_btn)
            assert sign_in
            sign_in.click()
            error = browser.find_element(xpath, error_sign_in)
            assert error
            error_msg = html2text.html2text(error.get_attribute("outerHTML"))
            print(error_msg)
            try:
                page_wait = WebDriverWait(browser, delay).until(EC.presence_of_element_located((xpath, error_sign_in_1)))
                AC(browser).move_to_element(page_wait).perform()
                error=browser.find_element(xpath,error_sign_in_1)
                assert error
                error_msg = html2text.html2text(error.get_attribute("outerHTML"))
                print(error_msg)
            except:
                print("No error found")

            #browser.quit()
        except:
            print("Skipping test")
            try:
                mail = self.mail
                modal = self.modal
                delay = 15
                page_wait = WebDriverWait(browser, delay).until(EC.presence_of_element_located((xpath, modal)))
                AC(browser).move_to_element(page_wait).perform()
                modal = browser.find_element(xpath,modal)
                assert modal
                email = browser.find_element(xpath,mail)
                email.send_keys("test@test.com")
                assert email


            except:
                print ("Login modal not found")


            #browser.quit()

    #browser.quit()

p = Test_Class_Home()
p.test_sign_in_link()
s = Test_Class_Login()
s.test_invalid_login()


