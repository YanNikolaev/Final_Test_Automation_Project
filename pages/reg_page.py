from pages.base_page import WebPage
from pages.elements import WebElement


class RegistrationPage(WebPage):

    def __init__(self, web_driver):
        url = 'https://b2c.passport.rt.ru'
        super().__init__(web_driver, url)
        web_driver.get(url)

    register_link = WebElement(id='kc-register')

    first_name_field = WebElement(xpath='//input[@name="firstName"]')

    last_name_field = WebElement(xpath='//input[@name="lastName"]')

    data_field = WebElement(id='address')

    password_input = WebElement(id='password')

    password_confirm = WebElement(id='password-confirm')

    register_button = WebElement(xpath='//button[@name="register"]')

    warning_message_names = WebElement(xpath='//div[@class="rt-input-container rt-input-container--error"]')

    warning_message_data = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[3]/span[1]')

    warning_message_confirm_pass = WebElement(css_selector='section#page-right > div > div > div > form > div:nth-of-type(4) > div > span')

    warning_message_pass = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[4]/div[1]/span[1]')
