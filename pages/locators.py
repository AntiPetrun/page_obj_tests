from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form.well")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "form#register_form.well")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "input#id_login-username.form-control")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "input#id_login-password.form-control")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary[name='login-submit']")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "input#id_registration-email.form-control")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "input#id_registration-password1.form-control")
    REGISTRATION_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "input#id_registration-password2.form-control")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary[name='registration_submit']")


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, ".alertinner > strong")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")
