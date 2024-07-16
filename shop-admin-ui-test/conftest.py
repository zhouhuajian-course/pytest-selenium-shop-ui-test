import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def baseurl():
    return "http://admin.shop.com/#"


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
