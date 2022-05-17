import json
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
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
        #time.sleep(20)
        login = self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "//android.view.View[@content-desc='Sign In (DEV)']")))
        login.click()
        sleep(5)
        try:
            self.wait.until(
                EC.presence_of_element_located(
                    (MobileBy.XPATH, "//android.widget.Button[@content-desc='Skip']"))).click()
        except AssertionError as msg:
            print(msg)

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
        try:
            element = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.widget.ImageView)")))
            actions = ActionChains(self.driver)
            # actions.move_to_element(element)
            actions.click_and_hold(element)
            actions.release(element)
            # actions.click(hidden_submenu)
            actions.perform()
        except:
            print("Not Found element")
            # actions = ActionChains(self.driver)
            # # actions.move_to_element(element)
            actions.click_and_hold(element)
            actions.release(element)
            # actions.click(hidden_submenu)
            actions.perform()

    def verify_tabs(self):
        try:
            cust_tab = self.wait.until(EC.presence_of_element_located(
            (MobileBy.XPATH, "(//android.view.View)[8]")))
            text1 = cust_tab.text
            print(text1)
            assert text1 == "Customers"
        except AssertionError as msg:
            print(msg)

        try:
            re_tab = self.wait.until(EC.presence_of_element_located(
            (MobileBy.XPATH, "(//android.view.View)[8]")))
            text = re_tab.text
            print(text)
            assert text == "REs"
        except AssertionError as msg:
            print(msg)

    def clickOn_Signout(self):
        signout = self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "(//android.widget.Button)[2]")))
        signout.click()

    def click_admin(self):
        admin = self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "(//android.widget.Button)[1]")))
        admin.click()

    def verify_homepage(self):
        homepage = self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "(//android.widget.ImageView)")))
        homepage.click()

    def re_tab(self):
        self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[9]"))).click()

    def click_sortby(self):
        self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[17]"))).click()

    def verify_dropdownlist(self):
        sort_options = self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[17]")))
        select = Select(sort_options)
        option_list = select.options

        for ele in option_list:
            print(ele.text)

