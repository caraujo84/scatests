from utils.simple_actions import SimpleActions
from objects.pages.site_protection import SiteProtection

class Custom:

    def __init__(self, driver):
        self.driver = driver

    def pass_site_protection(self, log):
        simple_actions = SimpleActions(self.driver)
        siteProtection = SiteProtection(self.driver)
        log.info("Try to pass site protection")
        if not simple_actions.check_element_exists(siteProtection.username) or not simple_actions.check_element_exists(siteProtection.password) or not simple_actions.check_element_exists(siteProtection.loginBtn):
            log.warning("Couldn't find fields")
            return
        simple_actions.element_send_key(
            siteProtection.username, "OptiInfinityBank")
        simple_actions.element_send_key(
            siteProtection.password, "@Verndale321!")
        simple_actions.element_click(siteProtection.loginBtn)
        log.info("Site protection passed")
