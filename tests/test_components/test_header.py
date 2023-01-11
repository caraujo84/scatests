import pytest
import allure
from core.base_class import BaseClass
from objects.components.header import Header

class TestHeader(BaseClass):

    def initialize_objects(self):
        self.header = Header(self.driver)

    def manual_init(self, driver):
        self.driver = driver
        self.initialize_objects()
        
    @pytest.fixture
    def auto_init(self):
        self.initialize_objects()

    @allure.feature('header')
    def test_header_menu(self, auto_init):

        log = self.get_logger()
        simple_actions = self.get_simple_actions()
        screen_utils = self.get_screenshot_utils()
        error_count = 0
        
        menu_expected_titles = ['Personal', 'Business', 'Articles', 'Locations']
        menu_actual_titles = [
            simple_actions.get_element(self.header.menu_personal_item).text,
            simple_actions.get_element(self.header.menu_business_item).text,
            simple_actions.get_element(self.header.menu_articles_item).text,
            simple_actions.get_element(self.header.menu_locations_item).text,
        ]

        log.info('Start reviewing header menu titles')
        for expected_title, actual_title in zip(menu_expected_titles, menu_actual_titles):
            log.info(f'Review {expected_title}')
            if (expected_title != actual_title):
                log.error(f'"{actual_title}" title is incorrect')
                log.warning(f'Expected Title "{expected_title}"')
                screen_utils.add_screenshot('test_header_menu', expected_title)
                error_count += 1
            else:
                log.info(f'{expected_title} title text is correct')
                
        log.attach_log()
        if (error_count > 0):
            pytest.fail(f'There where {error_count} errors!')
