from locators.order_page_locators import OrderPageLocators
from page_object.order_page import OrderPage
from conftest import driver
import pytest
from faker import Faker
import allure

faker = Faker('ru_RU')


class TestOrderPage:

    @allure.title('Проверка позитивного сценария оформления заказа самоката')
    @allure.description('Проверяем работу страниц оформления заказа с использованием нескольких наборов данных.')
    @pytest.mark.parametrize("name, surname, address, phone, comment", [
        (faker.first_name(), faker.last_name(), faker.street_name(), faker.numerify('+79########'), faker.sentence()),
        (faker.first_name(), faker.last_name(), faker.street_name(), faker.numerify('+79########'), faker.sentence())
    ])
    def test_order_page(self, driver, name, surname, address, phone, comment):
        order_page = OrderPage(driver)
        order_page.click_on_cookie_popup(OrderPageLocators.ACCEPT_COOKIE_BUTTON)
        order_page.click_on_top_order_button()
        order_page.fill_customer_info_page(name, surname, address, phone)
        order_page.wait_visibility_of_element(OrderPageLocators.NEXT_BUTTON)
        order_page.click_on_next_button()
        order_page.fill_rent_info_page(comment)
        assert order_page.check_status_button_is_displayed()





