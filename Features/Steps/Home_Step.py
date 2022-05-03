from behave import *

#use_step_matcher("re")
use_step_matcher("parse")

@given("User is on app home page")
def step_impl(context):
    pass


@step('User enters username "{username}"')
def step_impl(context,username):
    context.signIn.enter_Username(username)


@step('User enters password "{password}"')
def step_impl(context,password):
    context.signIn.enter_Password(password);