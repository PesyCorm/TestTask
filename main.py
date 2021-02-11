from CommonFiles import DriverStarter
from YandexPages import StartPage
from YandexPages import ResultList
import time


def test_tensor_search_in_yandex(driver):

	entry_field = StartPage(driver).enter_text_into_search()
	assert entry_field
	entry_field.send_keys("тензор")
	print(entry_field.get_attribute("aria-activedescendant"))
	StartPage(driver).find_button_click().click()
	ResultList(driver).return_result_list()
	time.sleep(3)

if __name__ == "__main__":
	with DriverStarter("https://yandex.ru") as driver:
		test_tensor_search_in_yandex(driver)