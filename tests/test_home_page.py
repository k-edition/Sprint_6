from page_objects.home_page import HomePageScooter
from data import DataScooter
from conftest import driver
import pytest
import allure


class TestHomePageScooter:

    question_num_and_answer = [[0, DataScooter.ANSWER_0],
                               [1, DataScooter.ANSWER_1],
                               [2, DataScooter.ANSWER_2],
                               [3, DataScooter.ANSWER_3],
                               [4, DataScooter.ANSWER_4],
                               [5, DataScooter.ANSWER_5],
                               [6, DataScooter.ANSWER_6],
                               [7, DataScooter.ANSWER_7]]

    @allure.title('Проверка ответа вопрос в  разделе "Вопросы о важном"')
    @allure.description('На главной странице нажимаем на вопрос и сверяем текст ответа')
    @pytest.mark.parametrize('num, answer', question_num_and_answer)
    def test_check_text_answer(self, driver, num, answer):
        home_page = HomePageScooter(driver)
        home_page.click_question(num)
        home_page.check_text_answer(num, answer)
