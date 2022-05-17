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
from Features.Pages.bohapk_page import bohapk_page

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

    def verify_dropdownlist(self):
        sort_options = self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[17]")))
        select = Select(sort_options)
        option_list = select.options

        for ele in option_list:
            print(ele.text)