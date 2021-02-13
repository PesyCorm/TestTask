from selenium import webdriver
import pytest


@pytest.fixture
def driver(request):

    driver = webdriver.Chrome()
    driver.get("https://yandex.ru")
    request.addfinalizer(driver.quit)
    return driver