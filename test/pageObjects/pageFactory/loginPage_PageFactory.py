# Page Locators
# Page Actions

from seleniumpagefactory.Pagefactory import PageFactory
from test.utils.commom_utils import *
from selenium.webdriver.common.by import By

class LoginPage(PageFactory):

    def __init__(self,driver):
        self.driver = driver
        self.highlight = True

    locators = {
        'username': ('CSS', "#login-username"),
        'password': ('NAME', 'password'),
        'error_message': ('CSS', '#js-notification-box-msg'),
        'submit_button': ('XPATH', '//button[@id="js-login-btn"]')
    }

    def login_to_vwo(self,usr,pwd):
        self.username.set_text(usr)
        self.password.set_text(pwd)
        self.submit_button.click_button()

    def error_msg(self):
        return self.error_message.get_text()


