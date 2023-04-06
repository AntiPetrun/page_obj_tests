import time

from selenium.common import NoSuchElementException

from page_obj_tests.pages.base_page import BasePage
from page_obj_tests.pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def check_correct_product_in_basket(self):
        self.check_product_name()
        self.check_product_price()
        self.check_successful_message()

    def check_product_name(self):
        expected_element = self.get_element_by_locator(*ProductPageLocators.PRODUCT_NAME)
        actual_element_in_basket = self.get_element_by_locator(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)
        assert actual_element_in_basket == expected_element, 'Wrong product added to basket'

    def check_product_price(self):
        expected_element = self.get_element_by_locator(*ProductPageLocators.PRODUCT_PRICE)
        actual_element_in_basket = self.get_element_by_locator(*ProductPageLocators.PRICE_IN_BASKET)
        assert actual_element_in_basket == expected_element, 'Total amount of products in basket is not equal'

    def check_successful_message(self):
        expected_element = self.get_element_by_locator(*ProductPageLocators.PRODUCT_NAME)
        actual_element = self.get_element_by_locator(*ProductPageLocators.SUCCESS_MESSAGE)
        assert expected_element in actual_element, 'Message is not correct'
        print(actual_element)

    def guest_can_add_to_basket(self):
        try:
            add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
            add_to_basket.click()
        except NoSuchElementException:
            print("Button are not present")
