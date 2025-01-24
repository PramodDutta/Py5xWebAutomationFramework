from selenium import webdriver
import allure
import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from dotenv import load_dotenv
import os
from test.utils.Utils import *


@allure.title("VWO Login Negative Testcase")
@allure.description("TC1 - Negative TC - VWO Login with invalid creds.")
@allure.feature("VWO Login with invalid creds")
@pytest.mark.negativevwologin
def test_app_vwo_login_chrome():
    load_dotenv()
    match os.getenv("BROWSER"):
        case "chrome":
            chrome_options = Options()
            chrome_options.add_argument("--incognito")
            driver = webdriver.Chrome(options=chrome_options)

        case "edge":
            edge_options = Options()
            edge_options.add_argument("--inprivate")
            driver = webdriver.Edge(options=edge_options)

        case "firefox":
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.add_argument("-private")
            driver = webdriver.Firefox(options=firefox_options)
        case _:
            print("Browser not found!")
            exit(1)

    driver.get(os.getenv("URL"))

    take_screen_shot(driver=driver, name="vwoLogin_Step1")


    email_web_element = driver.find_element(By.ID, "login-username")
    email_web_element.send_keys(os.getenv("INVALID_USERNAME"))

    password_web_element = driver.find_element(By.NAME, "password")
    password_web_element.send_keys(os.getenv("INVALID_PASSWORD"))

    submit_btn_web_element = driver.find_element(By.ID, "js-login-btn")
    submit_btn_web_element.click()

    take_screen_shot(driver=driver, name="vwoLogin_Step2")


    time.sleep(3)

    error_message_web_element = driver.find_element(By.CLASS_NAME, "notification-box-description")
    print(error_message_web_element.text)

    take_screen_shot(driver=driver, name="vwoLogin_Step3")

    assert error_message_web_element.text == os.getenv("error_message_expected")

    time.sleep(5)
    driver.quit()  # close everything.
