from behave import *

#use_step_matcher("re")
use_step_matcher("parse")

@step("user taps on RE tab")
def step_impl(context):
    context.re.re_tab()

@step('user taps on "{option}" options')
def step_impl(context, option):
    if option == "Sort By":
        context.re.click_sortby()
    if option == "Filter By":
        context.re.click_filterby()

@then("user verifies following fields are available")
def step_impl(context):
      for row in context.table:
        s = context.re.verify_fields(row['Field'])
        assert row['Field'] == s

@step("user taps on plus symbol")
def step_impl(context):
    context.re.tap_symbol()

@step("user taps on Add RE")
def step_impl(context):
    context.re.add_re()

@step('user taps "{option}"')
def step_impl(context, option):
    context.re.tap_option_to_select(option)

@step('user selects Estimated Order Date "{date}"')
def step_impl(context, date):
    context.re.order_date(date)

@step("user enter following details for selected Customer Info options")
def step_impl(context):
    for row in context.table:
        context.re.cust_info(row['Field'], row['Value'])

@step('user enters the "{option}" Primary Contact details as')
def step_impl(context, option):
    context.re.scroll_down()
    context.re.tap_to_select_op(option)
    for row in context.table:
        context.re.primary_contact(row['Field'], row['Value'])

@step('user enter Pre-RE Footprint(Sq ft) as "{number}"')
def step_impl(context, number):
    context.re.scroll_down()
    context.re.select_footprint(number)

@step('user enters Lift Capabilities as "{capability}"')
def step_impl(context, capability):
    context.re.select_lift_capability()

@step('user selects Color "{color}"')
def step_impl(context, color):
    context.re.scroll_down()
    context.re.tap_to_select_op(color)
    context.re.scroll_down()

@step("user enter following details for Metrics as:")
def step_impl(context):
    context.re.select_metrics()

@step('user taps "{option}" to select')
def step_impl(context, option):
    context.re.tap_to_select_op(option)

@then('user verifies "{re}" page is displayed with details "{name}" and "{location}"')
def step_impl(context, re, name, location):
    cus_name,cus_loc = context.re.verify_page_displayed(re)
    assert cus_name == name
    assert cus_loc == location

@step('user taps on "search" symbol')
def step_impl(context):
    context.re.tap_search()

@step('user enters "{number}" in search field')
def step_impl(context, number):
    context.re.search_re(number)

@step('user selects RE# "{re_num}" with location "{loc}"')
def step_impl(context, re_num, loc):
    context.re.select_re(re_num, loc)

# @then("user verifies following options are available for filter by")
# def step_impl(context):
#     for row in context.table:
#         s = context.re.verify_fields(row['Field'])
#         assert row['Field'] == s

@then('user verifies searched RE# "{re_num}" details page is displayed')
def step_impl(context, re_num):
    get_num = context.re.verify_re()
    assert get_num == re_num

@step('user taps on "downward arrow"')
def step_impl(context):
    context.re.tap_arrow()

@then('user verifies REs displayed are in "{option}" order of REID')
def step_impl(context, option):
    one_re = context.re.get_first_re()
    two_re = context.re.get_second_re()
    if option  == "Ascending":
        assert int(one_re) < int(two_re)
    if option == "Descending":
        assert int(one_re) > int(two_re)

@then("user verifies following options are displayed")
def step_impl(context):
    for row in context.table:
        s = context.re.verify_options(row['Field'])
        assert row['Field'] == s

@then("user verifies following alternatives are displayed")
def step_impl(context):
    for row in context.table:
        s = context.re.verify_alternatives(row['Field'])
        assert row['Field'] == s



@step('user selects RE# "{re_num}" from RE list')
def step_impl(context, re_num):
    context.re.select_re_from_list(re_num)

@step('user enters subtitle as "{text}"')
def step_impl(context, text):
    context.re.edit_subtitle(text)

@step('user select "{RE_Status}" from dropdown list')
def step_impl(context, RE_Status):
    context.re.select_re_status(RE_Status)


@then('user verifies REs with state "{RE_Status}" only are displayed')
def step_impl(context, RE_Status):
    get_status = context.re.verify_re_status(RE_Status)
    upp_RE = RE_Status.upper()
    assert get_status == upp_RE

@then("user verifies the following headers and tabs are displayed")
def step_impl(context):
    for row in context.table:
        context.re.verify_header_tabs(row['Field'])


@step('user taps on "Info" tab')
def step_impl(context):
    context.re.tap_info_tab()

@step('user "{option}" RE# "{re_num}" with location "{loc}" from list')
def step_impl(context, option, re_num, loc):
    context.re.tap_to_select_op(option)
    context.re.tap_re_to_select(loc, re_num)


