import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

class Login(unittest.TestCase):
    # elemente din pagina
    ACCEPT_COOKIES_BTN = (By.XPATH, '//a[@id="accept-cookie-policy"]')
    BARBATI_MENU_BTN = (By.XPATH, '//a[@href="/t/barbati/"]')
    FETE_MENU_BTN = (By.XPATH, '//a[@href="/t/fete/"]')
    BAIETI_MENU_BTN = (By.XPATH, '//a[@href="/t/baieti/"]')
    CUSTOMER_AUTHENTICATION_BTN = (By.XPATH, '//a[@href="/customer/authentication"]')
    SEARCH_FIELD = (By.XPATH, '//*[@id="search-input"]')
    PAGE_FAQ_MENU_BTN = (By.XPATH, '//a[@href="/page/faq/"]')
    WISHLIST_MENU_BTN = (By.XPATH, '//a[@id="wishlist-top-menu"]')
    CART_MENU_BTN = (By.XPATH, '//a[@href="/cart/"]')
    SEARCH_BUTTON = (By.XPATH, '')

    # se ruleaza inainte de fiecare testare

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://fashiondays.ro')  # url de start
        self.chrome.implicitly_wait(5)
        #self.chrome.find_element(*self.FORM_AUTH).click()

    # se ruleaza dupa fiecare test
    def tearDown(self):
        self.chrome.quit()

    # se verifica - url e corect
    def test_url(self):
        actual = self.chrome.current_url
        expected = 'https://www.fashiondays.ro/'
        self.assertEqual(expected, actual, 'Site-ul nu e corect')

    # se verifica titlul
    def test_page_title(self):
        actual = self.chrome.title
        expected = 'Colectii de moda pentru femei'
        self.assertEqual(expected, actual, 'titlul nu e corect')

    # se accepta cookie-urile
    def test_accept_cookies(self):
        self.chrome.find_element(*self.ACCEPT_COOKIES_BTN).click()

    # intrare pe pagina de Barbati si verificare titlu pagina
    def test_page_barbati(self):
        self.chrome.find_element(*self.BARBATI_MENU_BTN).click()
        sleep(3)
        actual = self.chrome.title
        expected = 'Colectii de moda pentru barbati'
        self.assertEqual(expected, actual, 'titlul nu e corect')

    # intrare pe pagina de Fete si verificare titlu pagina
    def test_page_fete(self):
        self.chrome.find_element(*self.FETE_MENU_BTN).click()
        sleep(3)
        actual = self.chrome.title
        expected = 'Destinatia de fashion #1 in Europa Centrala si de Est'
        self.assertEqual(expected, actual, 'titlul nu e corect')

    # intrare pe pagina de Baieti si verificare titlu pagina
    def test_page_baieti(self):
        self.chrome.find_element(*self.BAIETI_MENU_BTN).click()
        sleep(3)
        actual = self.chrome.title
        expected = 'Destinatia de fashion #1 in Europa Centrala si de Est'
        self.assertEqual(expected, actual, 'titlul nu e corect')

    # intrare pe pagina de autentificare
    def test_auth_page(self):
        self.chrome.find_element(*self.CUSTOMER_AUTHENTICATION_BTN).click()

    # cautare produs
    def test_search_item(self):
        self.chrome.find_element(*self.ACCEPT_COOKIES_BTN).click()
        sleep(5)
        self.chrome.find_element(*self.SEARCH_FIELD).click()
        sleep(5)
        self.chrome.find_element(*self.SEARCH_FIELD).send_keys('caciula')
        self.chrome.find_element(*self.SEARCH_FIELD).send_keys(Keys.RETURN)
        sleep(5)

    # intrare pe pagina de PAGE?FAQ si verificare titlu pagina
    def test_page_page_faq(self):
        self.chrome.find_element(*self.PAGE_FAQ_MENU_BTN).click()
        sleep(3)
        actual = self.chrome.title
        expected = 'Fashion Days - Cum te putem ajuta?'
        self.assertEqual(expected, actual, 'titlul nu e corect')
        sleep(5)

    # intrare pe pagina de Whishlist si verificare titlu pagina
    def test_page_wishlist(self):
        self.chrome.find_element(*self.WISHLIST_MENU_BTN).click()
        sleep(3)
        actual = self.chrome.title
        expected = 'Fashion Days - Favorite'
        self.assertEqual(expected, actual, 'titlul nu e corect')
        sleep(5)


    # intrare pe pagina de Cart si verificare titlu pagina
    def test_page_wishlist(self):
        self.chrome.find_element(*self.CART_MENU_BTN).click()
        sleep(3)
        actual = self.chrome.title
        expected = 'Fashion Days - Cosul Meu'
        self.assertEqual(expected, actual, 'titlul nu e corect')
        #sleep(5)

"""
    #hover pe incaltaminte
    def test_hover_incalmaminte(self):
    incaltaminte = self.chrome.find_element(By.XPATH, '//span[text()="Incaltaminte"]')
    hover =ActionChains(self.chrome).move_to_element(incaltaminte)
    hover.perform()
    sleep(2)
    """

"""
# hover pe bacanie
bacanie = driver.find_element(By.XPATH, '//span[text()="Bacanie"]')
hover = ActionChains(driver).move_to_element(bacanie)
hover.perform()
sleep(2)

# click pe dulciuri
driver.find_element(By.XPATH, '//a[text()="Dulciuri"]').click()
sleep(2)

# adaugam in cos bomboane Merci rosu
# observati ca pornim de la nume produs
# urcam in sus prin div-uri pana avem adaugar in cos cuprinsa in div
# coboram in jos pana la butonul pe care scrie adauga in cos
driver.find_element(By.XPATH, '//a[contains(text(), "Biscuiti")]/parent::div/parent::div/parent::div//button[text()="Adauga in Cos"]').click()
sleep(2)
# asteptam sa se incarce vezi detalii cos - dureaza ceva pana apre popup
detalii_cos = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "Vezi detalii cos")]')))

# click pe vezi detalii cos
detalii_cos.click()
sleep(2)
# click pe continua
driver.find_element(By.XPATH, '(//a[@href="/cart/checkout"])[1]').click()
sleep(2)
# verificam ca am ajuns pe pagina de login
assert driver.current_url == 'https://auth.emag.ro/user/login'

"""