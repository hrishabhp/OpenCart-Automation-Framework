import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def setup():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=Service(), options=options)

    driver.implicitly_wait(10)

    yield driver
    driver.quit()