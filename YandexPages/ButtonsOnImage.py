from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def circle_buttons(driver, button):

    if button == "forward":
        return WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".CircleButton_type_next .CircleButton-Icon")
            )
        )
    elif button == "back":
        return WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".CircleButton_type_prev .CircleButton-Icon")
            )
        )