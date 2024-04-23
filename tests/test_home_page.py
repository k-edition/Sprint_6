from page_objects.home_page import HomePageScooter
from conftest import driver
import allure


class TestHomePageScooter:

    @allure.title('Проверка ответа на 1й вопрос в  разделе "Вопросы о важном"')
    @allure.description('На главной странице нажимаем на 1й вопрос "Сколько это стоит? И как оплатить?", '
                        'открывается ответ: Сутки — 400 рублей. Оплата курьеру — наличными или картой.')
    def test_check_text_question_0(self, driver):
        home_page = HomePageScooter(driver)
        home_page.click_question_0()
        home_page.check_text_question_0()

    @allure.title('Проверка ответа на 2й вопрос в  разделе "Вопросы о важном"')
    @allure.description('На главной странице нажимаем на 2й вопрос "Хочу сразу несколько самокатов! Так можно?", '
                        'открывается ответ: Пока что у нас так: один заказ — один самокат. Если хотите покататься '
                        'с друзьями, можете просто сделать несколько заказов — один за другим.')
    def test_check_text_question_1(self, driver):
        home_page = HomePageScooter(driver)
        home_page.click_question_1()
        home_page.check_text_question_1()

    @allure.title('Проверка ответа на 3й вопрос в  разделе «Вопросы о важном»')
    @allure.description('На главной странице нажимаем на 3й вопрос "Как рассчитывается время аренды?", '
                        'открывается ответ: Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая '
                        'в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ '
                        'курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.')
    def test_check_text_question_2(self, driver):
        home_page = HomePageScooter(driver)
        home_page.click_question_2()
        home_page.check_text_question_2()

    @allure.title('Проверка ответа на 4й вопрос в  разделе «Вопросы о важном»')
    @allure.description('На главной странице нажимаем на 4й вопрос "Можно ли заказать самокат прямо на сегодня?",'
                        ' открывается ответ: Только начиная с завтрашнего дня. Но скоро станем расторопнее.')
    def test_check_text_question_3(self, driver):
        home_page = HomePageScooter(driver)
        home_page.click_question_3()
        home_page.check_text_question_3()

    @allure.title('Проверка ответа на 5й вопрос в  разделе «Вопросы о важном»')
    @allure.description('На главной странице нажимаем на 5й вопрос "Можно ли продлить заказ или вернуть самокат '
                        'раньше?", открывается ответ: Пока что нет! Но если что-то срочное — всегда можно '
                        'позвонить в поддержку по красивому номеру 1010.')
    def test_check_text_question_4(self, driver):
        home_page = HomePageScooter(driver)
        home_page.click_question_4()
        home_page.check_text_question_4()

    @allure.title('Проверка ответа на 6й вопрос в  разделе «Вопросы о важном»')
    @allure.description('На главной странице нажимаем на 6й вопрос "Вы привозите зарядку вместе с самокатом?", '
                        'открывается ответ: Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь '
                        'суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.')
    def test_check_text_question_5(self, driver):
        home_page = HomePageScooter(driver)
        home_page.click_question_5()
        home_page.check_text_question_5()

    @allure.title('Проверка ответа на 7й вопрос в  разделе «Вопросы о важном»')
    @allure.description('На главной странице нажимаем на 7й вопрос "Можно ли отменить заказ?", открывается '
                        'ответ: Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже '
                        'не попросим. Все же свои.')
    def test_check_text_question_6(self, driver):
        home_page = HomePageScooter(driver)
        home_page.click_question_6()
        home_page.check_text_question_6()

    @allure.title('Проверка ответа на 8й вопрос в  разделе «Вопросы о важном»')
    @allure.description('На главной странице нажимаем на 8й вопрос "Я живу за МКАДом, привезёте?", открывается '
                        'ответ: Да, обязательно. Всем самокатов! И Москве, и Московской области.')
    def test_check_text_question_7(self, driver):
        home_page = HomePageScooter(driver)
        home_page.click_question_7()
        home_page.check_text_question_7()
