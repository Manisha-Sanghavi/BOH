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

    form_xpath = "//android.view.View[@content-desc='XXX']"
    option_xpath = "//android.widget.Button[@content-desc='XXX']"

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
                flag = True
        elif message == "A recovery email has been sent to your account":
            msg = self.wait.until(
                EC.presence_of_element_located(
                    (MobileBy.XPATH, "//android.view.View[@content-desc='" + message + "']")))
            flag = True
        elif message == "John J":
            # msg = self.wait.until(
            #     EC.presence_of_element_located(
            #         (MobileBy.XPATH, "//android.view.View[@content-desc='" + message + "']")))
            # flag = True
            self.wait.until(
                EC.presence_of_element_located(
                    (MobileBy.XPATH, "(//android.view.View)[1]"))).click()
            self.wait.until(
                EC.presence_of_element_located(
                    (MobileBy.XPATH, "//android.view.View[@content-desc='INFO Tab 1 of 3']"))).click()
            self.wait.until(
                EC.presence_of_element_located(
                    (MobileBy.XPATH, "//android.view.View[@content-desc='Delete John J?']"))).click()
            self.wait.until(
                EC.presence_of_element_located(
                    (MobileBy.XPATH, "//android.widget.Button[@content-desc='Yes']"))).click()
        elif message == "All associated data will be permanently removed":
            msg = self.wait.until(
                EC.presence_of_element_located(
                    (MobileBy.XPATH, "//android.view.View[@content-desc='" + message + "']")))
            flag = True
            self.wait.until(
                EC.presence_of_element_located(
                    (MobileBy.XPATH, "//android.widget.Button[@content-desc='Yes']"))).click()
        # elif message == "Joe M":
        #     user = self.wait.until(
        #         EC.presence_of_element_located(
        #             (MobileBy.XPATH, "(//android.view.View)[7]")))
        #     txt = user.get_attribute('content-desc')
        #     print('Value of Text:'+txt)
        #     value = txt.split()
        #     print(value)
        #     msg = value[0:1]
        #     print(msg)
        #     flag = True
        return flag

    def show_field(self, field):
        flag = False
        form_xpath = "//android.view.View[@content-desc='XXX']"
        show_data = form_xpath.replace('XXX', field)
        CustName_ele = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, show_data)))
        flag = True
        if field == 'Customer Management':
            CustName_ele = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, show_data)))
            # text_read = CustName_ele.text
            # print(text_read)
            # assert text_read == "Customer Name"
            flag = True
        elif field == 'Customers Tab 1 of 3':
            Cust_ele = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[8]")))
            # text_read = Cust_ele.text
            # print(text_read)
            # assert text_read == "Customers Tab 1 of 3"
            flag = True
        elif field == 'REs Tab 2 of 3':
            RE_ele = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[9]")))
            # text_read = RE_ele.text
            # print(text_read)
            # assert text_read == "REs Tab 2 of 3"
            flag = True
        elif field == "Opportunities Tab 3 of 3":
            Oppor_ele = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[10]")))
            # text_read = Oppor_ele.text
            # print(text_read)
            # assert text_read == "Opportunities Tab 3 of 3"
            flag = True
        else:
            raise NameError(f'Field {field} is not valid')
        return flag

    def tap_option(self, option_name):
        option_xpath = "//android.widget.Button[@content-desc='XXX']"
        option_Btn = option_xpath.replace('XXX', option_name)
        if option_name == "forgot password" or option_name == "SEND" or option_name == "CREATE TOUCHBASE" or option_name == "Search":
            tap_btn = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.widget.Button)[2]")))
            tap_btn.click()
            if option_name == "CREATE TOUCHBASE":
                try:
                    print(option_Btn)
                    tap_btn.click()
                    tap_btn.click()
                except:
                    actions = ActionChains(self.driver)
                    actions.move_to_element(tap_btn)
                    actions.click_and_hold(tap_btn)
                    actions.release(tap_btn)
                    actions.perform()
                # sleep(5)
        elif option_name == "Add Touchbase":
            option_xpath = "//android.widget.ImageView[@content-desc='XXX']"
            option_Btn = option_xpath.replace('XXX', option_name)
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, option_Btn))).click()
        elif option_name == "+":
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.widget.ImageView)[1]"))).click()
        elif option_name == "INFO Tab 1 of 3" or option_name == "Delete John J" or option_name == "Show menu Active":
            option_xpath = "//android.view.View[@content-desc='XXX']"
            option_Btn = option_xpath.replace('XXX', option_name)
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, option_Btn))).click()
        elif option_name == "Remember Me":
            self.wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, "//android.widget.CheckBox[@content-desc='Remember Me']"))).click()
        elif option_name == "Sort By":
            self.wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, "(//android.view.View)[17]"))).click()
        elif option_name == "filter By":
            self.wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, "(//android.view.View)[19]"))).click()
        elif option_name == "ACTIVE":
            self.wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, "//android.view.View[@content-desc='"+option_name+"']"))).click()
        elif option_name == "INACTIVE":
            self.wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, "//android.view.View[@content-desc='"+option_name+"']"))).click()
        elif option_name == "Set Customer to Inactive":
            self.wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, "//android.view.View[@content-desc='Set Customer as Inactive']"))).click()
        elif option_name == "Set Customer to Active":
            self.wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, "//android.view.View[@content-desc='Set Customer as Active']"))).click()
        else:
            raise NameError('name {option_name} is not valid')

    def page_navigate(self, Forgot_your_password):
        page_xpath = "//android.view.View[@content-desc='XXX']"
        option_Btn = page_xpath.replace('XXX', Forgot_your_password)
        flag = False
        try:
            page_ele = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, option_Btn)))
            flag = True
        except:
            print("User not navigated to page")
            page_ele = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(// android.view.View)[10]")))
            flag = True
        return flag
        # assert page_txt == "Forgot your password?"

    def enter_mail(self, email):
        if email == "harish.ekal@spurqlabs.com":
            self.wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, "//android.widget.EditText[@text='Type your BOH email']"))).click()
            self.wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, "//android.widget.EditText[@text='Type your BOH email']"))).send_keys(email)
        self.wait.until(EC.presence_of_element_located(
            (MobileBy.XPATH, "//android.view.View[@content-desc='Forgot your password?']"))).click()

    def skip(self):
        try:
            self.wait.until(
                EC.presence_of_element_located(
                    (MobileBy.XPATH, "//android.widget.Button[@content-desc='Skip']"))).click()
        except:
            print("Skip is skipped")

    def fill_data(self, field, value):
        write_data_xpath = "//android.widget.EditText[@text='XXX']"
        fill_data = write_data_xpath.replace('XXX', field)
        search_cust = "//android.widget.EditText[@text='Search Customers']"
        search_loc = "//android.widget.EditText[@text='Search Locations']"
        if field == "Customer":
            search_cust = "//android.widget.EditText[@text='Search Customers']"
            # add_cust = search_cust.replace('XXX',value)
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, fill_data))).click()
            if field == "Customer":
                self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, search_cust))).send_keys(value)
                self.wait.until(EC.presence_of_element_located(
                    (MobileBy.XPATH, '//android.view.View[@content-desc="Add Customer \'' + value + '\'"]'))).click()
            # elif field == "Notes":
            #     self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, fill_data))).click()
            #     self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, fill_data))).send_keys(value)
            #     self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "//android.view.View[@content-desc='New Touchbase']"))).click()
            # try:
            #     self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, search_cust))).send_keys(value)
            # except:
            #     print("This is for adding customer only.")
            #     # self.wait.until(EC.presence_of_element_located(
            #     #     (MobileBy.XPATH, "//android.view.View[@content-desc='Add Customer '"+value+"'']"))).click()
        elif field == "Location":
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, fill_data))).click()
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, search_loc))).send_keys(value)
            self.wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, '//android.view.View[@content-desc="Add Location \'' + value + '\'"]'))).click()
        elif field == "Contact":
            self.wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, "//android.widget.Button[@content-desc='" + value + "']"))).click()
            # try:
            #     actions = TouchAction(self.driver)
            #     # actions.scroll_from_element(element, 10, 100)
            #     actions.scroll(10, 100)
            #     actions.perform()
            # except:
            #     print("Scroll down didn't work")
        elif field == "Notes":
            note = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, fill_data)))
            # note = self.driver.find_element((MobileBy.XPATH,fill_data))
            print(fill_data)
            note.click()
            note.send_keys(value)
            self.wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, "//android.view.View[@content-desc='New Touchbase']"))).click()
        elif field == "Contact Method":
            element = self.wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, "//android.view.View[@content-desc='" + value + "']"))).click()

    def Create_touchbase(self):
        self.wait.until(
            EC.presence_of_element_located(
                (MobileBy.XPATH, "(//android.view.View)[1]"))).click()
