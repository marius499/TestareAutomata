from behave import *

@when('register: I set my email "{email}"')
def step_impl(context, email):
    context.register_page.set_email(email)

@when('register: I set my password "{password}"')
def step_impl(context, password):
    context.register_page.set_password(password)

@when('register: I click on Am citit termeni si conditii')
def step_impl(context):
    context.register_page.click_am_citit_conditii()

@when('register: I click ma abonez')
def step_impl(context):
    context.register_page.click_ma_abonez_chk()

@when('register: I click on creaza cont')
def step_impl(context):
    context.register_page.click_creeaza_cont_btn()

@then('register: verify error message for wrong email')
def step_impl(context):
    context.register_page.verify_message_error_email_address()

@then('register: verify error message accept terms and condition')
def step_impl(context):
    context.register_page.verify_message_error_conditii()

@then('register: verify error message no password')
def step_impl(context):
    context.register_page.verify_message_error_no_password()


