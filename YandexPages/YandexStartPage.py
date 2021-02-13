from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Работает на главной странице yandex.ru
# В класс передается драйвер
# click_on_yandex_service принимает в аргумент имя сервиса (например, "Картинки"), возвращает элемент сервиса на странице
#   *также можно передать значение для аргумента return_href (например, True), тогда метод вернет ссылку на сервис
# enter_text_into_search возвращает элемент поля поиска
# find_button_click возвращает элемент кнопки "Найти"

class StartPage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_yandex_service(self, requested_service: str, return_href=None):

        services_list = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, ".services-new_adaptive_yes .services-new__item")
            )
        )

        for el in services_list:
            if requested_service in el.text:
                if return_href:
                    return el.get_attribute("href")
                return el

    def enter_text_into_search(self):

        return WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "input__control.input__input.mini-suggest__input")
            )
        )

    def find_button_click(self):

        return WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME,
                 "button.mini-suggest__button.button_theme_websearch.button_size_ws-head.i-bem.button_js_inited")
            )
        )
