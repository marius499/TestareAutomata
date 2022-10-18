from pages.home_page import HomePage
from pages.login_page import CustomerAuthLoginPage
from pages.register_page import CustomerRegisterPage
from browser import Browser

def before_all(context):
    context.browser = Browser()
    context.home_page = HomePage()
    context.login_page = CustomerAuthLoginPage()
    context.register_page = CustomerRegisterPage()


def after_all(context):
    context.browser.close()