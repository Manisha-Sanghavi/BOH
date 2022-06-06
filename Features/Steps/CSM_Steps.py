from behave import *

# use_step_matcher("re")
use_step_matcher("parse")

@then('User verifies "{message}" is not displayed on page')
def step_impl(context, message):
    flag = context.csm.verify_Message_CSM(message)
    assert flag == True


@then('User verifies "{message}" is displayed on RE_Page')
def step_impl(context, message):
    msg = context.csm.verify_RE_Page_message(message)
    # assert msg == True
