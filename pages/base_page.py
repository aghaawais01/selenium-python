from selenium import webdriver
from selenium.webdriver.common.by import By
from CONST import BASE_URL


class BasePage(object):

    def __init__(self, driver, base_url=BASE_URL):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 30

    def visit(self, url):
        url = self.base_url + url
        self.driver.get(url)
