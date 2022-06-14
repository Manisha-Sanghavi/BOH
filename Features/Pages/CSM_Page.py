import json
from datetime import datetime
import datetime

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


class CSM_Page(Basepage):
    def __init__(self, context):
        Basepage.__init__(self, context.driver)
        self.context = context

    def verify_Message_CSM(self, message):
        if message == "Delete Requirement Estimate":
            size = self.driver.get_window_size()
            startX = int(size["width"] / 2)
            startY = int(size["height"] / 2) * 2
            endY = int(size["height"] / 4) * 2
            print("startx" + str(startX) + " startY" + str(startY) + " EndY" + str(endY))
            self.driver.swipe(startX, startY, startX, endY)
            sleep(2)
            element = self.wait.until(
                EC.presence_of_element_located(
                    (MobileBy.XPATH, "(//android.view.View)[11]//following::android.view.View")))
            text = element.get_attribute('content-desc')
            print(text)
            print("Checking Delete option is not present: " + message not in text)
        elif message == "Change RE State":
            element = self.wait.until(
                EC.presence_of_element_located(
                    (MobileBy.XPATH, "//android.view.View[@content-desc='Review and Validate']//following::android.view.View")))
            text = element.get_attribute('content-desc')
            print(message not in text)
        else:
            element = self.wait.until(
                EC.presence_of_element_located(
                    (MobileBy.XPATH, "(//android.view.View)[9]//following::android.view.View")))
            text = element.get_attribute('content-desc')
            print(text)
            print("Checking Delete option is not present: " + message not in text)
        return message not in text

    def verify_RE_Page_message(self, message):
        size = self.driver.get_window_size()
        startX = int(size["width"] / 2)
        startY = int(size["height"] / 2)*2
        endY = int(size["height"] / 4)*2
        print("startx" + str(startX) + " startY" + str(startY) + " EndY" + str(endY))
        self.driver.swipe(startX, startY, startX, endY)
        sleep(2)
        size = self.driver.get_window_size()
        startX = int(size["width"] / 2)
        startY = int(size["height"] / 2)*2
        endY = int(size["height"] / 4)*2
        print("startx" + str(startX) + " startY" + str(startY) + " EndY" + str(endY))
        self.driver.swipe(startX, startY, startX, endY)
        element = self.wait.until(
        EC.presence_of_element_located(
            (MobileBy.XPATH, '//android.view.View[@content-desc="' + message + '"]')))
        text = element.get_attribute('content-desc')
        assert message == "Delete Requirements Estimate"

