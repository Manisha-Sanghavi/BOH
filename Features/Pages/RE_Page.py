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

class RE_Page(Basepage):
    def __init__(self, context):
        Basepage.__init__(self, context.driver)
        self.context = context
        self.wait = WebDriverWait(self.driver, 60)
        self.implicit_wait = 25

    def re_tab(self):
        self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "(//android.widget.Button)[1]/following-sibling::android.view.View[3]"))).click()

    def get_re_num(self, re_string):
            a = re_string[4:7]
            return a

    def scroll_down(self):
        size = self.driver.get_window_size()
        startX = int(size["width"] / 2)
        startY = int(size["height"] / 2)
        endY = int(size["height"] / 4)
        #print("startx" + str(startX) + " startY" + str(startY) + " EndY" + str(endY))
        self.driver.swipe(startX, startY, startX, endY)
        sleep(2)

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

    def tap_date(self):
        self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "//android.view.View[@content-desc='MM/DD/YYYY']"))).click()

    def order_date(self, date):
        self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.Button[@content-desc='Switch to input']"))).click()
        self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.EditText"))).send_keys(date)
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
            self.scroll_down()
            self.wait.until(
                EC.presence_of_element_located((MobileBy.XPATH, '(//android.view.View[@content-desc="Customer Info"]/following-sibling::android.view.View)[4]'))).click()
            self.wait.until(
                EC.presence_of_element_located((MobileBy.XPATH, '// android.widget.EditText'))).send_keys(value)
            self.wait.until(
                EC.presence_of_element_located((MobileBy.XPATH, '(//android.view.View[@content-desc="'+value+'"])'))).click()

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
        self.driver.hide_keyboard()

    def select_lift_capability(self):
        self.driver.hide_keyboard()
        user_action = TouchAction(self.driver)
        # # ele = self.driver.find_element(MobileBy.XPATH, '//android.widget.CheckBox[@content-desc="25k Forklift"]')
        # #user_action.tap(ele, 743, 1320).perform()
        # #user_action.tap(x=743, y=1396).perform()
        self.scroll_down()
        user_action.tap(x=739, y=1328).perform()      #individual locators for checkbox not avalable
        user_action.tap(x=739, y=1558).perform()

    def select_color(self, color):
        self.wait.until(
                EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.Button[@content-desc='"+color+"']"))).click()
        self.scroll_down()

    def verify_re(self):
        ele = self.wait.until(
            EC.presence_of_element_located(
                (MobileBy.XPATH, "//android.widget.ScrollView/android.view.View[1]")))
        re_string = ele.get_attribute('content-desc')
        a = self.get_re_num(re_string)
        return a

    def select_colour(self, colour):
        self.wait.until(
            EC.presence_of_element_located(
                (MobileBy.XPATH, "//android.widget.Button[@content-desc='" + colour + "']"))).click()


    def create_estimation(self):
        self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.Button[@content-desc='CREATE REQUIREMENTS ESTIMATE']"))).click()

    def get_test_RE(self):
        global test_re_num
        test_re_num = self.verify_re()
        return test_re_num

    def select_test_RE(self, loc):
        ele = self.wait.until(
            EC.presence_of_element_located(
                (MobileBy.XPATH, "//android.widget.EditText[@text='Search REs']")))
        ele.send_keys(test_re_num)
        re_num = str(test_re_num)
        self.wait.until(
            EC.presence_of_element_located(
                (MobileBy.XPATH, "//android.view.View[@content-desc='"+ loc +" - RE "+ re_num +"']"))).click()

    def verify_page_displayed(self, option):
        time.sleep(3)
        ele = self.wait.until(
            EC.presence_of_element_located(
                (MobileBy.XPATH, "//android.widget.ScrollView/android.view.View[1]")))
        re_string = ele.get_attribute('content-desc')
        a = re_string.split()
        if option == "RE":
            name = a[4] + ' ' + a[5]
            location = a[6]
            return name, location
        if option == "opportunity":
            opp = a[3] + ' ' + a[4]
            return opp

    def tap_search(self):
        # self.wait.until(
        #     EC.presence_of_element_located(
        #         (MobileBy.XPATH, "//android.widget.Button[@content-desc='Back']"))).click()
        self.wait.until(
            EC.presence_of_element_located(
                (MobileBy.XPATH, "//android.widget.Button[@content-desc='Search']"))).click()

    def search_re(self, number):
        re_num = self.wait.until(
            EC.presence_of_element_located(
                (MobileBy.XPATH, "//android.widget.EditText[@text='Search REs']")))
        re_num.send_keys(number)

    def select_re(self):
        time.sleep(2)
        self.wait.until(
            EC.presence_of_element_located(
                (MobileBy.XPATH, '(//android.view.View)[8]'))).click()

    def tap_arrow(self):
        self.wait.until(
            EC.presence_of_element_located(
                (MobileBy.XPATH, "(//android.view.View)[18]"))).click()

    def get_first_re(self):
        ele = self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[21]")))
        re_one = ele.get_attribute('content-desc')
        a = self.get_re_num(re_one)
        return a

    def get_second_re(self):
        ele = self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[23]")))
        re_one = ele.get_attribute('content-desc')
        a = self.get_re_num(re_one)
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
        re_text.send_keys(text)
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

    def tap_info_tab(self):
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[11]"))).click()

    def tap_swap_contact(self):
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.Button[@content-desc='Swap Contact']"))).click()

    def select_contact(self, contact):
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "//android.view.View[@content-desc='"+contact+"']"))).click()
        #self.driver.switch_to.default_content()
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[19]"))).click()

    def verify_swapped_contact(self):
        a = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.view.View)[26]')))
        con_string = a.get_attribute('content-desc')
        b = con_string.split()
        c = b[2] + ' ' + b[3]
        return c

    def swap_back_contact(self, contact):
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.Button[@content-desc='Swap Contact']"))).click()
        self.wait.until(EC.presence_of_element_located(
            (MobileBy.XPATH, '//android.view.View[@content-desc="'+contact+' "]'))).click()
        # self.driver.switch_to.default_content()
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[19]"))).click()

    def select_opportunity(self, num, name):
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.view.View[@content-desc="Opportunity"])[2]'))).click()
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, f"//android.view.View[@content-desc='Opp {num} • "+ name +"']"))).click()


    def fill_details(self, field, value):
        if field == "Opportunity":
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.view.View)[22]'))).click()
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.view.View[@content-desc="'+ value +'"]'))).click()
        if field == "Sales Rep":
            time.sleep(1)
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.view.View)[25]'))).click()
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.view.View[@content-desc="'+ value +'"]'))).click()
        if field == "Direct":
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.view.View)[26]'))).click()
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.view.View[@content-desc="'+ field +'"]'))).click()
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.view.View[@content-desc="'+ value +'"]'))).click()

    def tap_contact(self):
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.Button[@content-desc="Swap Contact"]//parent::android.view.View'))).click()
        time.sleep(1)

    def fill_cust_contact(self, field, value):
        # user_action = TouchAction(self.driver)
        # user_action.tap(x=237, y=1620).perform()
        if field == "First Name":
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.widget.EditText)[2]'))).click()
            self.driver.find_element(MobileBy.XPATH, '(//android.widget.EditText)[2]').clear()
            ActionChains(self.driver).send_keys(value).perform()
            self.driver.hide_keyboard()
        if field == "Last Name":
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.widget.EditText)[3]'))).click()
            self.driver.find_element(MobileBy.XPATH, '(//android.widget.EditText)[3]').clear()
            ActionChains(self.driver).send_keys(value).perform()
            self.driver.hide_keyboard()
        if field == "Contact Email":
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.widget.EditText)[4]'))).click()
            self.driver.find_element(MobileBy.XPATH, '(//android.widget.EditText)[4]').clear()
            ActionChains(self.driver).send_keys(value).perform()
            self.driver.hide_keyboard()
        if field == "Contact Phone":
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.widget.EditText)[5]'))).click()
            self.driver.find_element(MobileBy.XPATH, '(//android.widget.EditText)[5]').clear()
            ActionChains(self.driver).send_keys(value).perform()
            self.driver.hide_keyboard()

    def save_contact(self):
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.Switch'))).click()
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.Button[@content-desc="Save Changes"]'))).click()
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.Button[@content-desc="Back"]'))).click()

    def verify_details(self, field, value):
        if field == "Customer Name":
            a = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.Button[@content-desc="Swap Contact"]//parent::android.view.View')))
            b = a.get_attribute('content-desc')
            c = b.split()
            cust_name = c[2] + ' ' + c[3]
            return cust_name
        if field == "Contact Email":
            a = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.view.View[@content-desc="'+value+'"]')))
            cont_email = a.get_attribute('content-desc')
            return cont_email
        if field == "Contact Phone":
            a = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.view.View[@content-desc="'+value+'"]')))
            cont_phone = a.get_attribute('content-desc')
            return cont_phone

    #def fill_info_details(self):



    def enter_pre_re(self, num):
        a = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText'))).click()
        ActionChains(self.driver).send_keys(num).perform()
        self.driver.hide_keyboard()

    def select_lift_caps(self):
        a = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.CheckBox[@content-desc="5k Forklift"]')))
        b = a.setattr('checked', 'true')

    def save_changes(self):
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.Button[@content-desc="Save Changes"]'))).click()
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.Button[@content-desc="Yes"]'))).click()

    def verify_changes(self):
        a = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.view.View)[22]')))
        opp_string = a.get_attribute('content-desc')
        b = opp_string.split()
        c = b[1] + ' ' + b[2]
        d = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.view.View)[23]')))
        sales_string = d.get_attribute('content-desc')
        e = sales_string.split()
        f = b[2] + ' ' + b[3]
        g = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.view.View)[24]')))
        sales_string = g.get_attribute('content-desc')
        h = sales_string.split()
        i = b[2]
        j = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.view.View)[25]')))
        sales_string = j.get_attribute('content-desc')
        k = sales_string.split()
        l = b[2]
        x = b[3]
        m = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.view.View)[25]')))
        sales_string = m.get_attribute('content-desc')
        n = sales_string.split()
        o = b[2] + ' ' + b[3]
        p = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText')))
        pre_re_value = p.get_attribute('text')
        q = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.CheckBox[@content-desc="5k Forklift"]')))
        sales_string = q.get_attribute('content-desc')
        r = self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.Button[@content-desc="TAN"]')))
        sales_string = r.get_attribute('content-desc')
        return c,f,i,l,x,o,pre_re_value,sales_string

    def tap_add_date(self):
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.Button[@content-desc="Add Another Date"]'))).click()

    def tap_save_changes(self):
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.view.View[@content-desc="SAVE CHANGES"]'))).click()

    def verify_dates(self):
        a = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.widget.Button[@content-desc="10%"]/following-sibling::android.view.View)[3]')))
        b = a.get_attribute('content-desc')
        c = b.split()
        first_date = c[0]
        x = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.widget.Button[@content-desc="10%"]/following-sibling::android.view.View)[6]')))
        y = x.get_attribute('content-desc')
        z = y.split()
        second_date = z[0]
        return first_date, second_date

    def delete_dates(self):
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.widget.Button[@content-desc="10%"]/following-sibling::android.view.View)[8]'))).click()
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.widget.Button[@content-desc="10%"]/following-sibling::android.view.View)[5]'))).click()

    def verify_dates_removed(self):
        try:
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.widget.Button[@content-desc="10%"]/following-sibling::android.view.View)[6]')))
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.widget.Button[@content-desc="10%"]/following-sibling::android.view.View)[3]')))
        except:
            return True


    def create_TB(self, name):
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.Button[@content-desc="Touchbase with '+ name +'"]'))).click()
        self.scroll_down()
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText[@text="Notes"]'))).click()
        ActionChains(self.driver).send_keys("New Touchbase").perform()
        self.driver.hide_keyboard()
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.ImageView[@content-desc="In-Person"]'))).click()
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.Button[@content-desc="CREATE TOUCHBASE"]'))).click()

    def verify_TB(self, re_num):
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.Button[@content-desc="Back"]'))).click()
        self.select_re_from_list(re_num)
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.view.View)[10]'))).click()
        a =  self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.widget.ImageView)[1]')))
        b = a.get_attribute('content-desc')
        c = b.split()
        cust_name = c[-2] + ' ' + c[-1]
        return cust_name

    #def tap_symbol_plus(self):







































