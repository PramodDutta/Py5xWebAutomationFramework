import time
import pytest
import selenium
from selenium import webdriver
import allure
import logging

from test.pageObjects.pageFactory.loginPage_PageFactory import LoginPage
from test.pageObjects.pageFactory.dashboard_PageFactory import DashboardPage

from allure_commons.types import AttachmentType
from test.constants.constants import Constants


@allure.epic("VWO App")
@allure.feature("Login Test")
class TestVWOLogin:
    @pytest.mark.usefixtures("setup")
    @pytest.mark.qa
    def test_vwo_login_negative(self, setup):
        try:
            LOGGER = logging.getLogger(__name__)
            driver = setup
            driver.get(Constants.app_url())
            loginPage = LoginPage(driver)
            loginPage.login_to_vwo(usr=self.username, pwd=123)
            error_msg_element = loginPage.error_msg()
            assert error_msg_element == "Your email, password, IP address or location did not match"
        except Exception as e:
            print(e)

    @pytest.mark.usefixtures("setup")
    @pytest.mark.qa
    def test_vwo_login_positive(self, setup):
        driver = setup
        driver.get(Constants.app_url())
        login_page = LoginPage(driver)
        login_page.login_to_vwo(usr=self.username, pwd=self.password)
        dashboard_page = DashboardPage(driver)
        username = dashboard_page.user_logged_in_text()
        assert "Aman" == username

    @pytest.mark.usefixtures("setup")
    @pytest.mark.qa
    def test_vwo_login_negative_tc2(self, setup):
        pass
