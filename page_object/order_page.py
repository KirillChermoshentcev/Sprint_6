from faker import Faker
from page_object.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import allure

faker = Faker('ru_RU')


class OrderPage(BasePage):

    @allure.step('Кликаем на кнопку "Заказать" в шапке страницы')
    def click_on_top_order_button(self):
        self.click_on_element(OrderPageLocators.TOP_ORDER_BUTTON)

    @allure.step('Заполняем страницу "Для кого самокат".')
    def fill_customer_info_page(self, name, surname, address, phone):
        self.wait_visibility_of_element(OrderPageLocators.NAME_INPUT)
        self.send_keys_to_input(OrderPageLocators.NAME_INPUT, name)

        self.wait_visibility_of_element(OrderPageLocators.SURNAME_INPUT)
        self.send_keys_to_input(OrderPageLocators.SURNAME_INPUT, surname)

        self.wait_visibility_of_element(OrderPageLocators.DELIVERY_ADDRESS)
        self.send_keys_to_input(OrderPageLocators.DELIVERY_ADDRESS, address)

        self.wait_visibility_of_element(OrderPageLocators.METRO_FIELD)
        self.click_on_element(OrderPageLocators.METRO_FIELD)
        self.wait_visibility_of_element(OrderPageLocators.METRO_STATIONS_SELECTOR)
        self.click_on_element(OrderPageLocators.SELECT_STATION)

        self.wait_visibility_of_element(OrderPageLocators.TELEPHONE_NUMBER)
        self.send_keys_to_input(OrderPageLocators.TELEPHONE_NUMBER, phone)

    @allure.step('Кликаем на кнопку "Далее".')
    def click_on_next_button(self):
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполняем страницу "Про аренду"')
    def fill_rent_info_page(self, comment):
        self.wait_visibility_of_element(OrderPageLocators.DELIVERY_DATE_FIELD)
        self.click_on_element(OrderPageLocators.DELIVERY_DATE_FIELD)

        self.wait_visibility_of_element(OrderPageLocators.CALENDAR)
        self.click_on_element(OrderPageLocators.CALENDAR_DAY)

        self.wait_visibility_of_element(OrderPageLocators.RENTAL_PERIOD_FIELD)
        self.click_on_element(OrderPageLocators.RENTAL_PERIOD_FIELD)

        self.wait_visibility_of_element(OrderPageLocators.RENTAL_DURETION)
        self.click_on_element(OrderPageLocators.RENTAL_DURETION)

        self.click_on_element(OrderPageLocators.SCOOTER_COLOUR)

        self.wait_visibility_of_element(OrderPageLocators.COMMENT_FOR_COURIER)
        self.send_keys_to_input(OrderPageLocators.COMMENT_FOR_COURIER, comment)

        self.click_on_element(OrderPageLocators.MAKE_ORDER_BUTTON)

        self.wait_visibility_of_element(OrderPageLocators.CONFIRM_BUTTON)
        self.click_on_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step('Проверка отображения кнопки "Посмотреть статус"')
    def check_status_button_is_displayed(self):
        return self.check_element_is_displaying(OrderPageLocators.CHECK_STATUS_BUTTON)


