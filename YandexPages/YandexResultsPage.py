from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Работает на странице результатов поиска
# В аргумент принимает драйвер
# Возвращает список с текстом, ссылками результатов поиска, проверкой на рекламу
#   *если результат является рекламой, check_ad будет True

    def return_result_list(driver):

        result_list_len = len(WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "organic__url-text")
            )
        ))

        result_list_value = []
        
        for el in range(result_list_len):
            result_list_value.append(
                {"result_text": driver.find_elements_by_class_name("organic__url-text")[el].text,
                 "result_link": driver.find_elements_by_css_selector(".path__item")[el].get_attribute("href"),
                 "check_ad": True if "yabs.yandex.ru" in driver.find_elements_by_css_selector(".path__item")[
                     el].get_attribute("href") else False}
            )

        return result_list_value
