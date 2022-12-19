import allure
import pytest
from selenium.webdriver.common.by import By
from utilities.base_class import BaseClass
from objects.pages.log_in import LogIn
from objects.pages.home_page import HomePage
from objects.pages.profile_selection import ProfileSelection
from tests.test_components.test_footer import TestFooter
from tests.test_flows.test_flow_register import TestFlowRegister

class TestFlowSubscribeLogin(BaseClass):
    
    @pytest.fixture
    def initialize_objects(self):
        self.home = HomePage(self.driver)
        self.login = LogIn(self.driver)
        self.profile = ProfileSelection(self.driver)
        
    
    @allure.story('subscribe_login_flow')
    def test_subscribe_login(self, initialize_objects):
        
        log = self.get_logger()
        error_count = 0
        
        log.info("Create fake user")
        user = self.get_fake_user()
        log.info("Test Subscribe")
        test_footer = TestFooter()
        test_footer.test_footer_subscribe_form(user)
        log.info("Test Register")
        TestFlowRegister.test_register_flow(self, TestFlowRegister.initialize_objects, user , review_name = True)
        