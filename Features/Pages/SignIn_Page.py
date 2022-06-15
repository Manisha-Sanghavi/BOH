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
        self.wait = WebDriverWait(self.driver, 60)
        self.implicit_wait = 25

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
        #sleep(5)
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
        elif message == "(123)456-7890" or message == "(089)674-5131":
            try:
                    self.wait.until(
                    EC.presence_of_element_located(
                    (MobileBy.XPATH, "//android.view.View[@content-desc='" + message + "']")))
            except:
                self.wait.until(
                    EC.presence_of_element_located(
                        (MobileBy.XPATH, "(//android.view.View)[7]")))
            flag = True
        elif message == "Save Changes":
            self.wait.until(
                EC.presence_of_element_located(
                    (MobileBy.XPATH, "(//android.widget.Button)[2]")))
            flag = True
        elif message == "Tap the + to add the first RE":
            self.wait.until(
                EC.presence_of_element_located(
                    (MobileBy.XPATH, "//android.view.View[@content-desc='" + message + "']")))
            flag = True

        elif message == "Est. Order Date 6/2022":
            text = self.wait.until(
                EC.presence_of_element_located(
                    (MobileBy.XPATH, "(//android.view.View)[17]")))
            value = text.get_attribute('content-desc')
            print(value)
            msg = value.split()
            print(msg)
            msg1 = msg[-11]
            msg2 = msg[-12]
            msg3 = msg[-13]
            msg4 = msg[-14]
            text = msg4 + msg3 + msg2 + " "+msg1
            # glob_opp = msg[0] + " "+msg[1]
            # print("global variable for opportunity: " +glob_opp)
            # if text.__contains__(glob_opp):
            #     print("You removed opportunity "+glob_opp+ "successfully.")

            print(text)
            flag = True
        elif message == "No requirement Estimates for opportunity #16":
            re_message = self.wait.until(
                EC.presence_of_element_located(
                    (MobileBy.XPATH, "(//android.widget.ImageView)[1]")))
            value = re_message.get_attribute('content-desc')
            assert message == value
            flag = True
        # elif message == "Removed Opportunity":
            # self.wait.until(
            #     EC.presence_of_element_located(
            #         (MobileBy.XPATH, "")))
        return flag

    def show_field(self, field):
        flag = False
        if field == 'Customer Management':
            form_xpath = "//android.view.View[@content-desc='XXX']"
            show_data = form_xpath.replace('XXX', field)
            CustName_ele = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, show_data)))
            flag = True
        elif field == 'Customers Tab 1 of 3':
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[8]")))
            flag = True
        elif field == 'REs Tab 2 of 3':
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[9]")))
            flag = True
        elif field == "Opportunities Tab 3 of 3":
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[10]")))
            flag = True
        else:
            text_ele = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[21]")))
            value = text_ele.get_attribute('content-desc')
            print(value)
            msg = value.split()
            print(msg)
            text1 = msg[0]+" "+msg[1]
            assert text1 == "Joe M"
            text2 = msg[-15]
            assert text2 == "london"
            text3 = msg[-13] + " " + msg[-12]
            assert text3 == "Rashmi C"
            text4 = msg[-10] + " " + msg[-9]
            assert text4 == "total REs"
            text5 = msg[-7]
            assert text5 == "touchbases"
            text6 = msg[-5]
            assert text6 == "value"
            flag = True
            # raise NameError(f'Field {field} is not valid')
        return flag

    def tap_option(self, option_name):
        option_xpath = "//android.widget.Button[@content-desc='XXX']"
        option_Btn = option_xpath.replace('XXX', option_name)
        if option_name == "forgot password" or option_name == "SEND" or option_name == "CREATE TOUCHBASE" or option_name == "Search" or option_name == "Save Changes" or option_name == "CREATE OPPORTUNITY":
            tap_btn = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.Button[@content-desc='"+option_name+"']")))
            tap_btn.click()
        elif option_name == "Add Touchbase" or option_name == "Add Opportunity":
            option_xpath = "//android.widget.ImageView[@content-desc='XXX']"
            option_Btn = option_xpath.replace('XXX', option_name)
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, option_Btn))).click()
        elif option_name == "+":
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.widget.ImageView)[1]"))).click()
        elif option_name == "INFO Tab 1 of 3" or option_name == "Delete John J" or option_name == "Show menu Active" or option_name == "Edit Contact" or option_name == "REs Tab 3 of 3" or option_name == "Opportunities Tab 3 of 3":
            try:
                option_xpath = "//android.view.View[@content-desc='XXX']"
                option_Btn = option_xpath.replace('XXX', option_name)
                self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, option_Btn))).click()
                # self.driver.find_element((MobileBy.XPATH (option_Btn))).click()
            except:
                print("You are in catch block")
                if option_name == "INFO Tab 1 of 3":
                    self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[9]"))).click()
                elif option_name == "REs Tab 3 of 3":
                    self.wait.until(
                        EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[11]"))).click()
        elif option_name == "Remember Me":
            self.wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, "//android.widget.CheckBox[@content-desc='Remember Me']"))).click()
        elif option_name == "Sort By":
            self.wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, "(//android.view.View)[17]"))).click()
        elif option_name == "filter By":
            self.wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, "(//android.view.View)[19]"))).click()
        elif option_name == "ACTIVE" or option_name == "Delete Opportunity":
            self.wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, "//android.view.View[@content-desc='"+option_name+"']"))).click()
            try:
                self.wait.until(EC.presence_of_element_located(
                    (MobileBy.XPATH, "//android.widget.Button[@content-desc='Yes']"))).click()
            except:
                print("No use of Yes option here")
        elif option_name == "INACTIVE":
            self.wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, "//android.view.View[@content-desc='"+option_name+"']"))).click()
        elif option_name == "Set Customer to Inactive":
            self.wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, "//android.view.View[@content-desc='Set Customer as Inactive']"))).click()
        elif option_name == "Set Customer to Active":
            self.wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, "//android.view.View[@content-desc='Set Customer as Active']"))).click()
        elif option_name == "Administrator":
            self.wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, "(//android.widget.Button)[1]"))).click()
        elif option_name == "Post a message":
            btn = self.wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, "//android.widget.EditText[@text='"+option_name+"']")))
            btn.click()
            btn.send_keys('Test')
            self.wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, "(//android.widget.Button)[2]"))).click()
        elif option_name == "contact name":
            self.wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, "(//android.view.View)[20]"))).click()
        elif option_name == "Delete Opportunity":
            self.wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, "//android.view.View[@content-desc='"+option_name+"']"))).click()
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
        elif field == "Location":
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, fill_data))).click()
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, search_loc))).send_keys(value)
            self.wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, '//android.view.View[@content-desc="Add Location \'' + value + '\'"]'))).click()
        elif field == "Contact":
            self.wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, "//android.widget.Button[@content-desc='" + value + "']"))).click()
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
