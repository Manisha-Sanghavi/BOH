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
        try:
            self.wait.until(
                EC.presence_of_element_located((MobileBy.XPATH, "(//android.widget.Button)[1]/following-sibling::android.view.View[3]"))).click()
        except:
            self.wait.until(
                EC.presence_of_element_located(
                    (MobileBy.XPATH, "(//android.widget.Button)[1]/following-sibling::android.view.View[3]"))).click()

    def get_re_num(self, re_string):
            num = re_string[4:7]
            return num

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

    def tap_option_to_select(self, option):
        time.sleep(1)
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.view.View[@content-desc="'+option+'"]'))).click()

    def tap_to_select_op(self, option):
        self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.Button[@content-desc="'+option+'"]'))).click()

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

    # def tap_new(self):
    #     self.wait.until(
    #         EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.Button[@content-desc="New"]'))).click()

    def primary_contact(self, field,value):
        ele = self.driver.find_element(MobileBy.XPATH, '//android.widget.EditText[@text="'+field+'"]').click()
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

    # def select_color(self, color):
    #     self.wait.until(
    #             EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.Button[@content-desc='"+color+"']"))).click()
    #

    def verify_re(self):
        ele = self.wait.until(
            EC.presence_of_element_located(
                (MobileBy.XPATH, "//android.widget.ScrollView/android.view.View[1]")))
        re_string = ele.get_attribute('content-desc')
        num = self.get_re_num(re_string)
        return num

    # def create_estimation(self):
    #     self.wait.until(
    #         EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.Button[@content-desc='CREATE REQUIREMENTS ESTIMATE']"))).click()

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
        ele_string = re_string.split()
        if option == "RE":
            name = ele_string[4] + ' ' + ele_string[5]
            location = ele_string[6]
            return name, location
        if option == "Opportunity":
            opp = ele_string[3] + ' ' + ele_string[4]
            return opp

    def tap_search(self):
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.Button[@content-desc='Search']"))).click()

    def tap_re_to_select(self, loc, re_num):
        num = str(re_num)
        if re_num == "942":
            try:
                self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.view.View[@content-desc="'+loc+' - RE '+num+'"]'))).click()
            except:
                self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.view.View[@content-desc="'+loc+' - RE '+num+'"]'))).click()
        if re_num == "940":
            try:
                self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.view.View[@content-desc="'+loc+' - RE '+num+'"]'))).click()
            except:
                self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.view.View[@content-desc="'+loc+' - RE '+num+'"]'))).click()

    def search_re(self, number):
        try:
            re_num = self.wait.until(
                EC.presence_of_element_located(
                    (MobileBy.XPATH, "//android.widget.EditText[@text='Search REs']")))
            re_num.send_keys(number)
        except:
            re_num = self.wait.until(
                EC.presence_of_element_located(
                    (MobileBy.XPATH, "//android.widget.EditText[@text='Search REs']")))
            re_num.send_keys(number)

    def select_re(self, num, loc):
        #time.sleep(10)
        re_num = str(num)
        try:
            self.wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.View[@content-desc="'+loc+' - RE '+re_num+'"]'))).click()
        except:
            self.wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.View[@content-desc="'+loc+' - RE '+re_num+'"]'))).click()

    def tap_arrow(self):
        try:
            self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[18]"))).click()
        except:
            self.wait.until(
                EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[18]"))).click()

    def get_first_re(self):
        ele = self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[21]")))
        re_one = ele.get_attribute('content-desc')
        num = self.get_re_num(re_one)
        return num

    def get_second_re(self):
        ele = self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[23]")))
        re_one = ele.get_attribute('content-desc')
        num = self.get_re_num(re_one)
        return num

    def verify_fields(self, field):
        ele = self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.Button[@content-desc="'+field+'"]')))
        time.sleep(1)
        s = ele.get_attribute('content-desc')
        print(s)
        return s

    def verify_options(self, field):
        ele = self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.ImageView[@content-desc="' + field + '"]')))
        s = ele.get_attribute('content-desc')
        print(s)
        return s

    def verify_alternatives(self, field):
        ele = self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, '//android.view.View[@content-desc="' + field + '"]')))
        s = ele.get_attribute('content-desc')
        print(s)
        return s


    def select_re_from_list(self, re_num):
        self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[21]"))).click()

    def edit_subtitle(self, text):
        try:
            user_action = TouchAction(self.driver)
            user_action.tap(x=100,y=385).perform()
            re_text = self.wait.until(
                EC.presence_of_element_located((MobileBy.CLASS_NAME, "android.widget.EditText")))
            re_text.send_keys(text)
            self.wait.until(
                EC.presence_of_element_located((MobileBy.XPATH, "(//android.widget.Button)[3]"))).click()
        except:
            user_action = TouchAction(self.driver)
            user_action.tap(x=100, y=385).perform()
            re_text = self.wait.until(
                EC.presence_of_element_located((MobileBy.CLASS_NAME, "android.widget.EditText")))
            re_text.send_keys(text)
            self.wait.until(
                EC.presence_of_element_located((MobileBy.XPATH, "(//android.widget.Button)[3]"))).click()


    def verify_subtitle(self):
        try:
            ele = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[15]")))
        except:
            ele = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[15]")))
        ele_string = ele.get_attribute('content-desc')
        sub_string = ele_string.split()
        full_string = sub_string[2] + ' ' + sub_string[3]
        return full_string

    def select_re_status(self, re_status):
        self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.Button[@content-desc='"+re_status+"']"))).click()

    def verify_re_status(self, re_status):
        self.wait.until(
            EC.presence_of_element_located(
                (MobileBy.XPATH, "(// android.view.View)[21]"))).click()
        uc_re = re_status.upper()
        ele = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "//android.view.View[@content-desc='"+uc_re+"']")))
        ele_status = ele.get_attribute('content-desc')
        return ele_status

    def tap_info_tab(self):
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[11]"))).click()

    # def tap_swap_contact(self):
    #     self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.Button[@content-desc='Swap Contact']"))).click()

    def select_contact(self, contact):
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "//android.view.View[@content-desc='"+contact+"']"))).click()
        #self.driver.switch_to.default_content()
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[19]"))).click()

    def verify_swapped_contact(self):
        ele = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.view.View)[26]')))
        con_string = ele.get_attribute('content-desc')
        con_string = con_string.split()
        swap_con = con_string[2] + ' ' + con_string[3]
        return swap_con

    def swap_back_contact(self, contact):
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.Button[@content-desc='Swap Contact']"))).click()
        self.wait.until(EC.presence_of_element_located(
            (MobileBy.XPATH, '//android.view.View[@content-desc="'+contact+'"]'))).click()
        # self.driver.switch_to.default_content()
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[19]"))).click()

    def select_opportunity(self, num, name):
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.view.View[@content-desc="Opportunity"])[2]'))).click()
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, f"//android.view.View[@content-desc='Opp {num} • "+ name +"']"))).click()

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
            ele = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.Button[@content-desc="Swap Contact"]//parent::android.view.View')))
            cus_string = ele.get_attribute('content-desc')
            c = cus_string.split()
            cust_name = c[2] + ' ' + c[3]
            return cust_name
        if field == "Contact Email":
            ele = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.view.View[@content-desc="'+value+'"]')))
            cont_email = ele.get_attribute('content-desc')
            return cont_email
        if field == "Contact Phone":
            ele = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.view.View[@content-desc="'+value+'"]')))
            cont_phone = ele.get_attribute('content-desc')
            return cont_phone

    def fill_info_details(self, field, value):
        if field == "Sub-Title (optional)" or field == "Pre-RE Footprint (sq ft)":
            element = self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.EditText[@text='"+field+"']")))
            element.click()
            element.send_keys(value)
            self.wait.until(
                EC.presence_of_element_located((MobileBy.XPATH, "//android.view.View[@content-desc='New Requirements Estimate']"))).click()
        elif field == "Opportunity":
            element = self.wait.until(
                EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View[@content-desc='Opportunity'])[2]")))
            element.click()
            # to click on suggested search option
            self.wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, "//android.widget.EditText[@text='Search Opportunities']"))).send_keys(value)
            # Its taking option from suggested list
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "//android.view.View[@content-desc='"+value+"']"))).click()
            size = self.driver.get_window_size()
            startX = int(size["width"] / 2)
            startY = int(size["height"] / 2)*2
            endY = int(size["height"] / 4)*2
            print("startx" + str(startX) + " startY" + str(startY) + " EndY" + str(endY))
            self.driver.swipe(startX, startY, startX, endY)
            sleep(2)
        elif field == "Select Lift Capabilities":
            # user_action = TouchAction(self.driver)
            # self.scroll_down()
            # user_action.tap(x=516, y=1052).perform()  # individual locators for checkbox not available
            # user_action.tap(x=739, y=1558).perform()
            element = self.wait.until(
                EC.presence_of_element_located(
                    (MobileBy.XPATH, "//android.widget.CheckBox[@content-desc='"+value+"']")))
            value = element.get_atrribute('checked')
            print("value before setting attribute: " +value)
            change_value = element.setattr(value, 'true')
            print("The value of attribute after set new attribute: " +change_value)

    def change_back_contact(self, cust_name, email, phone):
        cus_string = cust_name.split()
        first_name = cus_string[0]
        surname = cus_string[1]
        values = [first_name, surname, email, phone]
        for i in range(2, 6):
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, f'(//android.widget.EditText)[{i}]'))).click()
            self.driver.find_element(MobileBy.XPATH, f'(//android.widget.EditText)[{i}]').clear()
            ActionChains(self.driver).send_keys(values[i - 2]).perform()
            self.driver.hide_keyboard()

    def fill_info_details(self, field, value):
            if field == "Opportunity":
                self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.view.View)[22]'))).click()
                self.wait.until(EC.presence_of_element_located(
                    (MobileBy.XPATH, '//android.view.View[@content-desc="' + value + '"]'))).click()
            if field == "Sales Rep":
                time.sleep(1)
                self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.view.View)[23]'))).click()
                self.wait.until(EC.presence_of_element_located(
                    (MobileBy.XPATH, '//android.view.View[@content-desc="' + value + '"]'))).click()
            if field == "Direct":
                self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.view.View)[24]'))).click()
                self.wait.until(EC.presence_of_element_located(
                    (MobileBy.XPATH, '//android.view.View[@content-desc="' + field + '"]'))).click()
                self.wait.until(EC.presence_of_element_located(
                    (MobileBy.XPATH, '//android.view.View[@content-desc="' + value + '"]'))).click()
                for i in range(3):
                    self.scroll_down()
            if field == "Pre-RE Footprint(sq ft)":
                self.wait.until(
                    EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText'))).click()
                self.driver.find_element(MobileBy.XPATH,'//android.widget.EditText').clear()
                ActionChains(self.driver).send_keys(value).perform()
                self.driver.hide_keyboard()
            if field == "Default Color":
                for i in range(2):
                    self.scroll_down()
                self.wait.until(EC.presence_of_element_located(
                    (MobileBy.XPATH, '//android.widget.Button[@content-desc="' + value + '"]'))).click()

    def save_info_changes(self):
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.view.View[@content-desc="SAVE CHANGES"]'))).click()
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.Button[@content-desc="Yes"]'))).click()

    def re_back(self):
        try:
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.Button[@content-desc="Back"]'))).click()
        except:
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.Button[@content-desc="Back"]'))).click()



    def confirm_delete(self):
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.Button[@content-desc="Yes"]'))).click()

    def verify_info_change(self, field, value):
        if field == "Opportunity":
                ele = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.view.View)[22]')))
                opp_string = ele.get_attribute('content-desc')
                b = opp_string.split()
                opp = b[1] + ' ' + b[2]
                return opp
        if field == "Sales Rep":
                ele = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.view.View)[23]')))
                sales_string = ele.get_attribute('content-desc')
                b = sales_string.split()
                sale_rep = b[2] + ' ' + b[3]
                return sale_rep
        if field == "Direct":
                ele = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.view.View)[24]')))
                dir_string = ele.get_attribute('content-desc')
                b = dir_string.split()
                dir = b[2]
                return dir
        if field == "Pre-RE Footprint (sq ft)":
                for i in range(4):
                    self.scroll_down()
                ele = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText')))
                pre_re_value = ele.get_attribute('text')
                return pre_re_value
        if field == "Default Color":
                ele = self.wait.until(
                    EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.Button[@content-desc="GREEN"]')))
                sales_string = ele.get_attribute('content-desc')
                return sales_string

    # def tap_add_date(self):
    #     self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.Button[@content-desc="Add Another Date"]'))).click()

    # def tap_save_changes(self):
    #     self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.view.View[@content-desc="SAVE CHANGES"]'))).click()

    def verify_dates(self, i):
            ele = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH,
                         f'(//android.widget.Button[@content-desc="10%"]/following-sibling::android.view.View)[{i + 3}]')))
            b = ele.get_attribute('content-desc')
            date_string = b.split()
            date = date_string[0]
            return date

        # a = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.widget.Button[@content-desc="10%"]/following-sibling::android.view.View)[3]')))
        # b = a.get_attribute('content-desc')
        # c = b.split()
        # first_date = c[0]
        # x = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.widget.Button[@content-desc="10%"]/following-sibling::android.view.View)[6]')))
        # y = x.get_attribute('content-desc')
        # z = y.split()
        # second_date = z[0]
        # return first_date, second_date

    def delete_dates(self):
        time.sleep(2)
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
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "(//android.view.View)[21]"))).click()
        #self.select_re_from_list(re_num)
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.view.View)[13]'))).click()
        try:
            ele =  self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.widget.ImageView)[1]')))
            b = ele.get_attribute('content-desc')
            string_TB = b.split()
            cust_name = string_TB[-2] + ' ' + string_TB[-1]
            return cust_name
        except:
            ele = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.widget.ImageView)[1]')))
            b = ele.get_attribute('content-desc')
            string_TB = b.split()
            cust_name = string_TB[-2] + ' ' + string_TB[-1]
            return cust_name

    def delete_TB(self, option):
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.widget.ImageView)[1]'))).click()
        self.tap_option_to_select(option)

    def tap_symbol_plus(self):
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.widget.ImageView)[1]'))).click()

    def tap_add_config(self):
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.widget.ImageView)[1]'))).click()
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.ImageView[@content-desc="Add Configuration"]'))).click()

    def select_config(self, config_sys):
        if config_sys == "Configuration System":
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.widget.Button)[1]'))).click()
        if config_sys == "Loose Products":
            time.sleep(2)
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.widget.Button)[2]'))).click()


    def enter_config_name(self, test_system):
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText'))).click()
        self.driver.find_element(MobileBy.XPATH, '//android.widget.EditText').clear()
        ActionChains(self.driver).send_keys(test_system).perform()

    def tap_create(self):
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.widget.Button)[4]'))).click()

    def tap_find_products(self):
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText'))).click()

    def add_product(self):
        user_action = TouchAction(self.driver)
        user_action.tap(x=991, y=1025).perform()

    def verify_system(self):
        #time.sleep(2)
        try:
            ele = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.widget.Button)[2]')))
        except:
            ele = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.widget.Button)[2]')))
        get_string = ele.get_attribute('content-desc')
        string_split = get_string.split()
        system_add = string_split[0] + ' ' + string_split[1]
        return system_add

    def delete_sys(self):
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.widget.Button)[3]'))).click()
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.view.View)[8]'))).click()

    def tap_system(self, option):
        if option == "New System":
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.widget.Button)[2]'))).click()
        if option == "New Configuration":
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.widget.Button)[8]'))).click()

    def verify_products(self, field):
        try:
            ele = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.ImageView[@content-desc="'+field+'"]')))
            ele_str = ele.get_attribute('content-desc')
            return ele_str
        except:
            ele = self.wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, '//android.widget.ImageView[@content-desc="' + field + '"]')))
            ele_str = ele.get_attribute('content-desc')
            return ele_str

    def verify_prod_no(self, option):
        time.sleep(2)
        element = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.view.View)[21]')))
        element_str = element.get_attribute('content-desc')
        num = element_str.split()
        if option == "Products":
            return num[2], num[5]
        if option == "Duplicates":
            return num[2]


    def verify_name(self):
        element = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.widget.Button)[2]')))
        ele_str = element.get_attribute('content-desc')
        name = ele_str.split()
        return name[0] + ' ' + name[1]

    def tap_to_select(self):
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.widget.Button)[3]'))).click()

    def tap_to_perform(self, option):
        if option == "System 1":
            self.wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, '//android.view.View[@content-desc="Edit system name"]'))).click()
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText'))).clear()
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText'))).send_keys(option)
            self.wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, '//android.widget.Button[@content-desc="Change"]'))).click()
        if option == "Configuration 1":
            self.wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, '//android.view.View[@content-desc="Edit configuration name"]'))).click()
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText'))).clear()
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText'))).send_keys(option)
            self.wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, '//android.widget.Button[@content-desc="Change"]'))).click()
        if option == "2":
            self.wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, '//android.view.View[@content-desc="Duplicate New System"]'))).click()
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText'))).clear()
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText'))).send_keys(option)
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.Button[@content-desc="Add"]'))).click()
        if option == "3":
            self.wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, '//android.view.View[@content-desc="Duplicate New Configuration"]'))).click()
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText'))).clear()
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.EditText'))).send_keys(option)
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.Button[@content-desc="Add"]'))).click()

    def delete_dup(self, num):
        if num == "3":
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.widget.Button)[9]'))).click()
            self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.view.View)[8]'))).click()
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.widget.Button)[7]'))).click()
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.view.View)[8]'))).click()
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.widget.Button)[5]'))).click()
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.view.View)[8]'))).click()

    def verify_deleted(self):
        time.sleep(2)
        element = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.view.View)[21]')))
        ele_str = element.get_attribute('content-desc')
        return ele_str

    def tap_re(self):
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.view.View)[23]'))).click()

    # def tap_status(self, re_status):
    #     self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.view.View[@content-desc="'+re_status+'"]'))).click()

    def verify_state_change(self):
        ele = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.view.View[@content-desc="INACTIVE"]')))
        ele_str = ele.get_attribute('content-desc')
        return ele_str

    def delete_RE(self):
        RE_element = self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.view.View)[15]')))
        value = RE_element.get_attribute('content-desc')
        print("Text of RE_element: " +value)
        text = value.split()
        print("The splitted text: " +text)
        msg = text[0]+ " "+text[1]
        print("Required new RE number: "+msg)
        return msg

    def select_RE(self):
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, '(//android.view.View)[21]'))).click()






































