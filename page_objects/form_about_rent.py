from selenium.webdriver.common.by import By
from page_objects.base_page import BasePageScooter
import allure


class FormAboutRent(BasePageScooter):

    date_field = (By.XPATH, "//input[contains(@placeholder, 'Когда привезти')]")
    selected_day = (By.XPATH, "//div[contains(@class, 'selected')]")
    rent_time_field = (By.CLASS_NAME, 'Dropdown-root')
    period = (By.XPATH, "//div[@class='Dropdown-menu']/div[text()='сутки']")
    colour_check_box = (By.XPATH, "//input[@id='black']")
    comment_field = (By.XPATH, "//input[contains(@placeholder, 'Комментарий')]")
    order_button = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']")
    button_yes = (By.XPATH, "//button[text()='Да']")
    order_text = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']")

    @allure.step('Выбор даты, выпадающего календаря')
    def input_date(self, day):
        input_date = self.wait_and_find_element(self.date_field)
        input_date.send_keys(day)
        set_the_day = self.wait_and_find_element(self.selected_day)
        set_the_day.click()

    @allure.step('Выбор срока аренды из выпадающего списка')
    def set_rent_time(self, rent_time):
        set_time = self.wait_and_find_element(self.rent_time_field)
        set_time.click()
        text = str(self.period[1]).replace('сутки', f'{rent_time}')
        new_period = (By.XPATH, f"{text}")
        select_time = self.wait_and_find_element(new_period)
        select_time.click()

    @allure.step('Выбор цвета в чекбоксе')
    def set_colour(self, colour):
        text = str(self.colour_check_box[1]).replace('black', f'{colour}')
        new_colour = (By.XPATH, f"{text}")
        set_colour = self.wait_and_find_element(new_colour)
        set_colour.click()

    @allure.step('Ввод комментария')
    def input_comment(self, comment):
        input_comment = self.wait_and_find_element(self.comment_field)
        input_comment.send_keys(comment)

    @allure.step('Клик на кнопку "Заказать" под формой заказа')
    def click_order_button(self):
        self.wait_and_find_element(self.order_button).click()

    @allure.step('Клик на кнопку "Да" в окне "Хотите оформить заказ?"')
    def click_button_yes(self):
        self.wait_and_find_element(self.button_yes).click()

    @allure.step('Проверить, что появилось окно с сообщением "Заказ оформлен"')
    def check_order_is_placed(self):
        new_window = self.wait_and_find_element(self.order_text)
        text_in_window = new_window.text
        assert new_window.is_displayed() and 'Заказ оформлен' in text_in_window
