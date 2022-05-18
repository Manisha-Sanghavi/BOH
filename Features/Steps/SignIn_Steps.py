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

@step('User taps on "Administrator" option')
def step_impl(context):
    context.boh.click_admin()



@then('User verifies "{message}" page is displayed')
def step_impl(context, message):
    context.boh.verify_page(message)
