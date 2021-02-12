from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from CommonFiles import DriverStarter
from YandexPages import StartPage
from YandexPages import image_main_text, image_main_object
from YandexPages import ImageSearchPage
from YandexPages import circle_buttons
import pytest
import time


def test_yandex_image(driver):

	assert StartPage(driver).click_on_yandex_service("Картинки", True)
	StartPage(driver).click_on_yandex_service("Картинки").click()

	driver.switch_to.window(WebDriverWait(driver, 5).until(lambda driver: driver.window_handles[1]))

	assert WebDriverWait(driver, 10).until(lambda driver: "https://yandex.ru/images/" in driver.current_url)

	searched_image_text = image_main_text(driver, 1)
	image_main_object(driver, 1).click()

	assert ImageSearchPage(driver).value_image_entry_field() == searched_image_text

	ImageSearchPage(driver).image_on_document(1).click()
	assert WebDriverWait(driver, 10).until(
		EC.presence_of_element_located(
			(By.CLASS_NAME, "MMImageContainer")
		)
	)

	href_image = driver.current_url

	circle_buttons(driver, "forward").click()
	time.sleep(2)
	circle_buttons(driver, "back").click()
	assert WebDriverWait(driver, 10).until(lambda driver: href_image == driver.current_url)

	time.sleep(3)

if __name__ == "__main__":
	with DriverStarter("https://yandex.ru") as driver:
		test_yandex_image(driver)