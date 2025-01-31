import allure
import pytest

from core.base_class import BaseClass
from objects.components.component import Component


class TestComponent(BaseClass):
    def initialize_objects(self):
        self.component = Component(self.driver)

    def manual_init(self, driver):
        self.driver = driver
        self.initialize_objects()

    @pytest.fixture(autouse=True)
    def auto_init(self):
        self.initialize_objects()

    @allure.feature("component")
    @allure.title("Component Test")
    def test_component_1(self):
        log = self.get_logger()
        simple_actions = self.get_simple_actions()

        # Click element presented in a component
        simple_actions.element_click(self.component.component_element)

        log.info("Component Test 1")
        log.attach_log()
