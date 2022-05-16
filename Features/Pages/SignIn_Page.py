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

    form_xpath = "//android.view.View[@content-desc='XXX']"

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

    def verify_message(self, message):
        msg = self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "//android.view.View[@content-desc='" + message + "']")))
        read_message = msg.text
        print(read_message)
        assert read_message == "Incorrect username/password"
        # msg = self.wait.until(EC.presence_of_element_located(MobileBy.XPATH,""))

    def show_field(self, field):
        write_data = self.form_xpath.replace('XXX', field)
        if field == 'Customer Name':
            CustName_ele = self.wait.until(EC.presence_of_element_located(MobileBy.XPATH, write_data))
            text_read = CustName_ele.text
            assert text_read == "Customer Name"
        elif field == 'Customers Tab 1 of 3':
            Cust_ele = self.wait.until(EC.presence_of_element_located(MobileBy.XPATH, write_data))
            text_read = Cust_ele.text
            assert text_read == "Customers Tab 1 of 3"
        elif field == 'REs Tab 2 of 3':
            RE_ele = self.wait.until(EC.presence_of_element_located(MobileBy.XPATH, write_data))
            text_read = RE_ele.text
            assert text_read == "REs Tab 2 of 3"
        elif field == "Opportunities Tab 3 of 3":
            Oppor_ele = self.wait.until(EC.presence_of_element_located(MobileBy.XPATH, write_data))
            text_read = Oppor_ele.text
            assert text_read == "Opportunities Tab 3 of 3"
        else:
            raise NameError(f'Field {field} is not valid')
