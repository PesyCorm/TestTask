from YandexPages import StartPage, \
						return_result_list

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import pytest

# Поиск в Яндексе
# ___________________________________________________________
# В большинстве случаев тест падает из-за того,
# 	что на странице нет ожидаемого кол-ва ссылок на yandex.ru

def test_tensor_search_in_yandex(driver):

	entry_field = StartPage(driver).enter_text_into_search()
	assert entry_field, "Поле поиска не найдено"

	entry_field.send_keys("Яндекс")

	assert WebDriverWait(driver, 5).until(
		EC.presence_of_element_located(
			(By.CLASS_NAME, "mini-suggest__popup.mini-suggest__popup_svg_yes.mini-suggest__popup_visible")
		)
	), "Таблица с подсказками не обнаружена"

	entry_field.send_keys(Keys.ENTER)
	result_list = return_result_list(driver)

	counter = 0
	counter_results = 0

	for x in result_list:
		if result_list[counter]["check_ad"]:
			continue
		elif counter < 5:
			if "yandex.ru" in result_list[counter]["result_link"]:
				counter_results += 1
			counter += 1
		else:
			break

	assert counter_results == 5, f"Ожидалось, что первые 5 результатов содержат ссылку 'yandex.ru', обнаружено {counter_results}"