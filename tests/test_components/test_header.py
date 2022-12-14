import pytest
from utilities.BaseClass import BaseClass
from objects.components.header import Header

class TestHeader(BaseClass):

    def test_header_menu(self):

        log = self.get_logger()
        error_count = 0
        header = Header(self.driver)

        log.info('Click menu button')
        self.wait_element(header.menu_btn)
        self.get_element_click(header.menu_btn)
        log.info('Review all the sub items')
        self.wait_element(header.menu_item_work)
        self.get_element_click(header.menu_item_work)
        log.info('Review Work Title')
        work_real_title = self.get_element(header.menu_work_title).text
        if (work_real_title == 'Our Works'):
            log.info('Work title is correct')
        else:
            error_count += 1
            log.error(f'The title "{work_real_title}" is incorrect')
            log.warning('Expected Work title: Our Works')
            self.add_screenshot('test_header_menu', 'work_title_screenshot')
        self.get_element_click(header.menu_item_expertise)
        log.info('Review Expertise Title')
        expertise_real_title = self.get_element(header.menu_expertise_title).text
        if (expertise_real_title == 'Our Expertise'):
            log.info('Expertise title is correct')
        else:
            error_count += 1
            log.error(f'The title "{expertise_real_title}" is incorrect')
            log.warning('Expected Expertise title: Our Expertise')
            self.add_screenshot('test_header_menu', 'expertise_title_screenshot')
        log.attach_log()
        if (error_count > 0):
            pytest.fail(f'There where {error_count} errors!')
