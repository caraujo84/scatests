import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from core.urls import URLS

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser-name", action="store", default="chrome", choices=("chrome", "firefox", "edge")
    )
    parser.addoption(
        "--headless", action="store", default="false", choices=("true", "false")
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        if request.config.getoption("headless") == 'true':
            options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()))
    elif browser_name == "edge":
        options = webdriver.EdgeOptions()
        if request.config.getoption("headless") == 'true':
            options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Edge(service=EdgeService(
            EdgeChromiumDriverManager().install()))
    else:
        options = webdriver.ChromeOptions()
        if request.config.getoption("headless") == 'true':
            options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()), options=options)

    driver.get(URLS.site_url)
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()
