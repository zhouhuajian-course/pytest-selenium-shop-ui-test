import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def baseurl():
    return "http://admin.shop.com/#"


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
