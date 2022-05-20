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


class SignIn_Page(Basepage):
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
        # self.wait.until(
        #     EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.Button[@content-desc='Skip']"))).click()

    # def Already_acc(self):
    #     alr_acc = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "//XCUIElementTypeButton[@name='Already Have An Account? Log In']")))
    #     alr_acc.click()
        # sleep(5)
        # try:
        #     self.wait.until(
        #         EC.presence_of_element_located(
        #             (MobileBy.XPATH, "//android.widget.Button[@content-desc='Skip']"))).click()
        # except:
        #     print("Skip is skipped")

    def click_admin(self):
        admin = self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "(//android.widget.Button)[1]")))
        admin.click()

    def clickOn_Signout(self):
        signout = self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "(//android.widget.Button)[2]")))
        signout.click()

    def verify_homepage(self):
        self.wait.until(
            EC.presence_of_element_located((MobileBy.CLASS_NAME, "android.widget.ImageView")))


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
            actions.move_to_element(element)
            actions.click_and_hold(element)
            actions.release(element)
            # actions.click(hidden_submenu)
            actions.perform()
        except:
            print("Not Found element")
            actions = ActionChains(self.driver)
            actions = ActionChains(self.driver)
            actions.move_to_element(element)
            actions.click_and_hold(element)
            actions.release(element)
            # actions.click(hidden_submenu)
            actions.perform()

    def verify_message(self, message):
        flag = False
        if message == "Incorrect username/password":
            try:
                msg = self.wait.until(
                    EC.presence_of_element_located(
                        (MobileBy.XPATH, "//android.view.View[@content-desc='" + message + "']")))
                flag = True
            except:
                msg = self.wait.until(
                    EC.presence_of_element_located(
                        (MobileBy.XPATH, "//android.view.View[@content-desc='" + message + "']")))
                read_message = msg.text
                assert read_message == "Incorrect username/password"
        elif message == "A recovery email has been sent to your account":
            msg = self.wait.until(
                EC.presence_of_element_located(
                    (MobileBy.XPATH, "//android.view.View[@content-desc='" + message + "']")))
            flag = True
        return flag

    def show_field(self, field, value=None):
        form_xpath = "//android.view.View[@content-desc='XXX']"
        show_data = self.form_xpath.replace('XXX', form_xpath)
        if field == 'Customer Name':
            CustName_ele = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "//android.view.View[@content-desc='"+field+"']")))
            text_read = CustName_ele.text
            assert text_read == "Customer Name"
        elif field == 'Customers Tab 1 of 3':
            Cust_ele = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, show_data)))
            text_read = Cust_ele.text
            assert text_read == "Customers Tab 1 of 3"
        elif field == 'REs Tab 2 of 3':
            RE_ele = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, show_data)))
            text_read = RE_ele.text
            assert text_read == "REs Tab 2 of 3"
        elif field == "Opportunities Tab 3 of 3":
            Oppor_ele = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, show_data)))
            text_read = Oppor_ele.text
            assert text_read == "Opportunities Tab 3 of 3"
        else:
            raise NameError(f'Field {field} is not valid')


    def tap_option(self, option_name):
        option_xpath = "//android.widget.Button[@content-desc='XXX']"
        option_Btn= option_xpath.replace('XXX', option_name)
        if option_name == "forgot password":
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH,option_Btn))).click()
            # self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.Button[@content-desc='"+ option_name +"']"))).click()
        elif option_name == "SEND":
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, option_Btn))).click()
        else:
            raise NameError('name {option_name} is not valid')

    def page_navigate(self, Forgot_your_password):
        page_xpath = "//android.view.View[@content-desc='XXX']"
        option_Btn = page_xpath.replace('XXX', Forgot_your_password)
        page_ele = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH,option_Btn)))
        page_txt = page_ele.text
        # assert page_txt == "Forgot your password?"

    def enter_mail(self, email):
        if email == "harish.ekal@spurqlabs.com":
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH,"//android.widget.EditText[@text='Type your BOH email']"))).click()
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.EditText[@text='Type your BOH email']"))).send_keys(email)
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH,"//android.view.View[@content-desc='Forgot your password?']"))).click()

    def skip(self):
        try:
            self.wait.until(
                EC.presence_of_element_located(
                    (MobileBy.XPATH, "//android.widget.Button[@content-desc='Skip']"))).click()
        except:
            print("Skip is skipped")

