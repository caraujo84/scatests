import time

from browser_setup.browser_config import Browser_Config
from browser_setup.urls import URLS
from page_objects.sign_in_page import SIGN_IN_PAGE
from tests.test_home_page import Test_Class_Home
from page_objects.home_page import Home_Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
import html2text

class Test_Account_Create:
    browser = Browser_Config.browser
    xpath = Browser_Config.xpath
    create_account_link = SIGN_IN_PAGE.create_account_link
    tag = Browser_Config.tag
    id = Browser_Config.id
    cookiebot = SIGN_IN_PAGE.cookiebot
    user_inf = SIGN_IN_PAGE.user_inf
    delay = 5

    def browser_nav(self):
        browser = self.browser
        #url = URLS.vern
        url = URLS.iewc
        #url = URLS.joel
        #url = URLS.lake
        browser.get(url)


    def test_account_creation(self):
        xpath = self.xpath
        tag = self.tag
        id = self.id
        browser = self.browser
        delay = self.delay
        create_account_link = self.create_account_link
        cookiebot = self.cookiebot

        # Close Cookiebot if any found
        try:
            page_wait = WebDriverWait(browser, delay).until(EC.element_to_be_clickable((xpath, cookiebot)))
            AC(browser).move_to_element(page_wait).perform()
            cookie_btn = browser.find_element(xpath,cookiebot)
            cookie_btn.click()
            print("Cookiebot closed")
        except:
            print("No cookiebot found")


        try:
            page_wait = WebDriverWait(browser, delay).until(EC.visibility_of_element_located((xpath, create_account_link)))
            #AC(browser).move_to_element(page_wait).perform()
            crt_acct_link = browser.find_element(xpath,create_account_link)
            assert crt_acct_link
            crt_acct_link.click()
            print("Create Account link clicked")
        except:
            print("Create Account link not found")


        # Extracting & Listing all the fields displayed in the Form (This could also be used to know which fields have validation)
        user_inf = self.user_inf

        page_wait = WebDriverWait(browser, delay).until(EC.presence_of_element_located((xpath, user_inf)))
        assert page_wait
        form_fields = browser.find_elements(tag,"input")
        assert form_fields
        list_fields = list()
        for x in form_fields:

            if x.get_attribute('data-val'):
                list_fields.append(x.get_attribute('id'))

        print(list_fields)

        #email_field = browser.find_element(id, "emailAddress1980")
        #email_field.send_keys("test@test.com")




t = Test_Account_Create()
t.browser_nav()
s = Test_Class_Home()
s.test_sign_in_link()
t.test_account_creation()