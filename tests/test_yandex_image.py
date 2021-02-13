from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from YandexPages import StartPage, \
                        image_main_text, \
                        image_main_object, \
                        ImageSearchPage, \
                        circle_buttons

import pytest
import time

# Картинки на Яндексе
# ___________________________________________________________
# Тест иногда падал в процессе перелистывания картинок
#   -после добавления time.sleep (стр. 40 и 44) падений не было

def test_yandex_image(driver):

    assert StartPage(driver).click_on_yandex_service("Картинки", True), "Ссылка на Я.Картинки не обнаружена на странице"
    StartPage(driver).click_on_yandex_service("Картинки").click()

    driver.switch_to.window(WebDriverWait(driver, 5).until(lambda driver: driver.window_handles[1]))

    assert WebDriverWait(driver, 10).until(lambda driver: "https://yandex.ru/images/" in driver.current_url), "Ожидалось 'https://yandex.ru/images/' в адресной строке"

    searched_image_text = image_main_text(driver, 0)
    image_main_object(driver, 0).click()

    assert ImageSearchPage(driver).value_image_entry_field() == searched_image_text, f"Открыли категорию {searched_image_text}, поле поиска содержит другое значение"

    ImageSearchPage(driver).image_on_document(0).click()
    assert WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "MMImageContainer")
        )
    ), "Картинка не открылась"

    time.sleep(2)
    href_image = driver.current_url

    circle_buttons(driver, "forward").click()
    time.sleep(2)
    assert driver.current_url != href_image, "При нажатии кнопки вперед картинка не изменилась"

    circle_buttons(driver, "back").click()
    assert WebDriverWait(driver, 10).until(lambda driver: href_image == driver.current_url), "Изображение не равно изначальному"
