from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class OrderPageLocators(BasePage):

    # Экран "Для кого самокат"
    ACCEPT_COOKIE_BUTTON = (By.XPATH, '//button[@id="rcc-confirm-button"]')
    TOP_ORDER_BUTTON = (By.XPATH, '//div[contains(@class, "Header_Nav")]/button[text()="Заказать"]')
    MIDDLE_ORDER_BUTTON = (By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button')
    TITLE_OF_CUSTOMER_INFO_PAGE = (By.XPATH, '//div[text()="Для кого самокат" and contains(@class, "Order_Header")]')
    NAME_INPUT = (By.XPATH, '//input[@placeholder="* Имя"]')
    SURNAME_INPUT = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    DELIVERY_ADDRESS = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_FIELD = (By.XPATH, '//input[@class="select-search__input"]')
    METRO_STATIONS_SELECTOR = (By.XPATH, '//div[@class="select-search__select"]')
    SELECT_STATION = (By.XPATH, '//button[@value="4"]')
    TELEPHONE_NUMBER = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH, '//button[text()="Далее"]')

    # Экран "Про аренду"
    TITLE_OF_RENT_INFO_PAGE = (By.XPATH, '//div[contains(text(),"Про аренду")]')
    DELIVERY_DATE_FIELD = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    CALENDAR = (By.XPATH, '//div[@class="react-datepicker-popper"]')
    CALENDAR_DAY = (By.XPATH, '//div[contains(@class, "react-datepicker__day react-datepicker__day--031")]')
    RENTAL_PERIOD_FIELD = (By.XPATH, '//div[text()="* Срок аренды"]')
    RENTAL_DURETION = (By.XPATH, '//div[contains(text(),"сутки")]')
    SCOOTER_COLOUR = (By.XPATH, '//input[@id="black"]')
    COMMENT_FOR_COURIER = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    MAKE_ORDER_BUTTON = (By.XPATH, '//div[contains(@class, "Order_Buttons")]/button[text()="Заказать"]')
    CONFIRM_BUTTON= (By.XPATH, '//button[contains(text(),"Да")]')
    CHECK_STATUS_BUTTON = (By.XPATH, '//button[contains(text(),"Посмотреть статус")]')

