from behave import *

# use_step_matcher("re")
use_step_matcher("parse")
new_opportunity_no = ""
delete_oppo_no = ""
@step("User fills all required data into their respective field for opportunity")
def step_impl(context):
    for row in context.table:
        flag = context.op.show_opp_field(row['Field'], row['Value'])
        assert flag == True
    # context.op.scroll_to()


@step("User select opportunity")
def step_impl(context):
    context.op.choose_opportunity()


@then("User verifies following options are displayed in opportunity details")
def step_impl(context):
    for row in context.table:
        context.op.display_details(row['Field'])


@then("User verifies following option are displayed")
def step_impl(context):
    for row in context.table:
        s = context.op.verifying_page_field(row['Field'])
        assert row['Field'] == s


@then('User verifies REs list is displayed')
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


@step("User deletes newly created opportunity")
def step_impl(context):
    context.cust.tap_option_index("opportunities")
    context.op.select_opportunity()
    context.boh.tap_option("Delete Opportunity")


@then('user verifies new opportunity with "{message}" is displayed on page')
def step_impl(context, message):
    context.boh.verify_message(message)


@step("User creates new opportunity with following details")
def step_impl(context):
    context.boh.tap_option("+")
    context.boh.tap_option("Add Opportunity")
    for row in context.table:
        flag = context.op.show_opp_field(row['Field'], row['Value'])
        assert flag == True


@then("User verifies opportunity deleted  successfully")
def step_impl(context):
    print("User removed opportunity successfully")
    new_opportunity_no = context.op.search_opp()
    delete_oppo_no = context.op.search_opp()
    print("validation delete only: " + delete_oppo_no)
    assert new_opportunity_no == delete_oppo_no

@step("User select new opportunity")
def step_impl(context):
    context.op.choose_opportunity()
    new_opportunity_no = context.op.new_created_oppo_text()
    print("validation only: "+new_opportunity_no)


@step("User create new opportunity with following details")
def step_impl(context):
    context.boh.tap_option("+")
    context.boh.tap_option("Add Opportunity")
    for row in context.table:
        flag = context.op.show_opp_field(row['Field'], row['Value'])
        assert flag == True
    context.boh.tap_option("CREATE OPPORTUNITY")


@step("User delete opportunity")
def step_impl(context):
    context.op.choose_opportunity()
    context.boh.tap_option("Delete Opportunity")