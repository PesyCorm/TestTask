from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def image_main_object(driver, requested_section: int):
    return WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "PopularRequestList-Shadow")
        )
    )[requested_section]


def image_main_text(driver, requested_section: int):
    return WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "PopularRequestList-SearchText")
        )
    )[requested_section].text
