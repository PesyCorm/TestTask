from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Исполняется на главной странице Я.Картинки (https://yandex.ru/images/)
# Обе функции на вход принимают драйвер и номер блока (по умолчанию 0)
#   image_main_object возвращает блок поиска изображений
#   image_main_text возвращает текст этого блока

def image_main_object(driver, requested_section=0):
    return WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "PopularRequestList-Shadow")
        )
    )[requested_section]


def image_main_text(driver, requested_section=0):
    return WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "PopularRequestList-SearchText")
        )
    )[requested_section].text
