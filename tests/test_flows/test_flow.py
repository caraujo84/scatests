import allure
import pytest
from core.base_class import BaseClass
from objects.pages.page import Page


class TestFlow(BaseClass):

    def initialize_objects(self):
        self.page = Page(self.driver)

    def manual_init(self, driver):
        self.driver = driver
        self.initialize_objects()

    @pytest.fixture(autouse=True)
    def auto_init(self):
        self.initialize_objects()

    @allure.story('flow')
    @allure.title('Flow Test')
    def test_flow_1(self):

        log = self.get_logger()
        simple_actions = self.get_simple_actions()

        # Click element presented in a component of the page
        simple_actions.element_click(self.page.component.component_element)

        # Click element presented in the page
        simple_actions.element_click(self.page.page_element)

        log.info('Flow Test 1')
        log.attach_log()
