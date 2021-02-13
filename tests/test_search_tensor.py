from YandexPages import StartPage
from YandexPages import ResultList
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


def test_tensor_search_in_yandex(driver):

	entry_field = StartPage(driver).enter_text_into_search()
	assert entry_field, "Поле поиска не найдено"

	entry_field.send_keys("тензор")

	assert WebDriverWait(driver, 5).until(
		EC.presence_of_element_located(
			(By.CLASS_NAME, "mini-suggest__popup.mini-suggest__popup_svg_yes.mini-suggest__popup_visible")
		)
	), "Таблица с подсказками не обнаружена"

	StartPage(driver).find_button_click().click()
	result_list = ResultList(driver).return_result_list()

	counter = 0
	counter_results = 0

	for x in result_list:
		if result_list[counter]["check_ad"]:
			continue
		elif counter < 5:
			if "tensor.ru" in result_list[counter]["result_link"]:
				counter_results += 1
			counter += 1
		else:
			break

	assert counter_results == 5, f"Ожидалось, что первые 5 рузультатов содержат ссылку 'tensor.ru', обнаружено {counter_results}"