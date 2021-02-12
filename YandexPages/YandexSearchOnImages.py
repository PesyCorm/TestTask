from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ImageSearchPage:

    def __init__(self, driver):

        self.driver = driver

    def image_entry_field(self):

        pass

    def value_image_entry_field(self):

        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "input__control")
            )
        ).get_attribute("value")

    def image_on_document(self, number: int):

        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "serp-item__link")
            )
        )[number]