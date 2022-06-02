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

@then("user verifies following options are available for sort by")
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

@step('user taps on MM/DD/YYYYY')
def step_impl(context):
    context.re.tap_date()

@step('user selects Estimated Order Date "{date}"')
def step_impl(context, date):
    context.re.order_date(date)

@step("user enter following details for selected Customer Info options")
def step_impl(context):
    for row in context.table:
        context.re.cust_info(row['Field'], row['Value'])

@step("user enters the Primary Contact details as")
def step_impl(context):
    context.re.scroll_down()
    context.re.tap_new()
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
    context.re.select_color(color)

@step("user enter following details for Metrics as:")
def step_impl(context):
    context.re.select_metrics()

@step("user taps Create Requirements Estimate")
def step_impl(context):
    context.re.create_estimation()

@then('user verifies "{re}" page is displayed with details "{name}" and "{location}"')
def step_impl(context, re, name, location):
    a,b = context.re.verify_page_displayed(re)
    print(a)
    assert a == name
    assert b == location

@step('user taps on "search" symbol')
def step_impl(context):
    context.re.tap_search()

@step('user enters "{number}" in search field')
def step_impl(context, number):
    context.re.search_re(number)

@step('user selects RE# "{re_num}"')
def step_impl(context, re_num):
    context.re.select_re()

@then("user verifies following options are available for filter by")
def step_impl(context):
    for row in context.table:
        s = context.re.verify_fields(row['Field'])
        assert row['Field'] == s

@then('user verifies searched RE# "{re_num}" details page is displayed')
def step_impl(context, re_num):
    a = context.re.verify_re()
    assert a == re_num

@step('user taps on "downward arrow"')
def step_impl(context):
    context.re.tap_arrow()

@then('user verifies REs displayed are in ascending order of REID')
def step_impl(context):
    a = context.re.get_first_re()
    b = context.re.get_second_re()
    assert int(a) < int(b)

@then("user verifies REs displayed are in descending order of REID")
def step_impl(context):
    a = context.re.get_first_re()
    b = context.re.get_second_re()
    assert int(a) > int(b)

@then("user verifies following options are displayed")
def step_impl(context):
    for row in context.table:
        s = context.re.verify_fields(row['Field'])
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
    a = context.re.verify_re_status(RE_Status)
    b = RE_Status.upper()
    assert a == b

@then("user verifies the following headers and tabs are displayed")
def step_impl(context):
    for row in context.table:
        context.re.verify_header_tabs(row['Field'])


@step('user taps on "Info" tab')
def step_impl(context):
    context.re.tap_info_tab()

@step('user searches RE# "{num}" from RE list')
def step_impl(context, num):
    context.re.tap_search()
    context.re.search_re(num)
    context.re.select_re()

@step('user taps on "Swap Contact"')
def step_impl(context):
    context.re.tap_swap_contact()


@step("user selects Contact '{contact}' displayed in the list")
def step_impl(context, contact):
    context.re.select_contact(contact)


@then("user verifies swapped contact '{contact}' is displayed")
def step_impl(context, contact):
    c = context.re.verify_swapped_contact()
    assert c == contact


@step("user swap back the contact to '{contact}'")
def step_impl(context, contact):
    context.re.swap_back_contact(contact)

@step("user adds new RE as test_RE with following customer info details")
def step_impl(context):
    #context.re.re_tab()
    context.re.tap_symbol()
    context.re.add_re()
    for row in context.table:
        context.re.cust_info(row['Field'], row['Value'])
    for i in range(4):
        context.re.scroll_down()
    context.re.create_estimation()

@step("user search test_RE")
def step_impl(context):
    context.re.get_test_RE()
    context.re.tap_search()

@step("user selects test_RE with location '{loc}' from RE list")
def step_impl(context, loc):
    context.re.select_test_RE(loc)

@then('user verifies "{subtitle}" subtitle is displayed')
def step_impl(context, subtitle):
    a, b = context.re.verify_subtitle()
    new_subtitle = a + ' ' + b
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
    a = context.re.verify_page_displayed(opportunity)
    assert a == opp


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


# @step('user taps on "Save Changes"')
# def step_impl(context):
#     context.re.save_changes()


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
    x = 0
    y = 0
    values = [date1,x ,y,date2]
    for i in [0, 3]:
         a = context.re.verify_dates(i)
         assert a == values[i]
    #assert b == date2

@step("user taps on Add Another Date")
def step_impl(context):
    context.re.tap_add_date()


@step('user taps on "Save Changes" to save dates')
def step_impl(context):
    context.re.tap_save_changes()


@step("user scrolls down")
def step_impl(context):
    for i in range(3):
        context.re.scroll_down()

@step("user taps on 'x' symbol to delete dates")
def step_impl(context):
    context.re.delete_dates()
    context.re.tap_save_changes()


@then("user verifies that the dates are removed successfully")
def step_impl(context):
    a = context.re.verify_dates_removed()
    assert a == True

@step('user taps on Touchbase with "{name}"')
def step_impl(context, name):
    context.re.create_TB(name)

@then("user verifies Touchbase is created with '{cust}' for RE# '{re_num}'")
def step_impl(context, cust, re_num):
    a = context.re.verify_TB(re_num)
    assert a == cust


@step("user taps on '+' symbol")
def step_impl(context):
    context.re.tap_symbol_plus()


@step("user edits the following details")
def step_impl(context):
    for row in context.table:
        context.re.fill_info_details(row['Field'], row['Value'])
    context.re.save_info_changes()


@then("user verifies that following details in Info tab of RE# test_RE are displayed")
def step_impl(context):
    context.re.re_back()
    context.re.tap_search()
    context.re.search_re()
    context.re.select_re()
    context.re.tap_info_tab()
    for row in context.table:
        s = context.re.verify_info_change(row['Field'], row['Value'])
        assert s == row['Value']