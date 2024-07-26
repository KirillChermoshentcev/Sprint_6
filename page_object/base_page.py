from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск элемента с ожиданием')
    def find_element_with_wait(self, locator, timeout=15):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Клик на кнопку разрешения использования cookies')
    def click_on_cookie_popup(self, locator, timeout=15):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).click()

    @allure.step('Проскроллили до элемента')
    def scroll_for_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Ожидание прогрузки элемента')
    def wait_visibility_of_element(self, locator, timeout=15):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Проверка, что элемент прогрузился')
    def check_element_is_displaying(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Кликнули на элемент')
    def click_on_element(self, locator):  # Кликнули на элемент
        self.find_element_with_wait(locator).click()

    @allure.step('Получение текста элемента')
    def get_text_from_element(self, locator):  # Получили текст элемента
        element = self.find_element_with_wait(locator)
        return element.text

    @allure.step('Форматирование локатора вопроса и ответа')
    def format_locator(self, locator, num):
        method, locator = locator
        locator = locator.format(num)
        return (method, locator)

    @allure.step('Ввод данных в поле ввода')
    def send_keys_to_input(self, locator, keys):
        element = self.find_element_with_wait(locator)
        element.send_keys(keys)

    @allure.step('Переключение на другую вкладку')
    def switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Получение заголовка страницы')
    def get_page_title(self, locator, timeout=15):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        return self.driver.title

