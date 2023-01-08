import pytest
from selenium import webdriver

from pages.auth_page import AuthPage
from settings import valid_email, valid_password, invalid_email, invalid_password, correct_phone, incorrect_phone

@pytest.mark.parametrize("email", [valid_email, invalid_email], ids=["валидный адрес", "невалидный адрес"])
@pytest.mark.parametrize("password", [valid_password, invalid_password], ids=["валидный пароль", "невалидный пароль"])
def test_rostelekom_page_email(email, password):
    """Проверка для входа по адресу электронной почты."""
    web_browser = webdriver.Chrome('/Users/yan/Desktop/test/chromedriver')
    page = AuthPage(web_browser)
    page.username.send_keys(email)
    page.password.send_keys(password)
    web_browser.implicitly_wait(10)
    page.enter_button.click()
    if email == valid_email and password == valid_password:
        assert page.get_current_url() == 'https://start.rt.ru/?tab=main'
    else:
        assert page.message.get_text() == 'Неверный логин или пароль'
    page.close()


@pytest.mark.parametrize("phone", [correct_phone, incorrect_phone], ids=["корректный телефон", "некорректный телефон"])
@pytest.mark.parametrize("password", [valid_password, invalid_password], ids=["валидный пароль", "невалидный пароль"])
def test_rostelekom_page_phone(phone, password):
    """Проверка входа по номеру телефона."""
    web_browser = webdriver.Chrome('/Users/yan/Desktop/test/chromedriver')
    page = AuthPage(web_browser)

    page.username.send_keys(phone)
    web_browser.implicitly_wait(10)
    page.password.send_keys(password)

    web_browser.implicitly_wait(10)
    page.enter_button.click()
    if phone == correct_phone and password == valid_password:
        assert page.get_current_url() == 'https://b2c.passport.rt.ru/account_b2c/page?state=3e5e2e4f-5cd6-4818-9bb0-7d329d1f6e4c&client_id=account_b2c#/'
    else:
        assert page.message.get_text() == 'Неверный логин или пароль'
    page.close()


@pytest.mark.parametrize("login", ["<correct>", "<wrong>"], ids=["валидный логин", "невалидный логин"])
@pytest.mark.parametrize("password", ["<correct>", "<wrong>"], ids=["валидный пароль", "невалидный пароль"])
def test_rostelekom_page_login(login, password):
    """Проверка входа по логину.  Вместо "<correct>" подставить валидное значение,
    вместо "wrong" - любое незарегистрированное"""
    web_browser = webdriver.Chrome('/Users/yan/Desktop/test/chromedriver')
    page = AuthPage(web_browser)

    page.username.send_keys(login)
    web_browser.implicitly_wait(10)
    page.password.send_keys(password)

    web_browser.implicitly_wait(10)
    page.enter_button.click()
    if login == "correct" and password == "correct":
        assert page.get_current_url() == 'https://start.rt.ru/?tab=main'
    else:
        assert page.message.get_text() == 'Неверный логин или пароль'
    page.close()


@pytest.mark.parametrize("account", ["<correct>", "<wrong>"], ids=["валидный номер л/с", "невалидный номер л/с"])
@pytest.mark.parametrize("password", ["<correct>", "<wrong>"], ids=["валидный пароль", "невалидный пароль"])
def test_rostelekom_page_account(account, password):
    """Проверка входа по номеру лицевого счёта.  Вместо "<correct>" подставить валидное значение,
    вместо "wrong" - любое незарегистрированное"""
    web_browser = webdriver.Chrome('/Users/yan/Desktop/test/chromedriver')
    page = AuthPage(web_browser)

    page.username.send_keys(account)
    web_browser.implicitly_wait(3)
    page.password.send_keys(password)

    web_browser.implicitly_wait(3)
    page.enter_button.click()
    if account == "correct" and password == "correct":
        assert page.get_current_url() == 'https://start.rt.ru/?tab=main'
    else:
        assert page.message.get_text() == 'Неверный логин или пароль'
    page.close()
