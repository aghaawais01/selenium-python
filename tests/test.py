from pages.base_page import BasePage
from pages.home import HomePage
import unittest
from selenium import webdriver

class SimpleTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.home_page = HomePage(self.driver)

    def test_home(self):
        self.home_page.visit('/index.php')
        import time; time.sleep(6)


