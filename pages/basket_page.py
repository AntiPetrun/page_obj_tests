from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def should_be_empty_basket_opened_from_main_or_product_pages(self):
        self.is_guest_on_basket_page()
        self.is_basket_is_empty()
        self.should_be_message_empty_basket()

    def is_guest_on_basket_page(self):
        assert self.check_element_by_locator(
            *BasketPageLocators.BASKET_PAGE) == 'Basket', 'Basket page is not identified'

    def is_basket_is_empty(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_CONTAINER), 'Basket is not empty'

    def should_be_message_empty_basket(self):
        assert self.check_element_by_locator(
            *BasketPageLocators.BASKET_EMPTY_MESSAGE) == 'Your basket is empty. Continue shopping', 'No empty message'
