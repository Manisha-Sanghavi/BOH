from behave import *

# use_step_matcher("re")

use_step_matcher("parse")


@step('User select "{select_option}" option')
def step_impl(context, select_option):
    context.cust.select_option(select_option)


@then("User verifies customer list is sorted in ascending order")
def step_impl(context):
    context.cust.cust_list_asc()


@then("User verifies customer list is sorted in descending order")
def step_impl(context):
    context.cust.select_arrow()
    context.cust.cust_list_dsc()


@then("User verifies Customer with only Active status are displayed")
def step_impl(context):
    context.cust.status_verification('8')
    # context.cust.status_verification('23')


@step('User select customer')
def step_impl(context):
        context.cust.select_customer('21')