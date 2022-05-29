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

@step('user selects Estimated Order Date "{date}"')
def step_impl(context, date):
    context.re.order_date(date)

@step("user enter following details for selected Customer Info options")
def step_impl(context):
    for row in context.table:
        context.re.cust_info(row['Field'], row['Value'])

@step("user enters the Primary Contact details as")
def step_impl(context):
    context.re.tap_new()
    #context.re.scroll_down()

    for row in context.table:
        context.re.primary_contact(row['Field'], row['Value'])

@step('user enter Pre-RE Footprint(Sq ft) as "{number}"')
def step_impl(context, number):
    context.re.select_footprint(number)

@step('user enters Lift Capabilities as "{capability}"')
def step_impl(context, capability):
    context.re.select_lift_capability()

@step('user selects Color "{color}"')
def step_impl(context, color):
    context.re.select_color(color)

@step("user enter following details for Metrics as:")
def step_impl(context):
    context.re.select_metrics()

@step("user taps Create Requirements Estimate")
def step_impl(context):
    context.re.create_estimation()

@then("user verifies RE details page is displayed")
def step_impl(context):
    a,b = context.re.verify_re_page_displayed()
    print(a)
    assert a == 'Joe M'
    assert b == 'london'

@step('user taps on "search" symbol')
def step_impl(context):
    context.re.tap_search()

@step('user enters "{number}" in search field')
def step_impl(context, number):
    context.re.search_re(number)

@step('user selects RE# "{re_num}"')
def step_impl(context, re_num):
    context.re.select_re(re_num)

@then("user verifies following options are available for filter by")
def step_impl(context):
    for row in context.table:
        s = context.re.verify_fields(row['Field'])
        assert row['Field'] == s

@then('user verifies searched RE details page is displayed')
def step_impl(context):
    a = context.re.verify_re()
    assert a == "772"

@step('user taps on "downward arrow"')
def step_impl(context):
    context.re.tap_arrow()

@then('user verifies REs displayed are in ascending order of REID')
def step_impl(context):
    a = context.re.verify_ascend_descend(21)
    b = context.re.verify_ascend_descend(23)
    print(a)
    print(b)
    assert int(a) < int(b)

@then("user verifies REs displayed are in descending order of REID")
def step_impl(context):
    a = context.re.verify_ascend_descend(21)
    b = context.re.verify_ascend_descend(23)
    print(a)
    print(b)
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

@then('user verifies "Requirements changed" subtitle is displayed')
def step_impl(context):
    a, b = context.re.verify_subtitle()
    assert a == "Requirements"
    assert b == "changed"


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


@step('user taps on "Swap Contact"')
def step_impl(context):
    context.re.tap_swap_contact()


@step("user selects first Contact displayed in the list")
def step_impl(context):
    context.re.select_contact()


@then("user verifies swapped contact is displayed")
def step_impl(context):
    c = context.re.verify_swapped_contact()
    assert c == "Todd Floyd"


@step("user swap back the contacts")
def step_impl(context):
    context.re.swap_back_contact()

@step("user adds new RE as test_RE with following customer info details")
def step_impl(context):
    context.re.re_tab()
    context.re.tap_symbol()
    context.re.add_re()
    for row in context.table:
        context.re.cust_info(row['Field'], row['Value'])
    context.re.scroll_to_create()
    context.re.create_estimation()

@step("user search test_RE")
def step_impl(context):
    context.re.get_test_RE()
    context.re.tap_search()

@step("user selects test_RE from RE list")
def step_impl(context):
    context.re.select_test_RE()

@then('user verifies "Requirements process" subtitle is displayed')
def step_impl(context):
    a, b = context.re.verify_subtitle()
    assert a == "Requirements"
    assert b == "process"


@step('user selects Opportunity "{num}"')
def step_impl(context, num):
    context.re.select_opportunity(num)
    context.re.scroll_end()


@step('user selects colour "{colour}"')
def step_impl(context, colour):
    context.re.select_colour(colour)


@then("user verifies RE details page is displayed with opportunity")
def step_impl(context):
    a = context.re.verify_re_opportunity()
    assert a == "Opp #16"


@step("user taps and selects following details as")
def step_impl(context):
    for row in context.table:
        context.re.fill_details(row['Field'], row['Value'])


@step("user edits the following details displayed")
def step_impl(context):
    context.re.tap_contact()
    for row in context.table:
        context.re.fill_cust_contact(row['Field'], row['Value'])
    context.re.save_contact()


@step('user selects Lift Capabilities as "5k Forklift"')
def step_impl(context):
    context.re.select_lift_caps()


@step('user taps on "Save Changes"')
def step_impl(context):
    context.re.save_changes()


@then("user verifies that following details in RE Info tab are displayed")
def step_impl(context):
    a,b,c,d,e,f,g,h = context.re.verify_changes()
    assert a == "Opportunity #17"
    assert b == "Chris Dykes"
    assert c == "West"
    assert d == "Fredrick"
    assert e == "Jackson"
    assert f == "79"
    assert g == "5k Forklift"
    assert h == "TAN"




@step('user enters Pre-RE Footprint(Sq ft) as "{num}"')
def step_impl(context, num):
    context.re.enter_pre_re(num)


@then("user verifies dates are added successfully")
def step_impl(context):
    a,b = context.re.verify_dates()
    assert a == "6/11/2022"
    assert b == "9/21/2022"

@step("user taps on Add Another Date")
def step_impl(context):
    context.re.tap_add_date()


@step('user taps on "Save Changes" to save dates')
def step_impl(context):
    context.re.tap_save_changes()


@step("user scrolls down")
def step_impl(context):
    context.re.scroll_date()


@step("user taps on 'x' symbol to delete dates")
def step_impl(context):
    context.re.delete_dates()
    context.re.tap_save_changes()


@then("user verifies that the dates are removed successfully")
def step_impl(context):
    pass


@step('user taps on Touchbase with "{name}"')
def step_impl(context, name):
    context.re.create_TB(name)

@then("user verifies Touchbase is created")
def step_impl(context):
    a = context.re.verify_TB()
    assert a == "Collin Woods"