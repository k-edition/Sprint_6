import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    firefox_driver = webdriver.Firefox()
    firefox_driver.get('https://qa-scooter.praktikum-services.ru/')
    yield firefox_driver
    firefox_driver.quit()
