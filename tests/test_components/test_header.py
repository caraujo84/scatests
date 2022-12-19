import pytest
import allure
from utilities.base_class import BaseClass
from objects.components.header import Header

class TestHeader(BaseClass):

    @allure.feature('header')
    def test_header_menu(self):

        log = self.get_logger()
        error_count = 0
        header = Header(self.driver)
        
        menu_expected_titles = ['Personals', 'Businesss', 'Articles', 'Locations']
        menu_actual_titles = [
            self.get_element(header.menu_personal_item).text,
            self.get_element(header.menu_business_item).text,
            self.get_element(header.menu_articles_item).text,
            self.get_element(header.menu_locations_item).text,
        ]

        log.info('Start reviewing header menu titles')
        for expected_title, actual_title in zip(menu_expected_titles, menu_actual_titles):
            log.info(f'Review {expected_title}')
            if (expected_title != actual_title):
                log.error(f'"{actual_title}" title is incorrect')
                log.warning(f'Expected Title "{expected_title}"')
                self.add_screenshot('test_header_menu', expected_title)
                error_count += 1
            else:
                log.info(f'{expected_title} title text is correct')
                
        log.attach_log()
        if (error_count > 0):
            pytest.fail(f'There where {error_count} errors!')
