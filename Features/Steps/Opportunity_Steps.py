from behave import *

# use_step_matcher("re")
use_step_matcher("parse")

@step("User fills all required data into their respective field for opportunity")
def step_impl(context):
    for row in context.table:
        flag = context.op.show_opp_field(row['Field'])
        assert flag == True
    # context.op.scroll_to()


@step("User select opportunity")
def step_impl(context):
    context.op.select_opportunity()


@then("User verifies following options are displayed in opportunity details")
def step_impl(context):
    for row in context.table:
        context.op.display_details(row['Field'])


@then("User verifies following option are displayed")
def step_impl(context):
    for row in context.table:
        s = context.op.verifying_page_field(row['Field'])
        assert row['Field'] == s


@then('User verifies list is displayed')
def step_impl(context):
    context.op.verify_list()


@step('User selects "{option}" option')
def step_impl(context, option):
    context.op.choose_option(option)


@step('User taps on "{validate}" option for validation')
def step_impl(context, validate):
    context.op.scroll_to()
    context.op.option_for_validation(validate)


@then('User verifies "{Message}" is displayed on page for validation')
def step_impl(context, Message):
    pass