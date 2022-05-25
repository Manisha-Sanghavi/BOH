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


class Customer_Page(Basepage):
    def __init__(self, context):
        Basepage.__init__(self, context.driver)
        self.context = context
        self.form_xpath = "//android.view.View[@content-desc='XXX']"
        self.option_xpath = "//android.widget.Button[@content-desc='XXX']"
        self.list_xpath = "//android.view.View[@content-desc='Joe M london Validate Rashmi C 4 total REs 3 touchbases $51.4K value contacted 4 days ago']"

    def select_option(self, select_option):
        select_xpath = self.option_xpath.replace('XXX', select_option)
        select = self.wait.until(EC.presence_of_element_located(
            (MobileBy.XPATH, select_xpath)))
        select.click()

    def select_arrow(self):
        self.wait.until(EC.presence_of_element_located(
            (MobileBy.XPATH, "(//android.view.View)[18]"))).click()

    def cust_list_asc(self):
        # name = self.wait.until(EC.presence_of_all_elements_located(((MobileBy.XPATH,"//android.view.View[@content-desc='Joe M london Validate Rashmi C 4 total REs 3 touchbases $51.4K value contacted 4 days ago']"))))
        cust_one = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH,"(//android.view.View)[21]")))
        read_txt = cust_one.get_attribute('content-desc')
        print(read_txt)
        # value = self.list_xpath.split()
        value = read_txt.split()
        txt1 = value[-6]
        print("value of text1",txt1)
        cust_two = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[23]")))
        read_txt = cust_two.get_attribute('content-desc')
        print(read_txt)
        # value = self.list_xpath.split()
        value = read_txt.split()
        txt2 = value[-6]
        print("value of text2",txt2)
        assert txt1 > txt2

    def cust_list_dsc(self):
        cust1 = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH,"(//android.view.View)[21]")))
        read_txt = cust1.get_attribute('content-desc')
        print(read_txt)
        value = read_txt.split()
        txt1 = value[-6]
        # txt1 = value[-4:]
        print("text1:",txt1)
        cust2 = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[23]")))
        read_txt = cust2.get_attribute('content-desc')
        print(read_txt)
        value = read_txt.split()
        # txt2 = value[-3:]
        txt2 = value[-6]
        print("text2:",txt2)
        # size1 = len(txt1)
        # size2 = len(txt2)
        # print("length of text1",size1)
        # print("length of text1",size2)
        assert txt1 >= txt2

    def status_verification(self,index):
        status = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)["+index+"]")))
        status_txt = status.get_attribute('content-desc')
        print("status_text: ", status_txt)
        assert status_txt == "ACTIVE"

    def select_customer(self,index):
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)["+index+"]"))).click()

    def search_customer(self, cust):
        search_cust = self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.EditText[@text='Search Customers']")))
        search_cust.send_keys(cust)
        click_on_cust = self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[16]")))
        click_on_cust.click()

    def verify_message_on_page(self, message):
            user = self.wait.until(
                EC.presence_of_element_located(
                    (MobileBy.XPATH, "(//android.view.View)[7]")))
            txt = user.get_attribute('content-desc')
            print('Value of Text:'+txt)
            value = txt.split()
            print(value)
            msg1 = value[0]
            msg2 = value[1]
            msg = msg1+" " + msg2
            print(msg)
            assert message == msg

    def show_field_for_cust(self, field):
        flag = False
        if field == 'INFO Tab 1 of 3':
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[9]")))
            flag = True
        elif field == 'ACTIVITY Tab 2 of 3':
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[10]")))
            flag = True
        elif field == 'REs Tab 3 of 3':
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[11]")))
            flag = True
        elif field == 'In-Person':
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.widget.ImageView)[1]")))
            flag = True
        else:
            form_xpath = "//android.view.View[@content-desc='XXX']"
            show_data = form_xpath.replace('XXX', field)
            CustName_ele = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, show_data)))
            flag = True
        return flag

    def show_field_on_homepage(self, field):
        flag = False
        flag = True
        if field == "Add Touchbase":
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.widget.ImageView)[3]")))
            flag = True
        elif field == "Add Opportunity":
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.widget.ImageView)[2]")))
            flag = True
        elif field == "Add RE":
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.widget.ImageView)[1]")))
            flag = True
        # else:
        #     form_xpath = "//android.widget.ImageView[@content-desc='XXX']"
        #     show_data = form_xpath.replace('XXX', field)
        #     self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, show_data)))
        return flag

    def pop_up(self, pop_up):
        message = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(// android.view.View)[7]")))
        popup_read = message.get_attribute('Content-desc')
        print(popup_read)
        assert popup_read == pop_up

    def status_member(self, status):
        state = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[8]")))
        value = state.get_attribute('Content-desc')
        print(value)
        # status_value = value[0]
        assert value == status

    def show_field_info(self, field):
        value = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "//android.view.View[@content-desc='"+field+"']")))
        txt = value.get_attribute('content-desc')
        print(txt)
        msg = txt.split()
        msg1 = msg[0]
        msg2 = msg[1]
        msg4 = msg[2] + msg[3]
        if field == "Locations":
            print(msg1)
            return msg1
        elif field == "Contacts":
            msg3 = msg1 + msg2
            print(msg3)
            return msg3
        elif field == "no contacts":
            print(msg4)
            return msg4
        return txt

    def Verify_act_note(self, note):
        value = self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[20]")))
        text = value.get_attribute('content-desc')
        print(text)
        msg = text.split()
        text1 = msg[3]
        assert text1 == note

    def noteField_activity(self, note):
        actions = TouchAction(self.driver)
        element = self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "//android.view.View[@content-desc='New Touchbase']")))
        actions.scroll_from_element(element, 10, 100)
        actions.scroll(10, 100)
        actions.perform()

    def enter_contact(self, contact):
        value = self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "(//android.widget.EditText)[5]")))
        value.click()
        value.clear()
        value.send_keys(contact)
        # This is for tapping outside which help to see save changes button
        self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[7]"))).click()

    def tap_option_index(self, option_name):
        if option_name == "Back":
            index = '1'
            self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "(//android.widget.Button)["+index+"]"))).click()
        elif option_name == "Push":
            index = '1'
            self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "(//android.widget.Switch)["+index+"]"))).click()








