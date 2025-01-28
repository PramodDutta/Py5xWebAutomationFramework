import time

from seleniumpagefactory.Pagefactory import PageFactory
from test.utils.commom_utils import *

class DashboardPage(PageFactory):
    # Webdriver - Init
    def __init__(self, driver):
        self.driver = driver
        self.highlight = True

    locators = {
        'username_logged_in': ('XPATH', "//span[@data-qa='lufexuloga']")
    }

    def user_logged_in_text(self):
        webdriver_wait_url(driver=self.driver, timeout=10)
        return self.username_logged_in.get_text()