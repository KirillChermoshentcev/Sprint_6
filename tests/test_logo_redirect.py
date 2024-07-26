import allure

from conftest import driver
from page_object.home_page import HomePage
from locators.home_page_locators import HomePageLocators


class TestLogoRedirect:

    @allure.title('Проверка редиректа на главную страницу через лого Самоката')
    @allure.step('Проверка перехода на домашнюю страницу после нажатия на лого Самоката')
    def test_logo_scooter_redirect_to_home_page(self, driver):
        home_page = HomePage(driver)
        home_page.click_on_cookie_popup(HomePageLocators.ACCEPT_COOKIE_BUTTON)
        home_page.click_on_element(HomePageLocators.TOP_ORDER_BUTTON)
        home_page.wait_visibility_of_element(HomePageLocators.SCOOTER_LOGO)
        home_page.click_on_element(HomePageLocators.SCOOTER_LOGO)
        home_page.wait_visibility_of_element(HomePageLocators.HOME_PAGE_TITLE)
        assert home_page.check_home_page_title_is_displayed()

    @allure.title('Проверка редиректа на страницу Дзена через лого Яндекса')
    @allure.step('Проверка редиректа на страницу Дзена и переключения на новую вкладку после нажатия на лого Яндекса')
    def test_logo_yandex_redirect_to_dzen(self, driver):
        home_page = HomePage(driver)
        home_page.click_on_cookie_popup(HomePageLocators.ACCEPT_COOKIE_BUTTON)
        home_page.click_on_element(HomePageLocators.YANDEX_LOGO)
        home_page.switch_to_next_tab()
        assert home_page.get_page_title(HomePageLocators.DZEN_PAGE_IDENTIFIER) == 'Дзен'