from behave import *

# use_step_matcher("re")
use_step_matcher("parse")


@given("User is on app home page")
def step_impl(context):
    pass

@step("User taps on Already have an account button")
def step_impl(context):
    context.Homepage.Already_acc()


@step('User enters username "{username}"')
def step_impl(context, username):
    context.Homepage.enter_Username(username)


@step('User enters password "{password}"')
def step_impl(context, password):
    context.Homepage.enter_Password(password)


@step("User taps on Login button")
def step_impl(context):
    context.Homepage.clickOn_Login()

@then("Homepage is displayed")
def step_impl(context):
    pass



