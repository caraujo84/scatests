import allure
import pytest
from core.base_class import BaseClass
from tests.test_components.test_footer import TestFooter
from tests.test_flows.test_flow_register import TestFlowRegister


class TestSuiteSubscribeLogin(BaseClass):

    def initialize_objects(self):
        self.test_footer = TestFooter()
        self.test_footer.manual_init(self.driver)
        self.test_flow_register = TestFlowRegister()
        self.test_flow_register.manual_init(self.driver)

    @pytest.fixture
    def auto_init(self):
        self.initialize_objects()

    @allure.step
    def step_subscribe(self, user):
        allure.dynamic.parameter('Subscribe User', user.__str__())
        self.test_footer.test_footer_subscribe_form(None, user)

    @allure.step
    def step_login(self, user):
        allure.dynamic.parameter('Login User', user.__str__())
        self.test_flow_register.test_register(None, user, True)

    @allure.epic('subscribe_login_suite')
    def test_subscribe_login(self, auto_init):

        log = self.get_logger()
        fake_user_utils = self.get_fake_user_utils()

        custom_utils = self.get_custom_utils()
        custom_utils.pass_site_protection(log)

        log.info("Create fake user")
        user = fake_user_utils.get_fake_user()
        log.info("Test Subscribe")
        self.step_subscribe(user)
        log.info("Test Register")
        self.step_login(user)
        log.attach_log()
