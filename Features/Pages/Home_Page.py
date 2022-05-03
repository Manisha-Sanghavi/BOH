import json
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import time

from Features.Pages.BasePage import Basepage


class SignIn(Basepage):
    def __init__(self,context):
        Basepage.__init__(self,context.driver)
        self.context=context


    data = json.load(open('Features/Resources/config.json'))




    def enter_Username(self,username):
        user = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "//*[contains(@text,'E-Mail Address')]")))
        user.click()
        user.send_keys(username)

    def enter_Password(self,password):
          password_field = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "//*[contains(@text,'Password')]")))
          password_field.click()
          password_field.send_keys(password)

    def clickOn_Login(self):
          sleep(20)
          login = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "//*[contains(@text,'LOGIN')]")))
          login.click()
