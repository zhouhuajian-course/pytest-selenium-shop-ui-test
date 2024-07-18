# 测试环境 灰度环境 生产环境
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.order(2)
def test_login_success(baseurl, driver):
    driver.get(baseurl + "/login")
    driver.refresh()
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("admin")
    driver.find_element(By.CSS_SELECTOR, ".el-form-item__content > .el-button").click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".user-avatar")))
    # assert ..


@pytest.mark.order(1)
def test_login_fail(baseurl, driver):
    driver.get(baseurl + "/login")
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("123456")
    driver.find_element(By.CSS_SELECTOR, ".el-form-item__content > .el-button").click()
    WebDriverWait(driver, 5).until(
        expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".el-message__content"),
                                                          "用户名或密码错误"))
    # assert
