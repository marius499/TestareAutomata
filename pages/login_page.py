from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CustomerAuthLoginPage(BasePage):

    EMAIL_INPUT = (By.ID, 'email')
    PASSWORD_INPUT = (By.ID, 'password')
    INTRA_IN_CONT_BTN = (By.ID, 'pizokel_customer_submit')
    REGISTER_BTN = (By.XPATH, '//a[@href="customer/authentication/register"]')
    EMAIL_ERROR_MSG = (By.XPATH, '//div[text()="Adresa de email sau parola este incorecta. Te rugam sa introduci o alta combinatie."]')
    CUSTOMER_REGISTRATION_BTN = (By.XPATH, '//a[@href="/customer/authentication/register"]//parent::li')

    def register_page(self):
        self.wait_and_click_elem_by_selector(*self.REGISTER_BTN)

    def set_email(self, email):
        self.wait_and_fill_elem_by_selector(*self.EMAIL_INPUT, email)

    def set_password(self, password):
        self.wait_and_fill_elem_by_selector(*self.PASSWORD_INPUT, password)

    def click_continua_btn(self):
        self.wait_and_click_elem_by_selector(*self.INTRA_IN_CONT_BTN)

    def verify_error_msg(self):
        self.verify_element_is_not_displayed_by_selector(*self.EMAIL_ERROR_MSG)

    def click_customer_registration_menu_btn(self):
        self.wait_and_click_elem_by_selector(*self.CUSTOMER_REGISTRATION_BTN)








