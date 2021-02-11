from CommonFiles import DriverStarter
from YandexPages import StartPage
from YandexPages import ResultList
import pytest
import time


def test_tensor_search_in_yandex(driver):

	entry_field = StartPage(driver).enter_text_into_search()
	assert entry_field
	entry_field.send_keys("тензор")
	time.sleep(2)
	assert driver.find_element_by_class_name("mini-suggest__popup.mini-suggest__popup_svg_yes.mini-suggest__popup_visible")
	StartPage(driver).find_button_click().click()
	result_list = ResultList(driver).return_result_list()
	counter = 0
	for el in result_list:
		if result_list[counter]["check_ad"]:
			continue
		if counter < 5:
			# assert "tensor.ru" in result_list[counter]["result_link"]
			# нужен pytest
			counter += 1
		else:
			break


	time.sleep(3)

if __name__ == "__main__":
	with DriverStarter("https://yandex.ru") as driver:
		test_tensor_search_in_yandex(driver)