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
            EC.presence_of_element_located((MobileBy.XPATH, "(//android.widget.Button)[1]/following-sibling::android.view.View[3]"))).click()

    def get_re_num(self, re_string, num):
        if num == "Yes":
            a = re_string[4:7]
            return a
        if num == "No":
            a = re_string[0:2]
            return a

    def click_sortby(self):
        self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[17]"))).click()

    def click_filterby(self):
        self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[19]"))).click()

    def tap_symbol(self):
        self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "(//android.widget.Button)[3]"))).click()

    def add_re(self):
        self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.ImageView[@content-desc='Add RE']"))).click()

    def order_date(self, date):
        self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "//android.view.View[@content-desc='MM/DD/YYYY']"))).click()
        self.driver.find_element(MobileBy.XPATH, '//android.view.View[@content-desc="31, Tuesday, May 31, 2022"]').click()
        self.driver.find_element(MobileBy.XPATH, '//android.widget.Button[@content-desc="OK"]').click()

    def cust_info(self, field, value):
        if field == "RE Region":
            self.driver.find_element(MobileBy.XPATH,'(//android.view.View[@content-desc="Customer Info"]/following-sibling::android.view.View)[2]').click()
            self.wait.until(
                EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.Button[@content-desc="'+value+'"]'))).click()
        if field == "Customer Name":
            self.driver.find_element(MobileBy.XPATH, '(//android.view.View[@content-desc="Customer Info"]/following-sibling::android.view.View)[3]').click()
            self.wait.until(
                EC.presence_of_element_located((MobileBy.XPATH, '//android.view.View[@content-desc="'+value+'"]'))).click()
        if field == "Customer Location":
            element_to_tap = self.driver.find_element(MobileBy.XPATH, '(//android.view.View[@content-desc="Customer Info"]/following-sibling::android.view.View)[3]')
            element_to_drag_to = self.driver.find_element(MobileBy.XPATH, '(//android.view.View[@content-desc="Opportunity"])[1]')
            self.driver.scroll(
                element_to_tap, element_to_drag_to)
            self.wait.until(
                EC.presence_of_element_located((MobileBy.XPATH, '(//android.view.View[@content-desc="Customer Info"]/following-sibling::android.view.View)[4]'))).click()
            self.wait.until(
                EC.presence_of_element_located((MobileBy.XPATH, '// android.widget.EditText'))).send_keys(value)
            self.wait.until(
                EC.presence_of_element_located((MobileBy.XPATH, '(//android.view.View[@content-desc="'+value+'"])'))).click()

    def scroll_down(self):
        element_to_tap = self.driver.find_element(MobileBy.XPATH,
                                                  '//android.view.View[@content-desc="Select Lift Capabilities"]')
        element_to_drag_to = self.driver.find_element(MobileBy.XPATH,
                                                      '//android.view.View[@content-desc="Metrics"]')
        self.driver.scroll(
            element_to_tap, element_to_drag_to)

    def tap_new(self):
        self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.Button[@content-desc="New"]'))).click()

    def primary_contact(self, field,value):
        a = self.driver.find_element(MobileBy.XPATH, '//android.widget.EditText[@text="'+field+'"]').click()
        ActionChains(self.driver).send_keys(value).perform()

    def select_footprint(self, number):
        self.driver.hide_keyboard()
        self.wait.until(
                EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.EditText[@text='Pre-RE Footprint (sq ft)']"))).click()
        ActionChains(self.driver).send_keys(number).perform()

    def select_lift_capability(self):
        self.driver.hide_keyboard()
        user_action = TouchAction(self.driver)
        # ele = self.driver.find_element(MobileBy.XPATH, '//android.widget.CheckBox[@content-desc="25k Forklift"]')
        #user_action.tap(ele, 743, 1320).perform()
        #user_action.tap(x=743, y=1396).perform()
        self.scroll_down()
        user_action.tap(x=739, y=1562).perform()      #individual locators for checkbox not avalable

    def select_color(self, color):
        self.wait.until(
                EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.Button[@content-desc='"+color+"']"))).click()
        self.scroll_down()

    def verify_re(self):
        ele = self.wait.until(
            EC.presence_of_element_located(
                (MobileBy.XPATH, "//android.widget.ScrollView/android.view.View[1]")))
        re_string = ele.get_attribute('content-desc')
        a = self.get_re_num(re_string, "Yes")
        return a

    def create_estimation(self):
        self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.Button[@content-desc='CREATE REQUIREMENTS ESTIMATE']"))).click()

    def verify_re_page_displayed(self):
        time.sleep(3)
        ele = self.wait.until(
            EC.presence_of_element_located(
                (MobileBy.XPATH, "//android.widget.ScrollView/android.view.View[1]")))
        re_string = ele.get_attribute('content-desc')
        a = self.get_re_num(re_string, "No")
        return a

    def tap_search(self):
        self.wait.until(
            EC.presence_of_element_located(
                (MobileBy.XPATH, "//android.widget.Button[@content-desc='Search']"))).click()

    def search_re(self, number):
        re_num = self.wait.until(
            EC.presence_of_element_located(
                (MobileBy.XPATH, "//android.widget.EditText[@text='Search REs']")))
        re_num.send_keys(number)

    def select_re(self, re_num):
        self.wait.until(
            EC.presence_of_element_located(
                (MobileBy.XPATH, f"//android.view.View[@content-desc='Camp Humphreys, Korea - RE {re_num}']"))).click()

    def tap_arrow(self):
        self.wait.until(
            EC.presence_of_element_located(
                (MobileBy.XPATH, "(//android.view.View)[18]"))).click()

    def verify_ascend_descend(self, number):
        ele = self.wait.until(
            EC.presence_of_element_located(
                (MobileBy.XPATH, f"(//android.view.View)[{number}]")))
        re_one = ele.get_attribute('content-desc')
        a = self.get_re_num(re_one, "Yes")
        return a

    def verify_fields(self, field):
        a = self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.ImageView[@content-desc='"+field+"']")))
        s = a.get_attribute('content-desc')
        print(s)
        return s

    def select_re_from_list(self, re_num):
        self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "(// android.view.View)[21]"))).click()

    def edit_subtitle(self, text):
        user_action = TouchAction(self.driver)
        user_action.tap(x=100,y=385).perform()
        re_text = self.wait.until(
            EC.presence_of_element_located((MobileBy.CLASS_NAME, "android.widget.EditText")))
        re_text.send_keys("Requirements changed")
        self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "(//android.widget.Button)[3]"))).click()

    def verify_subtitle(self):
        ele = self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[15]")))
        ele_string = ele.get_attribute('content-desc')
        a = ele_string.split()
        return a[2], a[3]

    def select_re_status(self, re_status):
        self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.Button[@content-desc='"+re_status+"']"))).click()

    def verify_re_status(self, re_status):
        self.wait.until(
            EC.presence_of_element_located(
                (MobileBy.XPATH, "(// android.view.View)[21]"))).click()
        uc_re = re_status.upper()
        a = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "//android.view.View[@content-desc='"+uc_re+"']")))
        b = a.get_attribute('content-desc')
        return b





























