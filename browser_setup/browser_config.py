class Browser_Config():

    # Setting up browser
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By

    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--start-maximized")



    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    xpath = By.XPATH
    id = By.ID
    tag = By.TAG_NAME