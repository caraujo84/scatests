import allure
import pytest
from selenium.webdriver.common.by import By
from core.base_class import BaseClass
from objects.pages.log_in import LogIn
from objects.pages.home_page import HomePage
from objects.pages.profile_selection import ProfileSelection
from tests.test_components.test_footer import TestFooter
from tests.test_flows.test_flow_register import TestFlowRegister

class TestSuiteSubscribeLogin(BaseClass):
    
    @pytest.fixture
    def initialize_objects(self):
        self.home = HomePage(self.driver)
        self.login = LogIn(self.driver)
        self.profile = ProfileSelection(self.driver)
        
    
    @allure.epic('subscribe_login_suite')
    def test_subscribe_login(self, initialize_objects):
        
        log = self.get_logger()
        error_count = 0
        
        log.info("Create fake user")
        user = self.get_fake_user()
        log.info("Test Subscribe")
        test_footer = TestFooter()
        test_footer.manual_init(self.driver)
        test_footer.test_footer_subscribe_form(None, user)
        log.info("Test Register")
        test_flow_register = TestFlowRegister()
        test_flow_register.manual_init(self.driver)
        test_flow_register.test_register_flow(None, user , True)
        