@step('user "{option}" RE# "{num}" with location "{loc}" from RE list')
def step_impl(context, option, num, loc):
    context.re.tap_to_select_op(option)
    context.re.search_re(num)
    context.re.select_re(num, loc)

@step("user selects Contact '{contact}' displayed in the list")
def step_impl(context, contact):
    context.re.select_contact(contact)


@then("user verifies swapped contact '{contact}' is displayed")
def step_impl(context, contact):
    cus_contact = context.re.verify_swapped_contact()
    assert cus_contact == contact


@step("user swap back the contact to '{contact}'")
def step_impl(context, contact):
    context.re.swap_back_contact(contact)

@step("user adds new RE as test_RE by tapping '{option}' with following customer info details")
def step_impl(context, option):
    #context.re.re_tab()
    context.re.tap_symbol()
    context.re.add_re()
    for row in context.table:
        context.re.cust_info(row['Field'], row['Value'])
    for i in range(4):
        context.re.scroll_down()
    context.re.tap_to_select_op(option)

@step("user search test_RE")
def step_impl(context):
    context.re.get_test_RE()
    context.re.tap_search()

@step("user selects test_RE with location '{loc}' from RE list")
def step_impl(context, loc):
    context.re.select_test_RE(loc)

@then('user verifies "{subtitle}" subtitle is displayed')
def step_impl(context, subtitle):
    new_subtitle = context.re.verify_subtitle()
    assert new_subtitle == subtitle

@step('user sets the subtitle as "original RE"')
def step_impl(context):
    context.re.set_subtititle()

@step('user selects Opportunity "{num}" with name "{name}"')
def step_impl(context, num, name):
    context.re.select_opportunity(num, name)
    for i in range(4):
        context.re.scroll_down()

@step('user selects colour "{colour}"')
def step_impl(context, colour):
    #context.re.scroll_down()
    context.re.select_colour(colour)


@then('user verifies RE details page is displayed with "{opportunity}" number "{opp}"')
def step_impl(context, opportunity, opp):
    get_opp = context.re.verify_page_displayed(opportunity)
    assert get_opp == opp

@step('user deletes created RE by tapping "{option}"')
def step_impl(context, option):
    context.re.tap_info_tab()
    for i in range(5):
        context.re.scroll_down()
    context.re.tap_option_to_select(option)
    context.re.confirm_delete()

# @step("user taps and selects following details as")
# def step_impl(context):
#     for row in context.table:
#         context.re.fill_details(row['Field'], row['Value'])

@step("user edits the following details displayed")
def step_impl(context):
    context.re.tap_contact()
    for row in context.table:
        context.re.fill_cust_contact(row['Field'], row['Value'])
    context.re.save_contact()

@step('user selects Lift Capabilities as "5k Forklift"')
def step_impl(context):
    context.re.select_lift_caps()

@then("user verifies that following details in RE Info tab are displayed")
def step_impl(context):
    for row in context.table:
            s = context.re.verify_details(row['Field'], row['Value'])
            assert row['Value'] == s

@step("user changes the contact details as '{cust_name}' with '{email}' and '{phone}'")
def step_impl(context, cust_name, email, phone):
    context.re.tap_contact()
    context.re.change_back_contact(cust_name, email, phone)
    context.re.save_contact()

@step('user enters Pre-RE Footprint(Sq ft) as "{num}"')
def step_impl(context, num):
    context.re.enter_pre_re(num)


@then("user verifies dates '{date1}' and '{date2}' are added successfully")
def step_impl(context, date1, date2):
    get_date2, get_date1 = context.re.verify_dates()
    assert get_date1 == date1
    assert get_date2 == date2

@step("user scrolls down")
def step_impl(context):
    for i in range(2):
        context.re.scroll_down()

@step('user taps on x symbol to delete dates and "{option}"')
def step_impl(context, option):
    context.re.delete_dates()
    context.re.tap_option_to_select(option)


@then("user verifies that the dates are removed successfully")
def step_impl(context):
    get_date = context.re.verify_dates_removed()
    assert get_date == True

@step('user taps on Touchbase with "{name}"')
def step_impl(context, name):
    context.re.create_TB(name)

@then("user verifies Touchbase is created with '{cust}' for RE# '{re_num}'")
def step_impl(context, cust, re_num):
    get_TB = context.re.verify_TB(re_num)
    assert get_TB == cust

@step('user "{option}"')
def step_impl(context, option):
    context.re.delete_TB(option)

@step("user taps on '+' symbol")
def step_impl(context):
    context.re.tap_symbol_plus()

@step("user edits the following details")
def step_impl(context):
    for row in context.table:
        context.re.fill_info_details(row['Field'], row['Value'])
    context.re.save_info_changes()

