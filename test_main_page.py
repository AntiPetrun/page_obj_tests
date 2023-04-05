from selenium.webdriver.common.by import By
from urllib3.util import url

from .pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"


def test_should_be_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
