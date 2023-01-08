from pages.base_page import WebPage
from pages.elements import WebElement


class AuthPage(WebPage):

    def __init__(self, web_driver):
        url = 'https://b2c.passport.rt.ru'
        super().__init__(web_driver, url)
        web_driver.get(url)

    username = WebElement(xpath='//input[@id="username"]')

    password = WebElement(id='password')

    enter_button = WebElement(id='kc-login')

    forgot_link = WebElement(id='forgot_password')

    register_link = WebElement(id='kc-register')

    message = WebElement(id="form-error-message")