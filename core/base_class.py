import pytest

from utils.custom import Custom
from utils.fake_user import FakeUser
from utils.image_actions import ImageActions
from utils.logger import Logger
from utils.random_actions import RandomActions
from utils.screenshot_actions import ScreenshotActions
from utils.select_actions import SelectActions
from utils.simple_actions import SimpleActions
from utils.switch_actions import SwitchActions
from utils.wait_actions import WaitActions


@pytest.mark.usefixtures("setup")
class BaseClass:

    def get_logger(self):
        return Logger()

    def get_fake_user_utils(self):
        return FakeUser()

    def get_wait_actions(self):
        return WaitActions(self.driver)

    def get_screenshot_actions(self):
        return ScreenshotActions(self.driver)

    def get_simple_actions(self):
        return SimpleActions(self.driver)

    def get_select_actions(self):
        return SelectActions(self.driver)

    def get_random_actions(self):
        return RandomActions(self.driver)
    
    def get_switch_actions(self):
        return SwitchActions(self.driver)

    def get_image_actions(self):
        return ImageActions(self.driver)

    def get_custom_utils(self):
        return Custom(self.driver)
