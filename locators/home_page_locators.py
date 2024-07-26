from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class HomePageLocators(BasePage):

    TOP_ORDER_BUTTON = (By.XPATH, '//div[contains(@class, "Header_Nav")]')
    MIDDLE_ORDER_BUTTON = (By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button')
    ACCEPT_COOKIE_BUTTON = (By.XPATH, '//button[@id="rcc-confirm-button"]')
    FAQ_SECTION = (By.XPATH, '//div[contains(@class, "Home_FAQ")]')
    SCOOTER_LOGO = (By.XPATH, '//a[@href="/" and contains(@class, "Header_LogoScooter")]')
    YANDEX_LOGO = (By.XPATH, '//a[@href="//yandex.ru" and contains(@class, "Header_LogoYandex")]')
    HOME_PAGE_TITLE = (By.XPATH, '//div[contains(@class, "Home_Header__")]')
    DZEN_PAGE_IDENTIFIER = (By.XPATH, '//title[contains(text(), "Дзен")]')

    FAQ_QUESTIONS = (By.XPATH, '//div[@id="accordion__heading-{}"] / parent :: div')
    FAQ_ANSWERS = (By.XPATH, '//div[@id="accordion__panel-{}"]')
    LAST_QUESTION = (By.XPATH, '//div[@id="accordion__heading-7"]')