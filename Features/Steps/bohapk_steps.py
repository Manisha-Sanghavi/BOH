from behave import *

# use_step_matcher("re")

use_step_matcher("parse")


@given("Given User is on BOH FPU homepage")
def step_impl(context):
    context.boh.dev_build()
    print("User is on Homepage")


@when('User enters username as "{username}"')
def step_impl(context, username):
    context.boh.enter_Username(username)


@step('User enters password as "{password}"')
def step_impl(context, password):
    context.boh.enter_Password(password)


@step('User taps on Sign In button')
def step_impl(context):
    context.boh.clickOn_Login()


@then('User verifies "{message}" page is displayed')
def step_impl(context, message):
    context.boh.verify_page(message)


@given("User is on BOH FPU homepage")
def step_impl(context):
    context.boh.dev_build()
    print("User is on Homepage")


@when('User login with "{username}" and "{password}"')
def step_impl(context, username, password):
    context.boh.enter_Username(username)
    context.boh.enter_Password(password)
    context.boh.clickOn_Login()


@then('User verifies "{message}" "Customers" and REs are displayed on page')
def step_impl(context, message):
    context.boh.verify_page(message)
    context.boh.verify_tabs()


@step('User taps on "Administrator" option')
def step_impl(context):
    context.boh.click_admin()

@step('User taps on "Sign Out" button')
def step_impl(context):
    context.boh.clickOn_Signout()

@then('User verifies "Homepage" is displayed')
def step_impl(context):
    context.boh.verify_homepage()

@step('user is navigated to "Customer Management" page')
def step_impl(context):
    context.boh.verify_page()

@step("user taps on RE tab")
def step_impl(context):
    context.boh.re_tab()


@step('user taps on "Sort By" option')
def step_impl(context):
    context.boh.click_sortby()


@then("user verifies option")
def step_impl(context):
    context.boh.verify_dropdownlist()