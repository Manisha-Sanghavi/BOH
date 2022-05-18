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

class RE_Page(Basepage):
    def __init__(self, context):
        Basepage.__init__(self, context.driver)
        self.context = context

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

        except:
            print("Skip is skipped")

    def verify_page(self, message):
        try:
            cust_element = self.wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, "//android.view.View[@content-desc='" + message + "']")))
            text = cust_element.text
            print(text)
            assert text == "Customer Management"
        except AssertionError as msg:
            print(msg)

    def re_tab(self):
        self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[9]"))).click()

    def click_sortby(self):
        self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[17]"))).click()

    def verify_dropdownlist(self):
        # def select_option(option_list):
        #     for ele in option_list:
        #         print(ele.text)


        #self.driver.find_element(MobileBy.XPATH, "(//android.view.View)[17]").click()
        a = self.driver.find_elements(MobileBy.CLASS_NAME, '//android.widget.Button')
        ele_name = a.getattr("text")
        print(ele_name)
        # b = self.driver.find_elements(MobileBy.XPATH, '//android.widget.Button[@content-desc="RE Date"]').text
        # c = self.driver.find_elements(MobileBy.XPATH, '//android.widget.Button[@content-desc="Value"]').text
        # d = self.driver.find_elements(MobileBy.XPATH, '//android.widget.Button[@content-desc="REID"]').text
        # e = self.driver.find_elements(MobileBy.XPATH, '//android.widget.Button[@content-desc="Location"]').text
        # f = self.driver.find_elements(MobileBy.XPATH, '//android.widget.Button[@content-desc="CSM"]').text
        # g = self.driver.find_elements(MobileBy.XPATH, '//android.widget.Button[@content-desc="Status"]').text

        print(len(a))

        #select_option(dropdownlist)


