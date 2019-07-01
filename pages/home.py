from base_page import BasePage
from selenium import webdriver


class HomePage(BasePage):

    # url =

    def click_women_tab(self):
        self.driver.find_element_by_css_selector('.sf-with-ul[title="Women"]')
