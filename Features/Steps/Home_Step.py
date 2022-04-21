from behave import *

use_step_matcher("re")


@given("I am on app home page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given I am on app home page')


@step('I Login with user "testuser31"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And I Login with user "testuser31"')


@step('I create security pin for "testuser31"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And I create security pin for "testuser31"')


@when("I tap on club deals tab")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I tap on club deals tab')


@step("I select 'Request Information-Clubdeal' property from club deals tab")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And I select \'Request Information-Clubdeal\' property from club deals tab')


@step("I tap on Request information button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And I tap on Request information button')


@step('I tap "Information by mail" button')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And I tap "Information by mail" button')


@then("I see message 'We would be happy to send you further background information on this project.'")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: Then I see message \'We would be happy to send you further background information on this project.\'')


@step("I can see 'Funding Phase-Clubdeal' property on club deals tab")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And I can see \'Funding Phase-Clubdeal\' property on club deals tab')


@then("I verify following text details of property 'Nova Living! Rahlstedt' in culb deal tab")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """



@given("I am on Finexity home page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given I am on Finexity home page')


@when("I click on login button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I click on login button')


@step('I enter the username "{username}"')
def step_impl(context, username):
    """
    :type context: behave.runner.Context
    :type username: str
    """
    raise NotImplementedError(u'STEP: And I enter the username "<username>"')


@step('I enter the password for "{password}"')
def step_impl(context, password):
    """
    :type context: behave.runner.Context
    :type password: str
    """
    raise NotImplementedError(u'STEP: And I enter the password for "<password>"')


@step("I click on sign in button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And I click on sign in button')


@then('I verify that user see "{message}" alert')
def step_impl(context, message):
    """
    :type context: behave.runner.Context
    :type message: str
    """
    raise NotImplementedError(u'STEP: Then I verify that user see "<message>" alert')


@step('I enter the username "(?P<username>.+)"')
def step_impl(context, username):
    """
    :type context: behave.runner.Context
    :type username: str
    """
    raise NotImplementedError(u'STEP: And I enter the username "<username>"')