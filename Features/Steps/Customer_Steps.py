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


@step('User search for customer "{cust}"')
def step_impl(context, cust):
    context.cust.search_customer(cust)


@then('User verifies "{message}" displayed on page')
def step_impl(context, message):
    context.cust.verify_message_on_page(message)

@then("User verifies Customer details page with following information is displayed")
def step_impl(context):
    for row in context.table:
        flag = context.cust.show_field_for_cust(row['Field'])
        assert flag == True


@then("User verifies following options are displayed on homepage")
def step_impl(context):
    for row in context.table:
        flag = context.cust.show_field_on_homepage(row['Field'])
        assert flag == True

@step('User verifies status changed to "{status}"')
def step_impl(context, status):
    context.cust.status_member(status)

@step('"{pop_up}" popup is displayed')
def step_impl(context, pop_up):
    context.cust.pop_up(pop_up)
