from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CustomerRegisterPage(BasePage):

    EMAIL_INPUT = (By.ID, 'pizokel_customer_register_email')
    PASSWORD_INPUT = (By.XPATH, '//input[@id="pizokel_customer_register_password"]')
    CREEAZA_CONT_BTN = (By.ID, 'pizokel_customer_register_submit')
    AM_CITIT_CONDITII_CHK = (By.XPATH, '//label[@for="register-termscheck"]')
    MESAGE_ERROR_EMAIL_ADDRESS = (By.XPATH, '//div[text()="Adresa de Email nu este completata corect (exemplu: nume@exemplu.com)"]')
    MA_ABONEZ_CHK = (By.XPATH, '//label[@for="register-newsletter_subscription_type"]')
    MESSAGE_ERROR_CONDITII = (By.XPATH, '(//label[@class="register-checkbox-label"]/text())[1]')
    MESSAGE_ERROR_NO_PASSWORD = (By.XPATH, '//div[text()="Acest camp este obligatoriu"]')

    def set_email(self, email):
        self.wait_and_fill_elem_by_selector(*self.EMAIL_INPUT, email)

    def set_password(self, password):
        self.wait_and_fill_elem_by_selector(*self.PASSWORD_INPUT, password)

    def click_am_citit_conditii(self):
        self.wait_and_click_elem_by_selector(*self.AM_CITIT_CONDITII_CHK)

    def verify_message_error_email_address(self):
        self.verify_element_is_not_displayed_by_selector(*self.MESAGE_ERROR_EMAIL_ADDRESS)

    def click_ma_abonez_chk(self):
        self.wait_and_click_elem_by_selector(*self.MA_ABONEZ_CHK)

    def verify_message_error_conditii(self):
        self.verify_element_is_not_displayed_by_selector(*self.MESSAGE_ERROR_CONDITII)

    def verify_message_error_no_password(self):
        self.verify_element_is_not_displayed_by_selector(*self.MESSAGE_ERROR_NO_PASSWORD)

    def click_creeaza_cont_btn(self):
        self.wait_and_click_elem_by_selector(*self.CREEAZA_CONT_BTN)




