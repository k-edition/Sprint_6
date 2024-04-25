from selenium.webdriver.common.by import By
from page_objects.base_page import BasePageScooter
import allure


class HomePageScooter(BasePageScooter):

    question_0 = (By.ID, "accordion__heading-0")
    text_question_0 = (By.XPATH, "//div[@id='accordion__panel-0']/p")
    question_1 = (By.ID, "accordion__heading-1")
    text_question_1 = (By.XPATH, "//div[@id='accordion__panel-1']/p")
    question_2 = (By.ID, "accordion__heading-2")
    text_question_2 = (By.XPATH, "//div[@id='accordion__panel-2']/p")
    question_3 = (By.ID, "accordion__heading-3")
    text_question_3 = (By.XPATH, "//div[@id='accordion__panel-3']/p")
    question_4 = (By.ID, "accordion__heading-4")
    text_question_4 = (By.XPATH, "//div[@id='accordion__panel-4']/p")
    question_5 = (By.ID, "accordion__heading-5")
    text_question_5 = (By.XPATH, "//div[@id='accordion__panel-5']/p")
    question_6 = (By.ID, "accordion__heading-6")
    text_question_6 = (By.XPATH, "//div[@id='accordion__panel-6']/p")
    question_7 = (By.ID, "accordion__heading-7")
    text_question_7 = (By.XPATH, "//div[@id='accordion__panel-7']/p")

    order_button_header = (By.XPATH, "//div[@class='Header_Nav__AGCXC']/button[text()='Заказать']")
    order_button_middle = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/button")

    cookie_button = (By.ID, 'rcc-confirm-button')

    @allure.step('Согласие с использованием куки кликом на кнопку "да все привыкли"')
    def click_cookie_button(self):
        self.driver.find_element(*self.cookie_button).click()

    @allure.step('1.Клик на вопрос "Сколько это стоит? И как оплатить?"')
    def click_question_0(self):
        element = self.driver.find_element(*self.question_0)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait_and_find_element(self.question_0).click()

    @allure.step('1.Клик на вопрос "Хочу сразу несколько самокатов! Так можно?"')
    def click_question_1(self):
        element = self.driver.find_element(*self.question_1)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait_and_find_element(self.question_1).click()

    @allure.step('1.Клик на вопрос "Как рассчитывается время аренды?"')
    def click_question_2(self):
        element = self.driver.find_element(*self.question_2)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait_and_find_element(self.question_2).click()

    @allure.step('1.Клик на вопрос "Можно ли заказать самокат прямо на сегодня?"')
    def click_question_3(self):
        element = self.driver.find_element(*self.question_3)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait_and_find_element(self.question_3).click()

    @allure.step('1.Клик на вопрос "Можно ли продлить заказ или вернуть самокат раньше?"')
    def click_question_4(self):
        element = self.driver.find_element(*self.question_4)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait_and_find_element(self.question_4).click()

    @allure.step('1.Клик на вопрос "Вы привозите зарядку вместе с самокатом?"')
    def click_question_5(self):
        element = self.driver.find_element(*self.question_5)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait_and_find_element(self.question_5).click()

    @allure.step('1.Клик на вопрос "Можно ли отменить заказ?"')
    def click_question_6(self):
        element = self.driver.find_element(*self.question_6)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait_and_find_element(self.question_6).click()

    @allure.step('1.Клик на вопрос "Я живу за МКАДом, привезёте?"')
    def click_question_7(self):
        element = self.driver.find_element(*self.question_7)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait_and_find_element(self.question_7).click()

    @allure.step('Клик на кнопку "Заказать" вверху страницы')
    def click_order_button_header(self):
        self.driver.find_element(*self.order_button_header).click()

    @allure.step('Клик на кнопку "Заказать" внизу страницы')
    def click_order_button_middle(self):
        self.driver.find_element(*self.order_button_middle).click()

    @allure.step('2.Проверить, что текст ответа: "Сутки — 400 рублей. Оплата курьеру — наличными или картой."')
    def check_text_question_0(self):
        actually_value = self.driver.find_element(*self.text_question_0).text
        expected_value = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'

    @allure.step('2.Проверить, что текст ответа: "Пока что у нас так: один заказ — один самокат. Если хотите '
                 'покататься с друзьями, можете просто сделать несколько заказов — один за другим."')
    def check_text_question_1(self):
        actually_value = self.driver.find_element(*self.text_question_1).text
        expected_value = ('Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, '
                          'можете просто сделать несколько заказов — один за другим.')
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'

    @allure.step('2.Проверить, что текст ответа: "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат '
                 '8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ '
                 'курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."')
    def check_text_question_2(self):
        actually_value = self.driver.find_element(*self.text_question_2).text
        expected_value = ('Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. '
                          'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. '
                          'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.')
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'

    @allure.step('2.Проверить, что текст ответа: "Только начиная с завтрашнего дня. Но скоро станем расторопнее."')
    def check_text_question_3(self):
        actually_value = self.driver.find_element(*self.text_question_3).text
        expected_value = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'

    @allure.step('2.Проверить, что текст ответа: "Пока что нет! Но если что-то срочное — всегда можно позвонить '
                 'в поддержку по красивому номеру 1010."')
    def check_text_question_4(self):
        actually_value = self.driver.find_element(*self.text_question_4).text
        expected_value = ('Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому '
                          'номеру 1010.')
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'

    @allure.step('2.Проверить, что текст ответа: "Самокат приезжает к вам с полной зарядкой. Этого хватает на '
                 'восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."')
    def check_text_question_5(self):
        actually_value = self.driver.find_element(*self.text_question_5).text
        expected_value = ('Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если '
                          'будете кататься без передышек и во сне. Зарядка не понадобится.')
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'

    @allure.step('2.Проверить, что текст ответа: "Да, пока самокат не привезли. Штрафа не будет, объяснительной '
                 'записки тоже не попросим. Все же свои."')
    def check_text_question_6(self):
        actually_value = self.driver.find_element(*self.text_question_6).text
        expected_value = ('Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. '
                          'Все же свои.')
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'

    @allure.step('2.Проверить, что текст ответа: "Да, обязательно. Всем самокатов! И Москве, и Московской области."')
    def check_text_question_7(self):
        actually_value = self.driver.find_element(*self.text_question_7).text
        expected_value = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'

    @allure.step('Проверить, что url соответствует https://qa-scooter.praktikum-services.ru/')
    def check_current_url(self):
        current_url = self.driver.current_url
        assert current_url == 'https://qa-scooter.praktikum-services.ru/'
