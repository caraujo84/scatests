import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from threading import Thread
from browser_setup.urls import URLS
from browser_setup.browser_config import Browser_Config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
from page_objects.home_page import Home_Page
from page_objects.sign_in_page import SIGN_IN_PAGE
from selenium.common.exceptions import NoSuchElementException
import html2text
import requests
import json

BROWSERSTACK_USERNAME = os.environ.get("BROWSERSTACK_USERNAME") or "sigfridopujols3"
BROWSERSTACK_ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY") or "FynT9C7yi2jcpxs2hgJc"
URL = os.environ.get("URL") or "https://hub.browserstack.com/wd/hub"
BUILD_NAME = "Pilot_test"
capabilities = [
    {
        "browserName": "Chrome",
        "browserVersion": "latest",
        "os": "Windows",
        "osVersion": "11",
        "sessionName": "BStack Python parallel - Chrome", # test name
        "buildName": BUILD_NAME,  # Your tests will be organized within this build
    },
    {
        "browserName": "Edge",
        "browserVersion": "latest",
        "os": "Windows",
        "osVersion": "10",
        "sessionName": "BStack Python parallel - Microsoft Edge",
        "buildName": BUILD_NAME,
    },
    {
        "browserName": "Safari",
        "browserVersion": "latest",
        "os": "OS X",
        "osVersion": "Ventura",
        "sessionName": "BStack Python parallel - Safari",
        "buildName": BUILD_NAME,
    },
]
def get_browser_option(browser):
    switcher = {
        "chrome": ChromeOptions(),
        "firefox": FirefoxOptions(),
        "edge": EdgeOptions(),
        "safari": SafariOptions(),
    }
    return switcher.get(browser, ChromeOptions())

def test_home_page(cap):
    bstack_options = {
        "osVersion": cap["osVersion"],
        "buildName": cap["buildName"],
        "sessionName": cap["sessionName"],
        "userName": BROWSERSTACK_USERNAME,
        "accessKey": BROWSERSTACK_ACCESS_KEY
    }
    if "os" in cap:
        bstack_options["os"] = cap["os"]
    if "deviceName" in cap:
        bstack_options['deviceName'] = cap["deviceName"]
    if cap['browserName'] in ['ios']:
        cap['browserName'] = 'safari'
    options = get_browser_option(cap["browserName"].lower())
    if "browserVersion" in cap:
        options.browser_version = cap["browserVersion"]
    options.set_capability('bstack:options', bstack_options)
    if cap['browserName'].lower() == 'samsung':
        options.set_capability('browserName', 'samsung')
    driver = webdriver.Remote(
        command_executor=URL,
        options=options)

    try:

        url = URLS.iewc
        logo = Home_Page.logo_a
        driver.get(url)
        xpath = Browser_Config.xpath
        logo_presence = driver.find_element(xpath,logo)
        assert logo_presence

    except NoSuchElementException as err:
        message = "Exception: " + str(err.__class__) + str(err.msg)
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": ' + json.dumps(message) + '}}')


    try:
        request = requests.get(url)
        request1 = str(request)
        request = request1.replace("<", "").replace(">", "")

        ok_status = "Response [200]"
        assert request == ok_status
        if request == ok_status:
            #print("Page returned status:", request + ". Page loaded successfully")
            return ok_status
        else:
            request = requests.get(url)
            request1 = str(request)
            request = request1.replace("<", "").replace(">", "")
            return request
            #print("Error loading site, Request returned: ", request)
    except NoSuchElementException as err:
        message = "Exception: " + str(err.__class__) + str(err.msg)
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": ' + json.dumps(message) + '}}')

    #driver.quit()
    driver.close()

for cap in capabilities:
    Thread(target=test_home_page, args=(cap,)).start()