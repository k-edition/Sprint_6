from selenium.webdriver.common.by import By
from page_objects.base_page import BasePageScooter
import allure


class HomePageScooter(BasePageScooter):

    question_0 = (By.ID, "accordion__heading-0")
    answer_0 = (By.XPATH, "//div[@id='accordion__panel-0']/p")
    question_1 = (By.ID, "accordion__heading-1")
    answer_1 = (By.XPATH, "//div[@id='accordion__panel-1']/p")
    question_2 = (By.ID, "accordion__heading-2")
    answer_2 = (By.XPATH, "//div[@id='accordion__panel-2']/p")
    question_3 = (By.ID, "accordion__heading-3")
    answer_3 = (By.XPATH, "//div[@id='accordion__panel-3']/p")
    question_4 = (By.ID, "accordion__heading-4")
    answer_4 = (By.XPATH, "//div[@id='accordion__panel-4']/p")
    question_5 = (By.ID, "accordion__heading-5")
    answer_5 = (By.XPATH, "//div[@id='accordion__panel-5']/p")
    question_6 = (By.ID, "accordion__heading-6")
    answer_6 = (By.XPATH, "//div[@id='accordion__panel-6']/p")
    question_7 = (By.ID, "accordion__heading-7")
    answer_7 = (By.XPATH, "//div[@id='accordion__panel-7']/p")

    order_button_header = (By.XPATH, "//div[@class='Header_Nav__AGCXC']/button[text()='Заказать']")
    order_button_middle = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/button")

    cookie_button = (By.ID, 'rcc-confirm-button')

    @allure.step('Согласие с использованием куки кликом на кнопку "да все привыкли"')
    def click_cookie_button(self):
        self.wait_and_find_element(self.cookie_button).click()

    @staticmethod
    def get_question(num):
        question = (By.ID, f"accordion__heading-{num}")
        return question

    @staticmethod
    def get_answer(num):
        answer = (By.XPATH, f"//div[@id='accordion__panel-{num}']/p")
        return answer

    @allure.step('1.Клик на вопрос')
    def click_question(self, num):
        self.scroll_to_element(self.get_question(num))
        self.wait_and_find_element(self.get_question(num)).click()

    @allure.step('Клик на кнопку "Заказать" вверху страницы')
    def click_order_button_header(self):
        self.wait_and_find_element(self.order_button_header).click()

    @allure.step('Клик на кнопку "Заказать" внизу страницы')
    def click_order_button_middle(self):
        self.wait_and_find_element(self.order_button_middle).click()

    @allure.step('2.Проверить текст ответа')
    def check_text_answer(self, num, answer):
        actually_value = self.wait_and_find_element(self.get_answer(num)).text
        expected_value = answer
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'

    @allure.step('Проверить, что url соответствует https://qa-scooter.praktikum-services.ru/')
    def check_current_url(self):
        current_url = self.get_current_url()
        assert current_url == 'https://qa-scooter.praktikum-services.ru/'
