import allure
import pytest
from selenium.webdriver.common.by import By
from core.base_class import BaseClass
from objects.pages.home_page import HomePage
from objects.pages.social_sign_in import SocialSignIn
from objects.pages.login import Login
from objects.pages.profile_selection import ProfileSelection

class TestFlowRegister(BaseClass):

    def initialize_objects(self):
        self.home = HomePage(self.driver)
        self.socialSignIn = SocialSignIn(self.driver)
        self.login = Login(self.driver)
        self.profile = ProfileSelection(self.driver)
        
    def manual_init(self, driver):
        self.driver = driver
        self.initialize_objects()

    @pytest.fixture
    def auto_init(self):
        self.initialize_objects()
        
    @allure.story('register_flow')
    def test_register(self, auto_init, user = None, review_name = False):
        
        log = self.get_logger()
        simple_actions = self.get_simple_actions()
        wait_utils = self.get_wait_utils()
        screen_utils = self.get_screenshot_utils()
        fake_user_utils = self.get_fake_user_utils()
        random_actions_utils = self.get_random_actions()

        custom_utils = self.get_custom_utils()
        custom_utils.pass_site_protection(log)

        error_count = 0
        user = user if user != None else fake_user_utils.get_fake_user()
        
        log.info('Start register a user')
        wait_utils.wait_element(self.home.utility_nav.log_In)
        log.info('Click on Log in link')
        simple_actions.element_click(self.home.utility_nav.log_In)
        wait_utils.wait_element(self.login.socialSignInBtn)
        log.info('Login Page Loaded')
        log.info('Click on Social Sign in Button')
        simple_actions.element_click(self.login.socialSignInBtn)
        wait_utils.wait_element(self.socialSignIn.email_input)
        log.info('Social Sign in Page Loaded')
        log.info(f"Enter email: {user.email}")
        simple_actions.element_send_key(self.socialSignIn.email_input, user.email)
        log.info(f"Enter password: @Verndale321!")
        simple_actions.element_send_key(self.socialSignIn.password_input, "@Verndale321!")
        log.info("Click login")
        simple_actions.element_click(self.socialSignIn.login_btn)
        wait_utils.wait_element(self.socialSignIn.continue_btn)
        log.info("Permissions Page Loaded")
        continue_btn_text = simple_actions.get_element(self.socialSignIn.continue_btn).text
        complete_name = f'{user.first_name} {user.last_name}'
        
        if review_name:
            if complete_name not in continue_btn_text:
                log.error(f'"{continue_btn_text}" name is incorrect')
                log.warning(f'Expected name "{complete_name}"')
                screen_utils.add_screenshot('test_login', complete_name)
                error_count += 1
            else:
                log.info(f'{complete_name} name is correct')
                
        simple_actions.element_click(self.socialSignIn.continue_btn)
        wait_utils.wait_element(self.profile.employee_status)
        log.info("Profile Selection Page Loaded")
        selected_employee_status = random_actions_utils.select_random_option(self.profile.employee_status)
        log.info(f"Selected employee status: {selected_employee_status}")
        selected_annual_income = random_actions_utils.select_random_option(self.profile.annual_income_select)
        log.info(f"Selected annual income: {selected_annual_income}")
        simple_actions.element_send_key(self.profile.phone_number_input, user.phone)
        children = random_actions_utils.select_random_radio_button(self.profile.children_radio_buttons)
        log.info(f"Has children: {children}")
        homeowner = random_actions_utils.select_random_radio_button(self.profile.homeowner_radio_buttons)
        log.info(f"Homewoner: {homeowner}")
        simple_actions.element_click(self.profile.submit_btn)
        log.info("Send data")
        wait_utils.wait_element(self.profile.thank_you_ok_btn)
        simple_actions.element_click(self.profile.thank_you_ok_btn)
        log.attach_log()
        
        if error_count > 0:
            pytest.fail(f'There where {error_count} errors!')  
            