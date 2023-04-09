from selenium.webdriver.common.by import By


class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group a.btn.btn-default")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form.well")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "form#register_form.well")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTRATION = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, ".alertinner > strong")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")


class BasketPageLocators:
    BASKET_PAGE = (By.CSS_SELECTOR, "div.page-header h1")
    BASKET_CONTAINER = (By.CSS_SELECTOR, "form#basket_formset")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "div#content_inner p")
