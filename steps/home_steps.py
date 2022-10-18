from behave import *


@given('home: I am a user on fashiondays.ro Home page')
def step_impl(context):
    context.home_page.navigate_to_home_page()
    context.home_page.click_accept_cookies_btn()


@when('home: I click on contul meu')
def step_impl(context):
    context.home_page.click_customer_authentication_menu_btn()

@when('home: I click on fa-ti cont')
def step_impl(context):
    context.home_page.c








