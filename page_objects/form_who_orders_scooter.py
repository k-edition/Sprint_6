from selenium.webdriver.common.by import By
from page_objects.base_page import BasePageScooter
from page_objects.form_about_rent import FormAboutRent
import allure


class FormWhoOrdersScooter(BasePageScooter):

    name_field = (By.XPATH, "//input[contains(@placeholder, 'Имя')]")
    surname_field = (By.XPATH, "//input[contains(@placeholder, 'Фамилия')]")
    address_field = (By.XPATH, "//input[contains(@placeholder, 'Адрес')]")
    station_field = (By.XPATH, "//input[contains(@placeholder, 'Станция')]")
    phone_field = (By.XPATH, "//input[contains(@placeholder, 'Телефон')]")
    submit_button = (By.XPATH, "//button[text()='Далее']")

    logo_scooter = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    logo_yandex = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")

    @allure.step('Вввод имени заказчика')
    def input_name(self, name):
        input_name = self.wait_and_find_element(self.name_field)
        input_name.send_keys(name)

    @allure.step('Вввод фамилии заказчика')
    def input_surname(self, surname):
        input_surname = self.wait_and_find_element(self.surname_field)
        input_surname.send_keys(surname)

    @allure.step('Вввод адреса, куда привези самокат')
    def input_address(self, address):
        input_address = self.wait_and_find_element(self.address_field)
        input_address.send_keys(address)

    @allure.step('Выбор станции метро из выпадающего списка')
    def set_station(self, station):
        set_station = self.wait_and_find_element(self.station_field)
        set_station.click()
        set_the_station = self.wait_and_find_element((By.XPATH, f"//ul[@class='select-search__options']//div[text()='{station}']"))
        set_the_station.click()

    @allure.step('Вввод номера телефона заказчика')
    def input_phone(self, phone):
        input_phone = self.wait_and_find_element(self.phone_field)
        input_phone.send_keys(phone)

    @allure.step('Клик на кнопку "Далее"')
    def click_submit_button(self):
        self.wait_and_find_element(self.submit_button).click()
        return FormAboutRent(self.driver)

    @allure.step('Клик на логотип "Самокат')
    def click_logo_scooter(self):
        self.wait_and_find_element(self.logo_scooter).click()

    @allure.step('Клик на логотип "Яндекс')
    def click_logo_yandex(self):
        self.wait_and_find_element(self.logo_yandex).click()

    @allure.step('Проверить, что url соответствует https://qa-scooter.praktikum-services.ru/order')
    def check_current_url(self):
        current_url = self.driver.current_url
        assert current_url == 'https://qa-scooter.praktikum-services.ru/order'