from locators.home_page_locators import HomePageLocators
from page_object.home_page import HomePage
from conftest import driver
from data import TestData
import pytest
import allure


class TestHomePageFaq:

    @allure.title('Проверка выпадающего списка в разделе "Вопросы о важном".')
    @allure.description('Проверяем, что при нажатии на вопрос, открывается соответствующий текст ответа.')
    @pytest.mark.parametrize(
        'question_number, expected_answer',
        [
            (0, TestData.ANSWERS_DICT.get(0)),
            (1, TestData.ANSWERS_DICT.get(1)),
            (2, TestData.ANSWERS_DICT.get(2)),
            (3, TestData.ANSWERS_DICT.get(3)),
            (4, TestData.ANSWERS_DICT.get(4)),
            (5, TestData.ANSWERS_DICT.get(5)),
            (6, TestData.ANSWERS_DICT.get(6)),
            (7, TestData.ANSWERS_DICT.get(7))
        ]
    )
    def test_questions(self, driver, question_number, expected_answer):
        home_page = HomePage(driver)
        home_page.wait_top_order_button_is_displayed()
        home_page.click_on_cookie_popup(HomePageLocators.ACCEPT_COOKIE_BUTTON)
        home_page.scroll_to_element()
        home_page.wait_visibility_of_faq_section()
        result = home_page.click_on_question_and_get_answer_text(question_number)
        assert home_page.check_answer(result, expected_answer)