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

    def re_tab(self):
        self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[9]"))).click()

    def click_sortby(self):
        self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[17]"))).click()

    def click_filterby(self):
        self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[19]"))).click()


    def verify_sortby_filterby(self, field):
        a = self.driver.find_element(MobileBy.XPATH, "//android.widget.Button[@content-desc='"+field+"']")
        s = a.get_attribute('content-desc')
        print(s)
        return  s

    # def verify_filterby(self, field):
    #     a = self.driver.find_element(MobileBy.XPATH, "//android.widget.Button[@content-desc='" + field + "']")
    #     s = a.get_attribute('content-desc')
    #     # print(s)
    #     return s

    def tap_symbol(self):
        self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "(//android.widget.Button)[3]"))).click()

    def add_re(self):
        self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.ImageView[@content-desc='Add RE']"))).click()

    def order_date(self):
        self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "//android.view.View[@content-desc='MM/DD/YYYY']"))).click()
        self.driver.find_element(MobileBy.XPATH, '//android.view.View[@content-desc="31, Tuesday, May 31, 2022"]').click()
        self.driver.find_element(MobileBy.XPATH, '//android.widget.Button[@content-desc="OK"]').click()

    def cust_info(self):
        self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.Button[@content-desc='Direct']"))).click()
        self.driver.find_element(MobileBy.XPATH,
                                 '(//android.view.View)[18]').click()
        self.driver.find_element(MobileBy.XPATH, '//android.widget.Button[@content-desc="East"]').click()
        self.driver.find_element(MobileBy.XPATH, '(//android.view.View)[19]').click()
        self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "//android.view.View[@content-desc='Joe M']"))).click()
        self.driver.find_element(MobileBy.XPATH, '(//android.view.View)[20]')
        self.driver.find_element(MobileBy.XPATH, '(//android.view.View[@content-desc="Amsterdam"])[1]')

    def primary_contact(self, field,value):
        self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "(// android.widget.Button)[5]"))).click()
        if field == "Rank or Title (optional)":
            rank = self.driver.find_element(MobileBy.XPATH, '// android.widget.EditText[ @ text = "'+field+'"]').click()
            rank.send_keys(value)
        if field == "Contact First Name":
            first_name = self.driver.find_element(MobileBy.XPATH, '// android.widget.EditText[ @ text = "'+field+'"]').click()
            first_name.send_keys(value)
        if field == "Contact Last Name":
            last_name = self.driver.find_element(MobileBy.XPATH, '// android.widget.EditText[ @ text = "'+field+'"]').click()
            last_name.send_keys(value)
        if field == "Contact Email":
            email = self.driver.find_element(MobileBy.XPATH, '// android.widget.EditText[ @ text = "'+field+'"]').click()
            email.send_keys(value)
        if field == "Contact Phone":
            phone = self.driver.find_element(MobileBy.XPATH, '// android.widget.EditText[ @ text = "'+field+'"]').click()
            phone.send_keys(value)

    def select_metrics(self):
        sq_ft = self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.EditText[@text='Pre-RE Footprint (sq ft)']"))).click()
        sq_ft.send_keys("70")
        self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.Button[@content-desc='TAN']"))).click()

    def create_estimation(self):
        self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.Button[@content-desc='CREATE REQUIREMENTS ESTIMATE']"))).click()

    def tap_search(self):
        self.wait.until(
            EC.presence_of_element_located(
                (MobileBy.XPATH, "//android.widget.Button[@content-desc='Search']"))).click()

    def search_re(self):
        re_num = self.wait.until(
            EC.presence_of_element_located(
                (MobileBy.XPATH, "//android.widget.EditText[@text='Search REs']"))).click()
        re_num.send_keys("772")


















