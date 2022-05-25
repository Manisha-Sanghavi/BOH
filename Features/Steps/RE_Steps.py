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
    a = context.re.verify_re_page_displayed()
    print(a)
    assert a == 'RE'

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

@step('user edits subtitle as "{text}"')
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
