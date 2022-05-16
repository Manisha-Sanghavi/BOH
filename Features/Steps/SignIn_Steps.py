from behave import *

# use_step_matcher("re")

use_step_matcher("parse")


@given("User is on BOH FPU homepage")
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


@when('User login with "{username}" and "{password}"')
def step_impl(context, username, password):
    context.boh.enter_Username(username)
    context.boh.enter_Password(password)
    context.boh.clickOn_Login()


@then('User verifies "{message}" is displayed')
def step_impl(context, message):
    context.boh.verify_message(message)


@then("User verifies following options are displayed on page")
def step_impl(context):
    for row in context.boh.table:
        context.boh.show_field(row['Field'])

