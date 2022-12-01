from browser_setup.browser_config import Browser_Config
from browser_setup.urls import URLS
from page_objects.home_page import Home_Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
import requests
import html2text

class Test_Class_Home:

    #url = URLS.vern
    url = URLS.iewc
    #url = URLS.joel
    #url = URLS.lake
    browser = Browser_Config.browser
    browser.get(url)
    logo1 = Home_Page.logo_a
    logo2 = Home_Page.logo_b


    def __init__(self):
        return

    # TEST: Checking site response status (Ability to load site)

    def test_page_load(self):
        #browser = Browser_Config.browser
        #self.url = URLS.lake
        url = self.url
        #browser = self.browser
        #browser.get(self.url)
        request = requests.get(url)
        request1 = str(request)
        request = request1.replace("<", "").replace(">", "")

        ok_status = "Response [200]"
        assert request == ok_status
        if request == ok_status:
            print ("Page returned status:", request+". Page loaded successfully")
        else:
            request = requests.get(url)
            request1 = str(request)
            request = request1.replace("<", "").replace(">", "")
            print ("Error loading site, Request returned: ", request)

    # Navigate to URL
    #browser.get(url)

    # TEST: Verify page performance (basic test)
    def test_performance(self):
        #browser = self.browser
        try:

            navigationStart = self.browser.execute_script("return window.performance.timing.navigationStart")
            responseStart = self.browser.execute_script("return window.performance.timing.responseStart")
            domComplete = self.browser.execute_script("return window.performance.timing.domComplete")

            backendPerformance_calc = responseStart - navigationStart
            frontendPerformance_calc = domComplete - responseStart
            assert backendPerformance_calc
            assert frontendPerformance_calc
            backendPerformance_calc = backendPerformance_calc/1000 # To convert from milliseconds to seconds
            frontendPerformance_calc = frontendPerformance_calc/1000 # To convert from milliseconds to seconds
            print("Back End: %s" % backendPerformance_calc, "seconds"," / ","Front End: %s" % frontendPerformance_calc,"seconds")

        except:
            print ("Performance not measured")


    # TEST: Verifies Sign In link is present & clickable
    def test_sign_in_link(self):
        try:
            browser = self.browser
            delay = self.delay
            xpath = self.xpath
            url = self.url
            sign_in1 = Home_Page.sign_in
            sign_in2 = Home_Page.login
            sign_in3 = Home_Page.signin
            page_wait = WebDriverWait(browser, delay).until(EC.presence_of_element_located((xpath, sign_in1)))
            sign_in = browser.find_element(xpath,sign_in1)
            assert sign_in

            print ("Sign In link found")
            try:
                sign_in.click()
                current_url = browser.current_url
                #print (current_url)
                if current_url == url:
                    print ("Error: Sign In Link is not clickable")
                elif current_url[31:40] == "air-login":
                    sign_in = browser.find_element(xpath,sign_in3)
                    sign_in.click()
                    print ("Sign In link clicked")
                else:
                    print("Success: Sign In Link is clickable")


            except:
                print ("Link is not clickable")

        except:
            #print ("Sign In link A not found")
            try:
                page_wait = WebDriverWait(browser, delay).until(EC.presence_of_element_located((xpath, sign_in2)))
                sign_in = browser.find_element(xpath, sign_in2)
                assert sign_in
                sign_in.click()
                print ("Sign In Link found")
                try:
                    sign_in.click()
                    current_url = browser.current_url
                    #print(current_url)
                    if current_url == url:
                        print("Error: Sign In Link is not clickable")
                    elif current_url !=url:
                        print("Able to click on Sign In Link")
                    else:
                        print("Success: Sign In Link clickable")

                except:
                    print("Link is not clickable")

            except:
                print("Page has no Sign In feature")

    # TEST: Verify logo is displayed
    def test_logo(self):
        try:
            xpath = self.xpath
            browser = self.browser
            logo1 = self.logo1
            url = self.url
            delay = self.delay
            logo2 = self.logo2
            page_wait = WebDriverWait(browser,delay).until(EC.presence_of_element_located((xpath, logo1)))
            logo = browser.find_element(xpath, logo1)
            assert logo
            print ("Logo found successfully")
            try:
                logo.click()
                current_url = browser.current_url
                #print(current_url)
                if current_url == url:
                    print("Logo takes user to Home Page as expected")
                else:
                    print("Logo test failed")
            except:
                print("Logo not clickable")


        except:
            #print ("Logo A not found")
            try:
                page_wait = WebDriverWait(browser, delay).until(EC.presence_of_element_located((xpath, logo2)))
                logo = browser.find_element(xpath, logo2)
                assert logo
                print("Logo found successfully")
                try:
                    logo.click()
                    current_url = browser.current_url
                    #print(current_url)
                    if current_url == url:
                        print("Logo takes user to Home Page as expected")
                    else:
                        print("Logo test failed")
                except:
                    print("Logo not clickable")
            except:
                print ("Page does not contain a Logo")

    # TEST: Verify Copyright symbol is found in site
    def test_copyright_symbol(self):
        try:
            browser = self.browser
            xpath = self.xpath
            copy = Home_Page.copy
            copyr = browser.find_element(xpath,copy)
            copyright_text = html2text.html2text(copyr.get_attribute("outerHTML")) ## html2text library allows to strip HTML to get only text
            assert copyr
            assert copyright_text
            print("Copyright found")
            print(copyright_text)
        except:
            print("Copyright not found")

    def test_footer(self):
        browser = self.browser
        terms = Home_Page.terms
        faq = Home_Page.FAQ
        privacy = Home_Page.privacy
        contact_us = Home_Page.contact
        delay = 10
        xpath = Browser_Config.xpath

        try:
            page_wait = WebDriverWait(browser, delay).until(EC.visibility_of_element_located((xpath, faq)))
            AC(browser).move_to_element(page_wait).perform()
            faq_link = browser.find_element(xpath, faq)
            assert faq_link
            print("FAQ link found")
        except:
            print ("FAQ link not found")

        try:
            page_wait = WebDriverWait(browser, delay).until(EC.visibility_of_element_located((xpath, terms)))
            AC(browser).move_to_element(page_wait).perform()
            terms_conditions = browser.find_element(xpath, terms)
            assert terms_conditions
            print ("Terms & Condition link found")
        except:
            print("Terms And Conditions link not found")


        try:
            page_wait = WebDriverWait(browser, delay).until(EC.visibility_of_element_located((xpath, privacy)))
            AC(browser).move_to_element(page_wait).perform()
            privacy_link = browser.find_element(xpath, privacy)
            assert privacy_link
            print("Privacy Policy link found")

        except:
            print("Privacy Policy link not found")

        try:
            page_wait = WebDriverWait(browser, delay).until(EC.visibility_of_element_located((xpath, contact_us)))
            AC(browser).move_to_element(page_wait).perform()
            contact_us_link = browser.find_element(xpath, contact_us)
            assert contact_us_link
            print("Contact Us link found")

        except:
            print("Contact Us link not found")


    #### Functions ####
    ###################
home = Test_Class_Home()
home.test_page_load()
home.test_performance()
#home.test_sign_in_link()
#home.test_logo()
#home.test_copyright_symbol()

home.test_footer()
    ####################

#browser.quit()