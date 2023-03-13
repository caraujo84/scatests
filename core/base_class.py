import pytest
from utils.logger import Logger
from utils.wait_events import WaitEvents
from utils.screenshots_reports import ScreenshotsReports
from utils.simple_actions import SimpleActions
from utils.select_actions import SelectActions
from utils.random_actions import RandomActions
from utils.image_actions import ImageActions
from utils.fake_user import FakeUser
from utils.custom import Custom


@pytest.mark.usefixtures("setup")
class BaseClass:

    def get_logger(self):
        return Logger()

    def get_wait_utils(self):
        return WaitEvents(self.driver)

    def get_screenshot_utils(self):
        return ScreenshotsReports(self.driver)

    def get_simple_actions(self):
        return SimpleActions(self.driver)

    def get_select_actions(self):
        return SelectActions(self.driver)

    def get_random_actions(self):
        return RandomActions(self.driver)

    def get_image_actions(self):
        return ImageActions(self.driver)

    def get_fake_user_utils(self):
        return FakeUser()

    def get_custom_utils(self):
        return Custom(self.driver)
