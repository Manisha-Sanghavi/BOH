import json
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import time

from Features.Pages.BasePage import Basepage


class bohapk_page(Basepage):
    def __init__(self, context):
        Basepage.__init__(self, context.driver)
        self.context = context

    def enter_Username(self, username):
        user = self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.EditText[@text='email']")))
        user.click()
        user.send_keys(username)

    def enter_Password(self, password):
        password_field = self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.EditText[@text='password']")))
        password_field.click()
        password_field.send_keys(password)
        element = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.widget.ImageView)")))
        element.click()

    def clickOn_Login(self):
        # sleep(20)
        login = self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "//android.view.View[@content-desc='Sign In (DEV)']")))
        login.click()
        self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.Button[@content-desc='Skip']"))).click()

    # def Already_acc(self):
    #     alr_acc = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "//XCUIElementTypeButton[@name='Already Have An Account? Log In']")))
    #     alr_acc.click()

    def verify_page(self, message):
        try:
            cust_element = self.wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, "//android.view.View[@content-desc='" + message + "']")))
            text = cust_element.text
            print(text)
            assert text == "Customer Management"
        except AssertionError as msg:
            print(msg)

    def dev_build(self):

        element = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.widget.ImageView)")))
        actions = ActionChains(self.driver)
        try:

            actions.move_to_element(element)
            actions.click_and_hold(element)
            actions.release(element)
            # actions.click(hidden_submenu)
            actions.perform()
        except:
            print("Not Found element")
            # actions = ActionChains(self.driver)
            actions.move_to_element(element)
            actions.click_and_hold(element)
            actions.release(element)
            # actions.click(hidden_submenu)
            actions.perform()
