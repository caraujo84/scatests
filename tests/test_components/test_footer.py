import pytest
import allure
from core.base_class import BaseClass
from objects.components.footer import Footer

class TestFooter(BaseClass):

    def initialize_objects(self):
        self.footer = Footer(self.driver)
    
    def manual_init(self, driver):
        self.driver = driver
        self.initialize_objects()
        
    @pytest.fixture
    def auto_init(self):
        self.initialize_objects()
    
    @allure.feature('footer')
    def test_footer_subscribe_form(self, auto_init, user = None):
        
        log = self.get_logger()
        simple_actions = self.get_simple_actions()
        wait_utils = self.get_wait_utils()
        screen_utils = self.get_screenshot_utils()
        fake_user_utils = self.get_fake_user_utils()
        
        error_count = 0
        user = user if user is not None else fake_user_utils.get_fake_user()
        
        log.info('Start subscribe a user')
        wait_utils.wait_element(self.footer.input_name)
        simple_actions.element_send_key(self.footer.input_name, user.first_name)
        simple_actions.element_send_key(self.footer.input_last_name, user.last_name)
        simple_actions.element_send_key(self.footer.input_email, user.email)
        log.info(f'User first name: {user.first_name}')
        log.info(f'User last name: {user.last_name}')
        log.info(f'User email: {user.email}')
        simple_actions.element_click(self.footer.submit_btn)
        wait_utils.wait_element(self.footer.correct_message)
        actual_message = simple_actions.get_element(self.footer.correct_message).text
        expected_message = 'The form has been submitted successfully.'
        if (actual_message != expected_message):
            log.error(f'"{actual_message}" message is incorrect')
            log.warning(f'Expected message "{expected_message}"')
            screen_utils.add_screenshot('test_footer', 'test_footer')
            error_count += 1
        else:
            log.info(f'Subscribe message is correct')
            
        log.attach_log()
        if (error_count > 0):
            pytest.fail(f'There where {error_count} errors!')
