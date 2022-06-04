import json
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import time

from Features.Pages.BasePage import Basepage


class Opportunity_Page(Basepage):
    def __init__(self, context):
        Basepage.__init__(self, context.driver)
        self.context = context
        # self.x = self.search_opp()

    def show_opp_field(self, field, value):
        form_xpath = "//android.view.View[@content-desc='XXX']"
        show_data = form_xpath.replace('XXX', field)
        flag = False
        if field == "Affiliation":
            ele_1 = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[10]")))
            ele_1.click()
            self.wait.until(
                EC.presence_of_element_located(
                    (MobileBy.XPATH, "//android.widget.Button[@content-desc='" + value + "']"))).click()
            flag = True
        elif field == "Customer":
            ele_1 = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[11]")))
            ele_1.click()
            self.wait.until(
                EC.presence_of_element_located(
                    (MobileBy.XPATH, "//android.view.View[@content-desc='" + value + "']"))).click()
            flag = True
        elif field == "Location":
            ele_1 = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[12]")))
            ele_1.click()
            self.wait.until(
                EC.presence_of_element_located(
                    (MobileBy.XPATH, "//android.view.View[@content-desc='" + value + "']"))).click()
            flag = True
        elif field == "BOH Role":
            ele_1 = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[13]")))
            ele_1.click()
            self.wait.until(
                EC.presence_of_element_located(
                    (MobileBy.XPATH, "//android.widget.Button[@content-desc='" + value + "']"))).click()
            # This is for scrolling element
            # source = self.driver.find_element(MobileBy.XPATH, "//android.widget.Button[@content-desc='Direct']")
            # target = self.driver.find_element(MobileBy.XPATH, "//android.widget.Button[@content-desc='New']")
            # This is for scrolling
            size = self.driver.get_window_size()
            startX = int(size["width"] / 2)
            startY = int(size["height"] / 2)
            endY = int(size["height"] / 4)
            print("startx" + str(startX) + " startY" + str(startY) + " EndY" + str(endY))
            self.driver.swipe(startX, startY, startX, endY)
            sleep(2)
            flag = True
        elif field == "Win Probability":
            ele_1 = self.wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, "//android.widget.Button[@content-desc='" + value + "']")))
            ele_1.click()
            flag = True
            size = self.driver.get_window_size()
            startX = int(size["width"] / 2)
            startY = int(size["height"] / 2)
            endY = int(size["height"] / 4)
            print("startx" + str(startX) + " startY" + str(startY) + " EndY" + str(endY))
            self.driver.swipe(startX, startY, startX, endY)
            sleep(2)
        elif field == "Value Breakdown":
            ele_1 = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.widget.EditText)[1]")))
            ele_1.click()
            ele_1.send_keys(value)

            ele_2 = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.widget.EditText)[2]")))
            ele_2.click()
            ele_2.send_keys("1000")

            self.wait.until(
                EC.presence_of_element_located(
                    (MobileBy.XPATH, "//android.view.View[@content-desc='New Opportunity']"))).click()
            flag = True
        return flag

    def choose_opportunity(self):
        self.wait.until(
            EC.presence_of_element_located(
                (MobileBy.XPATH, "(//android.view.View)[17]"))).click()

    def display_details(self, field):
        opp_detail = self.wait.until(
            EC.presence_of_element_located(
                (MobileBy.XPATH, "(//android.view.View)[17]")))
        value = opp_detail.get_attribute('content-desc')
        print(value)
        txt = value.split()
        print(txt)
        # flag = False
        if field == "Opportunity #17":
            txt1 = txt[0]
            print(txt1)
            assert field == txt1
        elif field == "Joe M":
            txt2 = txt[2] + " " + txt[3]
            print(txt2)
            assert field == txt2
        elif field == "Joe M":
            txt3 = txt[4]
            print(txt3)
            assert field == txt3
        elif field == "Joe M":
            txt4 = txt[5] + " " + txt[6] + " " + txt[7]
            print(txt4)
            assert field == txt4
        elif field == "Joe M":
            txt5 = txt[0] + " " + txt[1]
            print(txt5)
            assert field == txt5
        elif field == "Joe M":
            txt6 = txt[8]
            print(txt6)
            assert field == txt6
        elif field == "Joe M":
            txt7 = txt[10]
            print(txt7)
            assert field == txt7
        elif field == "Joe M":
            txt8 = txt[12]
            print(txt8)
            assert field == txt8
        elif field == "Joe M":
            txt9 = txt[14]
            print(txt9)
            assert field == txt9

    def verifying_page_field(self, field):
        a = self.wait.until(
            EC.presence_of_element_located(
                (MobileBy.XPATH, "//android.widget.Button[@content-desc='" + field + "']")))
        s = a.get_attribute('content-desc')
        print(s)
        return s

    def verify_list(self):
        list = self.driver.find_elements(MobileBy.XPATH, '(//android.view.View)[18]//following::android.view.View')
        count = len(list)
        print(count)
        if count >= 1:
            return list
        assert list > count

    def choose_option(self, option):
        if option == "opportunity #16":
            index = '19'
            self.wait.until(
                EC.presence_of_element_located(
                    (MobileBy.XPATH, "(//android.view.View)['" + index + "']"))).click()

    def scroll_to(self):
        size = self.driver.get_window_size()
        startX = int(size["width"] / 2)
        startY = int(size["height"] / 2)
        endY = int(size["height"] / 4)
        print("startx" + str(startX) + " startY" + str(startY) + " EndY" + str(endY))
        self.driver.swipe(startX, startY, startX, endY)
        sleep(2)

    def option_for_validation(self, validate):
        validation_xpath = "//android.widget.Button[@content-desc='XXX']"
        use_xpath = validation_xpath.replace('XXX', validate)
        self.wait.until(
            EC.presence_of_element_located(
                (MobileBy.XPATH, use_xpath))).click()

    def page_for_validation(self, Message):
        validation_xpath = "//android.widget.Button[@content-desc='XXX']"
        use_xpath = validation_xpath.replace('XXX', Message)
        self.wait.until(
            EC.presence_of_element_located(
                (MobileBy.XPATH, "use_xpath"))).click()

    def search_opp(self):
        text_ele = self.wait.until(
            EC.presence_of_element_located(
                (MobileBy.XPATH, "(//android.view.View)[17]")))
        value = text_ele.get_attribute('content-desc')
        print(value)
        msg = value.split()
        print(msg)
        text = msg[0] + " " + msg[1]
        # print("global variable for opportunity: " + text)
        # if value.__contains__(text):
        #     print("You removed opportunity " + text + " successfully.")
        # print(text)
        return text

    def new_created_oppo_text(self):
        text_ele = self.wait.until(
            EC.presence_of_element_located(
                (MobileBy.XPATH, "(//android.view.View)[7]")))
        value = text_ele.get_attribute('content-desc')
        print(value)
        # msg = value.split()
        # print(msg)
        # text = msg[0] + " " + msg[1]
        # print("new Opportunity text: "+text)
        if value.__contains__('Opportunity'):
            print("You are removing newly created " + value + " successfully.")
        return value
