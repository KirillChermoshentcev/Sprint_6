from locators.home_page_locators import HomePageLocators
from page_object.base_page import BasePage
import allure


class HomePage(BasePage):

    @allure.step('Подождать отображение кнопки "Заказать" в шапке страницы')
    def wait_top_order_button_is_displayed(self):
        self.find_element_with_wait(HomePageLocators.TOP_ORDER_BUTTON)

    @allure.step('Проскроллили до элемента')
    def scroll_to_element(self):
        self.scroll_for_element(HomePageLocators.LAST_QUESTION)

    @allure.step('Подождать отображения блока с вопросами')
    def wait_visibility_of_faq_section(self):
        self.wait_visibility_of_element(HomePageLocators.FAQ_SECTION)

    @allure.step('Проверка отображения заголовка на домашней странице')
    def check_home_page_title_is_displayed(self):
        return self.check_element_is_displaying(HomePageLocators.HOME_PAGE_TITLE)

    @allure.step('Клик на вопрос')
    def click_on_question(self, num):
        formatted_question_locator = self.format_locator(HomePageLocators.FAQ_QUESTIONS, num)
        self.click_on_element(formatted_question_locator)

    @allure.step('Получения текста ответа')
    def get_text_answer(self, num):
        formatted_answer_locator = self.format_locator(HomePageLocators.FAQ_ANSWERS, num)
        return self.get_text_from_element(formatted_answer_locator)

    @allure.step('Проверка получения соответствующего ответа на выбранный вопрос')
    def click_on_question_and_get_answer_text(self, num):
        self.click_on_question(num)
        return self.get_text_answer(num)
    #@allure.step('Проверка соответствия результата')
    @staticmethod
    def check_answer(result, expected_answer):
        return result == expected_answer
