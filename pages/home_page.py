from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from time import sleep


class HomePage(BasePage):

    ACCEPT_COOKIES_BTN = (By.XPATH, '//a[@id="accept-cookie-policy"]')
    BARBATI_MENU_BTN = (By.XPATH, '//a[@href="/t/barbati/"]')
    FETE_MENU_BTN = (By.XPATH, '//a[@href="/t/fete/"]')
    BAIETI_MENU_BTN = (By.XPATH, '//a[@href="/t/baieti/"]')
    CUSTOMER_AUTHENTICATION_BTN = (By.XPATH, '//a[@href="/customer/authentication"]')
    CUSTOMER_REGISTRATION_BTN = (By.XPATH, '//a[@href="/customer/authentication/register"]//parent::li')
    SEARCH_FIELD = (By.XPATH, '//*[@id="search-input"]')
    PAGE_FAQ_MENU_BTN = (By.XPATH, '//a[@href="/page/faq/"]')
    WISHLIST_MENU_BTN = (By.XPATH, '//a[@id="wishlist-top-menu"]')
    CART_MENU_BTN = (By.XPATH, '//a[@href="/cart/"]')
    SEARCH_BUTTON = (By.XPATH, '')
    INTRA_IN_CONT_BTN = (By.XPATH, '')
    SALUT_MSG = (By.XPATH, '')
    SEARCH_INPUT = (By.ID, '')
    INTRA_IN_CONT_CLOSE_BTN = (By.XPATH, '')

    def navigate_to_home_page(self):
        self.driver.get('https://www.fashiondays.ro')

    def click_accept_cookies_btn(self):
        self.click_if_present_by_selector(*self.ACCEPT_COOKIES_BTN)

    def click_barbati_menu_btn(self):
        self.wait_and_click_elem_by_selector(*self.BARBATI_MENU_BTN)

    def click_fete_menu_btn(self):
        self.wait_and_click_elem_by_selector(*self.FETE_MENU_BTN)

    def click_baieti_menu_btn(self):
        self.wait_and_click_elem_by_selector(*self.BAIETI_MENU_BTN)

    def click_customer_authentication_menu_btn(self):
        self.wait_and_click_elem_by_selector(*self.CUSTOMER_AUTHENTICATION_BTN)










