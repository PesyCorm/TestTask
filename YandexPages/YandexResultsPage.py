from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ResultList:

    def __init__(self, driver):
        self.driver = driver

    def return_result_list(self):

        result_list_len = len(WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "organic__url-text")
            )
        ))

        result_list_value = []
        
        for el in range(result_list_len):
            result_list_value.append(
                {"result_text": self.driver.find_elements_by_class_name("organic__url-text")[el].text,
                 "result_link": self.driver.find_elements_by_css_selector(".path__item")[el].get_attribute("href"),
                 "check_ad": True if "yabs.yandex.ru" in self.driver.find_elements_by_css_selector(".path__item")[
                     el].get_attribute("href") else False}
            )

        return result_list_value
