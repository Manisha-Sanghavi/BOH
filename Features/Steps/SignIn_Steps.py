from behave import *

# use_step_matcher("re")

use_step_matcher("parse")


@given("Given User is on BOH FPU homepage")
def step_impl(context):
    try:
        context.boh.dev_build()
        print("User is on Homepage")
    except:
        context.boh.dev_build()


@when('User enters username as "{username}"')
def step_impl(context, username):
    context.boh.enter_Username(username)


@step('User enters password as "{password}"')
def step_impl(context, password):
    context.boh.enter_Password(password)


@step('User taps on Sign In button')
def step_impl(context):
    context.boh.clickOn_Login()
    context.boh.skip()               # To skip security page

@step('User tap on "Administrator" option')
def step_impl(context):
    context.boh.click_admin()

@step('User tap on "Sign Out" button')
def step_impl(context):
    context.boh.clickOn_Signout()

@then('User verifies "Homepage" is displayed')
def step_impl(context):
    context.boh.verify_homepage()

@when('User login with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.boh.enter_Username(username)
    context.boh.enter_Password(password)
    context.boh.clickOn_Login()
    try:
        context.boh.skip()
    except:
        print("skip is skipped")

@then('User verifies "{message}" page is displayed')
def step_impl(context, message):

    context.boh.verify_page(message)
    context.boh.verify_message(message)


@then("User verifies following options are displayed on page")
def step_impl(context):
    for row in context.table:
        flag = context.boh.show_field(row['Field'])
        assert flag == True

@when('User taps on "{option_name}" option')
def step_impl(context, option_name):
    context.boh.tap_option(option_name)

@step('User navigated to "{Forgot_your_password}" page')
def step_impl(context, Forgot_your_password):
    flag = context.boh.page_navigate(Forgot_your_password)
    assert flag == True


@step('User enters email "{email}" in type your BOH email field')
def step_impl(context,email):
    context.boh.enter_mail(email)


@then('User verifies message "{message}" is displayed')
def step_impl(context,message):
    flag = context.boh.verify_message(message)
    assert flag == True


@when('User login with "{username}" and "{password}" for validation')
def step_impl(context, username, password):
    context.boh.enter_Username(username)
    context.boh.enter_Password(password)
    context.boh.clickOn_Login()

@step("User fills all required data into their respective field")
def step_impl(context):
    for row in context.table:
        context.boh.fill_data(row['Field'], row['Value'])


@then('user verifies "{message}" is displayed on page')
def step_impl(context,message):
    context.boh.verify_message(message)


@step("User click on created touchbase")
def step_impl(context):
    context.boh.Create_touchbase()


@then('User verifies "Customer" is deleted successfully.')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then User verifies "Customer" is deleted successfully.')

