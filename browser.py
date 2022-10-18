import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Browser(unittest.TestCase):
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(10)
    driver.maximize_window()
    driver.delete_all_cookies()

    def close(self):
        self.driver.delete_all_cookies()
        self.driver.close()