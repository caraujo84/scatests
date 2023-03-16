import allure
import pytest
from core.base_class import BaseClass
from tests.test_components.test_component import TestComponent
from tests.test_flows.test_flow import TestFlow


class TestSuite(BaseClass):

    def initialize_objects(self):
        self.test_component = TestComponent()
        self.test_component.manual_init(self.driver)
        self.test_flow = TestFlow()
        self.test_flow.manual_init(self.driver)

    @pytest.fixture(autouse=True)
    def auto_init(self):
        self.initialize_objects()

    @allure.step('Step 1')
    def step_1(self):
        self.test_component.test_component_1()

    @allure.step('Step 2')
    def step_2(self):
        self.test_flow.test_flow_1()

    @allure.epic('suite')
    @allure.title('Suite Test')
    def test_suite_1(self):

        log = self.get_logger()
        log.info('Suite Test 1')

        # Run test component
        log.info("Test Component")
        self.step_1()

        # Run test flow
        log.info("Test Flow")
        self.step_2()
