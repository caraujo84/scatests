import allure
import pytest
from core.base_class import BaseClass
from objects.pages.log_in import LogIn
from objects.pages.home_page import HomePage
from objects.pages.profile_selection import ProfileSelection
from tests.test_components.test_footer import TestFooter
from tests.test_flows.test_flow_register import TestFlowRegister

class TestSuiteSubscribeLogin(BaseClass):

    def initialize_objects(self):
        self.home = HomePage(self.driver)
        self.login = LogIn(self.driver)
        self.profile = ProfileSelection(self.driver)
        self.test_footer = TestFooter()
        self.test_footer.manual_init(self.driver)
        self.test_flow_register = TestFlowRegister()
        self.test_flow_register.manual_init(self.driver)
    
    @pytest.fixture
    def auto_init(self):
        self.initialize_objects()
    
    @allure.epic('subscribe_login_suite')
    def test_subscribe_login(self, auto_init):
        
        log = self.get_logger()
        fake_user_utils = self.get_fake_user_utils()

        log.info("Create fake user")
        user = fake_user_utils.get_fake_user()
        log.info("Test Subscribe")
        self.test_footer.test_footer_subscribe_form(None, user)
        log.info("Test Register")
        self.test_flow_register.test_register_flow(None, user , True)
        