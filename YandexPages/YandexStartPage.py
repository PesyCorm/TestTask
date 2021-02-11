from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class StartPage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_yandex_service(self, requested_service):

        services_list = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "services-new__item-title")
            )
        )

        for el in services_list:
            if requested_service in el.text:
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