# @then("user verifies that following details in Info tab of RE# test_RE are displayed")
# def step_impl(context):
#     context.re.re_back()
#     context.re.tap_search()
#     context.re.search_re()
#     context.re.select_re()
#     context.re.tap_info_tab()
#     for row in context.table:
#         s = context.re.verify_info_change(row['Field'], row['Value'])
#         assert s == row['Value']

@step("user taps on plus symbol to Add Configuration")
def step_impl(context):
    context.re.tap_add_config()

@step('user creates "{sys_product}" name as "{test_Prod}"')
def step_impl(context, sys_product, test_Prod):
    context.re.select_config(sys_product)
    context.re.enter_config_name(test_Prod)
    context.re.tap_create()


@step('user adds product "{boh_product}"')
def step_impl(context, boh_product):
    #context.re.tap_find_products()
    #context.re.add_product()                #Individual locators not available
    context.re.re_back()


@then('user verifies "{test_System}" is displayed in Configured Systems list')
def step_impl(context, test_System):
    new_sys = context.re.verify_system()
    assert new_sys == test_System


@step('user deletes the "{test_System}"')
def step_impl(context, test_System):
    context.re.delete_sys()


# @step('user selects "{config_sys}"')
# def step_impl(context, config_sys):
#     context.re.tap_option_to_select(config_sys)


@then('user verifies "{test_Config}" is displayed in Loose Products list')
def step_impl(context, test_Config):
    new_config = context.re.verify_system()
    assert test_Config == new_config


@step('user taps on System Product "{sys_prod}"')
def step_impl(context, sys_prod):
    context.re.tap_system(sys_prod)

@then("user verifies following details about Products are displayed")
def step_impl(context):
    for row in context.table:
        s = context.re.verify_products(row['Field'])
        assert row['Field'] == s


@then("user verifies number of Configured Systems: '{n1}' and Loose Products: '{n2}' are displayed as RE '{Products}'")
def step_impl(context, n1, n2, Products):
        sys_num, prod_num = context.re.verify_prod_no(Products)
        assert sys_num == n1
        assert prod_num == n2


@step('user changes Configured System name as "{sys_name}"')
def step_impl(context, sys_name):
    context.re.tap_to_perform(sys_name)

@then('user verifies "{sys_name}" name is displayed')
def step_impl(context, sys_name):
    name = context.re.verify_name()
    assert name == sys_name

@step('user taps on three dots "..." of "{prod_name}" in the list')
def step_impl(context, prod_name):
    context.re.tap_to_select()

@step('user selects Duplicate "{prod_name}" to create "{num}" duplicates')
def step_impl(context, prod_name, num):
    context.re.tap_to_perform(num)


@then('user verifies "{num}" "{duplicates}" of the system is created for RE# "{re_num}" with location "{loc}"')
def step_impl(context,num, duplicates, re_num, loc):
    #context.re.re_back()
    #context.re.tap_search()
    #context.re.search_re(re_num)
    #context.re.select_re(re_num, loc)
    number = context.re.verify_prod_no(duplicates)
    assert int(number) == int(num) + 1


@step('user deletes the "{num}" duplicates')
def step_impl(context, num):
    context.re.delete_dup(num)


@step('user selects Delete "{sys_name}"')
def step_impl(context, sys_name):
    context.re.delete_sys()

@then('user verifies "New System" is deleted with message "{message}"')
def step_impl(context, message):
    msg = context.re.verify_deleted()
    print(msg)
    assert message == msg

@step("user taps on plus symbol to check the options")
def step_impl(context):
    context.re.tap_symbol_plus()

@then("following options are displayed")
def step_impl(context):
    for row in context.table:
        s = context.re.verify_fields(row['Field'])
        assert row['Field'] == s


# @then("user verifies following options are displayed")
# def step_impl(context):
#     for row in context.table:
#         s = context.re.verify_options(row['Field'])
#         assert row['Field'] == s


@step("user selects RE# 861")
def step_impl(context):
    context.re.tap_re()


@step('user taps on  "{re_status}" Status of RE')
def step_impl(context, re_status):
    context.re.tap_status(re_status)


@then('user verifies Status "{status}" is displayed')
def step_impl(context, status):
    re_state = context.re.verify_state_change()
    assert re_state == status


@step('user changes status "{opt1}" to "{opt3}" by tapping "{opt2}"')
def step_impl(context, opt1, opt3, opt2):
    context.re.tap_option_to_select(opt1)
    context.re.tap_option_to_select(opt2)
    context.re.tap_option_to_select(opt3)


@step('user enters email "{username}"')
def step_impl(context, username):
    context.boh.enter_email(username)