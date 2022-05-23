from behave import *

#use_step_matcher("re")
use_step_matcher("parse")

@given("User is on BOH FPU homepage")
def step_impl(context):
    context.boh.dev_build()
    print("User is on Homepage")


@when('User login with "{username}" and "{password}"')
def step_impl(context, username, password):
    context.boh.enter_Username(username)
    context.boh.enter_Password(password)
    context.boh.clickOn_Login()
    try:
        context.boh.skip()
    except:
        print("skip is skipped")

@step('user is navigated to "{message}" page')
def step_impl(context, message):
    context.boh.verify_page(message)

@step("user taps on RE tab")
def step_impl(context):
    context.re.re_tab()


@step('user taps on "{option}" options')
def step_impl(context, option):
    if option == "Sort By":
        context.re.click_sortby()
    elif option == "Filter By":
        context.re.click_filterby()

@then("user verifies following options are available for sort by")
def step_impl(context):
   #context.re.verify_dropdownlist()

    for row in context.table:
        s = context.re.verify_sortby_filterby(row['Field'])
        assert row['Field'] == s

@step("user taps on plus symbol")
def step_impl(context):
    context.re.tap_symbol()


@step("user taps on Add RE")
def step_impl(context):
    context.re.add_re()


@step('user selects Estimated Order Date "21/05/2022"')
def step_impl(context):
    context.re.order_date()


@step("user enter following details for selected Customer Info options")
def step_impl(context):
    context.re.cust_info()


@step("user enters the Primary Contact details as:")
def step_impl(context):
    for row in context.table:
        context.re.primary_contact(row['Feild'], row['Value'])


@step("user enter following details for Metrics as:")
def step_impl(context):
    context.re.select_metrics()


@step("user taps Create Requirements Estimate")
def step_impl(context):
    context.re.create_estimation()


@then("user verifies RE details page is displayed")
def step_impl(context):
    pass


@step('user taps on "search" symbol')
def step_impl(context):
    context.re.tap_search()


@step('user enters "772" in search field')
def step_impl(context):
    context.re.search_re()


@step('user selects "RE #772"')
def step_impl(context):
    context.re.select_re()

@then("user verifies following options are available for filter by")
def step_impl(context):
    for row in context.table:
        s = context.re.verify_sortby_filterby(row['Field'])
        assert row['Field'] == s


@then('user verifies "RE #772" details page is displayed')
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
