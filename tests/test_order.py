import pytest
from page_objects.home_page import HomePageScooter
from page_objects.form_who_orders_scooter import FormWhoOrdersScooter
from page_objects.form_about_rent import FormAboutRent
from data import DataScooter
from conftest import driver
import allure


class TestOrderScooter:
    pozitive_cases = [DataScooter.positive_case_1, DataScooter.positive_case_2]
    parameters = 'name, surname, address, station, phone, day, rent_time, colour, comment'

    @allure.title('Проверка позитивного сценария заказа')
    @allure.description('Позитивный сценарий включает: нажать кнопку "Заказать", Заполнить форму заказа, '
                        'Проверить, что появилось всплывающее окно с сообщением об успешном создании заказа')
    @pytest.mark.parametrize(parameters, pozitive_cases)
    def test_success_order(self, driver, name, surname, address, station, phone, day, rent_time, colour, comment):
        home_page = HomePageScooter(driver)
        home_page.click_cookie_button()
        home_page.click_order_button_header()
        form_who_orders = FormWhoOrdersScooter(driver)
        form_who_orders.input_name(name)
        form_who_orders.input_surname(surname)
        form_who_orders.input_address(address)
        form_who_orders.set_station(station)
        form_who_orders.input_phone(phone)
        form_who_orders.click_submit_button()
        form_about_rent = FormAboutRent(driver)
        form_about_rent.input_date(day)
        form_about_rent.set_rent_time(rent_time)
        form_about_rent.set_colour(colour)
        form_about_rent.input_comment(comment)
        form_about_rent.click_order_button()
        form_about_rent.click_button_yes()
        form_about_rent.check_order_is_placed()

    @allure.title('Проверка перехода на страницу формы заказа по кнопке "Заказать" вверху страницы')
    def test_order_button_header(self, driver):
        home_page = HomePageScooter(driver)
        home_page.click_cookie_button()
        home_page.click_order_button_header()
        form_who_orders = FormWhoOrdersScooter(driver)
        form_who_orders.check_current_url()

    @allure.title('Проверка перехода на страницу формы заказа по кнопке "Заказать" внизу страницы')
    def test_order_button_middle(self, driver):
        home_page = HomePageScooter(driver)
        home_page.click_cookie_button()
        home_page.click_order_button_middle()
        form_who_orders = FormWhoOrdersScooter(driver)
        form_who_orders.check_current_url()
