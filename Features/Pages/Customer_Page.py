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