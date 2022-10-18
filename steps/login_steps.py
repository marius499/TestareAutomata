from behave import *

@when('login: I set my email "{email}"')
def step_impl(context, email):
    context.login_page.set_email(email)

@when('login: I set my password "{password}" and click Continua')
def step_impl(context, password):
    context.login_page.set_password(password)
    context.login_page.click_continua_btn()
    #context.login_page.click_activeaza_mai_tarziu_btn()

@then('login: Verify if error message is received')
def step_impl(context):
    context.login_page.verify_error_msg()

@when('login: click on Fa-ti Cont')
def step_impl(context):
    context.login_page.click_customer_registration_menu_btn()
