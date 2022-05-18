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
    context.boh.skip()

@step('User taps on "Administrator" option')
def step_impl(context):
    context.boh.click_admin()

@step('User taps on "Sign Out" button')
def step_impl(context):
    context.boh.clickOn_Signout()

@then('User verifies "Homepage" is displayed')
def step_impl(context):
    context.boh.verify_homepage()



# @when('User login with "{username}" and "{password}"')
# def step_impl(context, username, password):
#     context.boh.enter_Username(username)
#     context.boh.enter_Password(password)
#     context.boh.clickOn_Login()
#     try:
#         context.boh.skip()
#     except:
#         print("skip is skipped")

@then('User verifies "{message}" page is displayed')
def step_impl(context, message):

    context.boh.verify_page(message)
    context.boh.verify_message(message)


@then("User verifies following options are displayed on page")
def step_impl(context):
    for row in context.boh.table:
        context.boh.show_field(row['Field'])


@when('User taps on "{option_name}" option')
def step_impl(context, option_name):
    context.boh.tap_option(option_name)

@step('User navigated to "{Forgot_your_password}" page')
def step_impl(context, Forgot_your_password):
    context.boh.page_navigate(Forgot_your_password)


@step('User enters email "{email}" in type your BOH email field')
def step_impl(context,email):
    context.boh.enter_mail(email)


@then('User verifies meassage "{message}" is displayed')
def step_impl(context,message):
    flag = context.boh.verify_message(message)
    assert flag == True


@when('User login with "{username}" and "{password}" for validation')
def step_impl(context, username, password):
    context.boh.enter_Username(username)
    context.boh.enter_Password(password)
    context.boh.clickOn_Login()

