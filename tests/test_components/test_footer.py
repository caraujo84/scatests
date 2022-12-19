import pytest
import allure
from utilities.base_class import BaseClass
from objects.components.footer import Footer

class TestFooter(BaseClass):
    
    @allure.feature('footer')
    def test_footer_subscribe_form(self, user = None):
        
        log = self.get_logger()
        error_count = 0
        footer = Footer(self.driver)
        user = user if user != None else self.get_fake_user()
        
        log.info('Start subscribe a user')
        self.wait_element(footer.input_name)
        self.element_send_key(footer.input_name, user.first_name)
        self.element_send_key(footer.input_last_name, user.last_name)
        self.element_send_key(footer.input_email, user.email)
        log.info(f'User first name: {user.first_name}')
        log.info(f'User last name: {user.last_name}')
        log.info(f'User email: {user.email}')
        self.element_click(footer.submit_btn)
        self.wait_element(footer.correct_message)
        actual_message = self.get_element(footer.correct_message).text
        expected_message = 'The form has been submitted successfully.'
        if (actual_message != expected_message):
            log.error(f'"{actual_message}" message is incorrect')
            log.warning(f'Expected message "{expected_message}"')
            self.add_screenshot('test_footer', 'test_footer')
            error_count += 1
        else:
            log.info(f'Subscribe message is correct')
            
        if (error_count > 0):
            pytest.fail(f'There where {error_count} errors!')
