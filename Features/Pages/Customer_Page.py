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

    def cust_list(self):
        name = self.wait.until(EC.presence_of_all_elements_located(((MobileBy.XPATH,"(//android.view.View)[21]"))))
        read_txt = name.text
        print(read_txt)
        value = self.list_xpath.split()
        # value = read_txt.split()
        print(value)
        retrieve_text = print(value[13:])