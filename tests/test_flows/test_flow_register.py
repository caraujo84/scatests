import allure
import pytest
from selenium.webdriver.common.by import By
from core.base_class import BaseClass
from objects.pages.home_page import HomePage
from objects.pages.log_in import LogIn
from objects.pages.profile_selection import ProfileSelection

class TestFlowRegister(BaseClass):

    def initialize_objects(self):
        self.home = HomePage(self.driver)
        self.login = LogIn(self.driver)
        self.profile = ProfileSelection(self.driver)
        
    def manual_init(self, driver):
        self.driver = driver
        self.initialize_objects()

    @pytest.fixture
    def auto_init(self):
        self.initialize_objects()
        
    @allure.story('register_flow')
    def test_register_flow(self, auto_init, user = None, review_name = False):
        
        log = self.get_logger()
        simple_actions = self.get_simple_actions()
        wait_utils = self.get_wait_utils()
        screen_utils = self.get_screenshot_utils()
        fake_user_utils = self.get_fake_user_utils()
        random_actions_utils = self.get_random_actions()

        error_count = 0
        user = user if user != None else fake_user_utils.get_fake_user()
        
        log.info('Start register a user')
        wait_utils.wait_element(self.home.utility_nav.log_In)
        log.info('Click on Log in link')
        simple_actions.element_click(self.home.utility_nav.log_In)
        wait_utils.wait_element(self.login.email_input)                            
        log.info(f"Enter email: {user.email}")
        simple_actions.element_send_key(self.login.email_input, user.email)
        log.info(f"Enter password: @Verndale321!")
        simple_actions.element_send_key(self.login.password_input, "@Verndale321!")
        log.info("Click login")
        simple_actions.element_click(self.login.login_btn)
        wait_utils.wait_element(self.login.continue_btn)
        continue_btn_text = simple_actions.get_element(self.login.continue_btn).text
        complete_name = f'{user.first_name} {user.last_name}'
        
        if review_name:
            if complete_name not in continue_btn_text:
                log.error(f'"{continue_btn_text}" name is incorrect')
                log.warning(f'Expected name "{complete_name}"')
                screen_utils.add_screenshot('test_login', complete_name)
                error_count += 1
            else:
                log.info(f'{complete_name} name is correct')
                
        simple_actions.element_click(self.login.continue_btn)
        wait_utils.wait_element(self.profile.job_type_select)
        selected_job_type = random_actions_utils.select_random_option(self.profile.job_type_select)
        log.info(f"Selected job type: {selected_job_type}")
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
        log.info("Choose a random profile")
        selected_profile = random_actions_utils.click_random_element_with_class(self.profile.profiles_container, 'resource-image-card')
        profile_name = selected_profile.find_element(By.TAG_NAME, 'H3')
        log.info(f"Profile selected: {profile_name}")
        profile_selector = (By.ID, selected_profile.get_attribute('data-modal-id'))
        selected_dialog = simple_actions.get_element(profile_selector)
        selected_dialog.find_element(By.TAG_NAME, 'button').click()
        wait_utils.wait_element(self.profile.thank_you_ok_btn)
        simple_actions.element_click(self.profile.thank_you_ok_btn)
        log.attach_log()
        
        if error_count > 0:
            pytest.fail(f'There where {error_count} errors!')  
            