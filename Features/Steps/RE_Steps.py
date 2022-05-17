from behave import *

#use_step_matcher("re")
use_step_matcher("parse")

@given("User is on BOH FPU homepage")
def step_impl(context):
    context.re.dev_build()
    print("User is on Homepage")


@when('User login with "{username}" and "{password}"')
def step_impl(context, username, password):
    context.re.enter_Username(username)
    context.re.enter_Password(password)
    context.re.clickOn_Login()

@step('user is navigated to "Customer Management" page')
def step_impl(context):
    context.re.verify_page()

@step("user taps on RE tab")
def step_impl(context):
    context.re.re_tab()


@step('user taps on "Sort By" option')
def step_impl(context):
    context.re.click_sortby()


@then("user verifies following options are available:")
def step_impl(context):
    context.re.verify_dropdownlist()