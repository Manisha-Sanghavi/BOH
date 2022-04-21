from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import  WebDriverWait
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Basepage(object):

    def __init__(self,driver):
        self.driver=driver
        self.wait =WebDriverWait(self.driver,60)
        self.implicit_wait=25

    def scroll(self):
         # size = self.driver.get_window_size()
         # startX = int(size["width"] / 2)
         # startY = int(size["height"] / 2)
         # endY = int(size["height"] / 4)
         # print("startx" + str(startX) + " startY" + str(startY) + " EndY" + str(endY))
         # self.driver.swipe(startX, startY, startX, endY)
         # sleep(2)
         sleep(1)
         self.driver.execute_script('mobile: scroll', {'direction': 'down'})
         sleep(1)

    def multiple_scroll(self,n):
        for i in range (n):
             # size = self.driver.get_window_size()
             # startX = int(size["width"] / 2)
             # startY = int(size["height"] / 2)
             # endY = int(size["height"] / 4)
             # self.driver.swipe(startX, startY, startX, endY)
             # print("Scroll " + str(i))
             self.driver.execute_script('mobile: scroll', {'direction': 'down'})
        sleep(2)


    def click_Textview(self,name):
        element  = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//XCUIElementTypeStaticText[contains(@name,"'+name+'")]')))
        element.click()

    def exists_Textview(self,name):
        try:
            ele = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//XCUIElementTypeStaticText[contains(@name, "'+name+'")]')))
            flag = ele.is_displayed()
        except:
            flag = False
        return flag

    def refresh_page(self):
        size = self.driver.get_window_size()
        startX = int(size["width"] / 2)
        startY = int(size["height"] *0.2)
        endY = int(size["height"] * 0.7)

        actions = TouchAction(self.driver)
        actions.press(None,startX,startY)
        actions.wait(500)
        actions.move_to(None,startX,endY)
        actions.release()
        actions.perform()

    def verify_element_clicked(self,id):
        flag = True
        for i in range(2):
            try:
                sleep(2)
                ele = self.driver.find_element_by_accessibility_id(id)
                ele.click()
            except:
                flag = False

    def verify_element_withxpath_clicked(self,path):
        flag = True
        for i in range(1):
            try:
                sleep(2)
                ele = self.driver.find_element_by_xpath(path)
                ele.click()
            except:
                flag = False

    def element_exists(self, xpath):
        flag = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, xpath))).is_displayed()
        return flag

    def click_element(self,xpath,wait_before=0):
        sleep(wait_before)
        try:
            element = self.wait.until(
                EC.element_to_be_clickable((MobileBy.XPATH, xpath)))
            element.click()
        except StaleElementReferenceException as Exception:
            element = self.driver.find_element_by_xpath(xpath)
            element.click()
        except:
            element = self.driver.find_element_by_xpath(xpath)
            element.click()

    def switch_context(self, context_name):
        print("All contexts : ")
        print(self.driver.contexts)
        print("Current context : " + self.driver.context)
        context_name = context_name.lower()
        if context_name == "native_app":
            self.driver.switch_to.context('NATIVE_APP')
            print("Now Current context : " + self.driver.context)
        elif context_name == "webview":
            self.driver.switch_to.context('WEBVIEW_com.finexity.androidtestapp')
            print("Now Current context : " + self.driver.context)
        else:
            print("Invalid context name")

        # webview = self.driver.contexts.last
        # self.driver.switch_to.context('WEBVIEW_com.finexity.androidtestapp')