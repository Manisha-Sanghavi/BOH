
import json
from time import sleep

from appium import webdriver
from allure_commons.types import AttachmentType
from allure_commons._allure import attach
from Features.Pages.BasePage import Basepage
#from Features.Utils.APIUtility import APIUtility
from Features.Pages.Home_Page import Home_page
from Features.Pages.bohapk_page import bohapk_page

# data = json.load(open("Features/Resources/config.json"))

# defbefore_all(context):

def before_feature(context, feature):
    print(feature)
    tags = str(feature.tags)




def before_scenario(context, scenario):
    tag=str(scenario.tags)
    print(tag)
    if context.config.userdata["executionMode"] == "Browserstack":
        context.driver = webdriver.Remote(
            command_executor='https://' + context.config.userdata["userName"] + ':' + context.config.userdata[
                "accessKey"] + '@hub-cloud.browserstack.com/wd/hub',
            desired_capabilities={
                # "platformName": "Android",
                "build": context.config.userdata["browserstack_build"],
                "device": context.config.userdata["browserstack_device"],
                "os_version": context.config.userdata["device_os_version"],
                "app": context.config.userdata["browserstack_appUrl"],
                #"nativeWebTap": True
                # "autoDismissAlerts": True
            }
        )
    elif context.config.userdata["executionMode"] == "Emulator":
        context.driver = webdriver.Remote(
            command_executor="http://localhost:4723/wd/hub",
            desired_capabilities={
                "platformName": context.config.userdata["platformName"],
                "deviceName": context.config.userdata["Emulator_deviceName"],
                "app": context.config.userdata["Emulator_app"],
                "appPackage": context.config.userdata["appPackage"],
                "appActivity": context.config.userdata["appActivity"]

            }
        )
    elif context.config.userdata["executionMode"] == "RealDevice":
        context.driver = webdriver.Remote(
            command_executor="http://localhost:4723/wd/hub",
            desired_capabilities={
                "platformName": context.config.userdata["platformName"],
                "build": context.config.userdata["realdevice_build"],
                "deviceName": context.config.userdata["realdevice_deviceName"],
                "os_version": context.config.userdata["realdevice_os_version"],
                "appPackage": context.config.userdata["appPackage"],
                "appActivity": context.config.userdata["appActivity"],
                "noReset": context.config.userdata["realdevice_noReset"],
                "newCommandTimeout": context.config.userdata["realdevice_newCommandTimeout"],
                "automationName": context.config.userdata["automationName"]
            })
    else:
        print("...")
    context.driver.switch_to.context('NATIVE_APP')
    baseobject = Basepage(context.driver)
    context.Homepage = Home_page(baseobject)
    context.boh = bohapk_page(baseobject)
    context.stepid = 1

def after_step(context, step):
    attach(context.driver.get_screenshot_as_png(), name=str(context.stepid), attachment_type=AttachmentType.PNG)
    context.stepid = context.stepid + 1

def after_scenario(context, scenario):
    # print("After Scenario",scenario)
    context.driver.reset()
    context.driver.quit()




