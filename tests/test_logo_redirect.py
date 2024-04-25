from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.home_page import HomePageScooter
from page_objects.form_who_orders_scooter import FormWhoOrdersScooter
from conftest import driver
import allure


class TestLogoScooter:

    @allure.title('Проверка перехода по лого "Самокат"')
    @allure.description('При клике на логотип "Самокат", происходит переход на главную страницу "Самоката"')
    def test_logo_scooter_redurect(self, driver):
        home_page = HomePageScooter(driver)
        home_page.click_order_button_header()
        form_who_orders = FormWhoOrdersScooter(driver)
        form_who_orders.click_logo_scooter()
        home_page.check_current_url()

    @allure.title('Проверка перехода по лого "Яндекс"')
    @allure.description('При клике на логотип "Яндекс", в новом окне через редирект открывается главная страница Дзена')
    def test_logo_yandex_redirect(self, driver):
        home_page = HomePageScooter(driver)
        home_page.click_order_button_header()
        form_who_orders = FormWhoOrdersScooter(driver)
        form_who_orders.click_logo_yandex()
        WebDriverWait(driver, 5).until(expected_conditions.number_of_windows_to_be(2))
        windows = driver.window_handles
        driver.switch_to.window(windows[-1])
        WebDriverWait(driver, 5).until(expected_conditions.url_contains('https://dzen.ru/'))
        assert 'https://dzen.ru/' in driver.current_url
