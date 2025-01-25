# Dashboard Page Class

# Page Locators
# Page Actions


from selenium.webdriver.common.by import By
from test.utils.commom_utils import webdriver_wait


class FreeTrialPage:
    def __init__(self, driver):
        self.driver = driver

    username_email_ft = (By.XPATH, "//input[@id='page-v1-step1-email']")
    button_click_ft = (By.XPATH, "//button[normalize-space()='Create a Free Trial Account']")
    checkbox_terms = (By.XPATH, "//input[@id='page-756cu-gdpr-consent-checkbox']")
    error_msg_invalid_email = (By.XPATH, "//div[normalize-space()='The email address you entered is incorrect.']")

    def get_username_ft(self):
        webdriver_wait(driver=self.driver, element_tuple=self.username_email_ft, timeout=5)
        return self.driver.find_element(*FreeTrialPage.username_email_ft)

    def get_button_click_ft(self):
        return self.driver.find_element(*FreeTrialPage.button_click_ft)

    def get_button_checkbox_terms(self):
        return self.driver.find_element(*FreeTrialPage.checkbox_terms)

    def get_error_msg_invalid_email(self):
        return self.driver.find_element(*FreeTrialPage.error_msg_invalid_email)

    def get_error_message_text(self):
        webdriver_wait(driver=self.driver, element_tuple=self.error_msg_invalid_email, timeout=15)
        return self.get_error_msg_invalid_email().text

    def enter_free_trial_details_invalid(self, invalid_email):
        try:
            self.get_username_ft().send_keys(invalid_email)
            self.get_button_checkbox_terms().click()
            webdriver_wait(driver=self.driver, element_tuple=self.button_click_ft, timeout=2)
            self.get_button_click_ft().click()
        except Exception as e:
            print(e)
