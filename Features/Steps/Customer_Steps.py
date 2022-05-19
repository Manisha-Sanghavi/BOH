from behave import *

# use_step_matcher("re")

use_step_matcher("parse")


@step('User select "{select_option}" option')
def step_impl(context, select_option):
    context.cust.select_option(select_option)


@then("User verifies customer list is sorted in ascending order")
def step_impl(context):
    context.cust.cust_list()