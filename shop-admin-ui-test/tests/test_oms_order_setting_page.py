import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_order_setting_form_validation(baseurl, driver):
    driver.get(baseurl + "/oms/order-setting")
    time.sleep(0.5)
    # 1
    element = driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(1) .el-input__inner")
    actions = ActionChains(driver)
    actions.double_click(element).perform()
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(1) .el-input__inner").send_keys(Keys.BACKSPACE)
    driver.find_element(By.CSS_SELECTOR, "html").click()
    WebDriverWait(driver, 5).until(expected_conditions.text_to_be_present_in_element(
        (By.CSS_SELECTOR, ".el-form-item:nth-child(1) .el-form-item__error"), "请输入大于0的正整数"))
    # 2
    element = driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(2) .el-input__inner")
    actions = ActionChains(driver)
    actions.double_click(element).perform()
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(2) .el-input__inner").send_keys("aaa")
    driver.find_element(By.CSS_SELECTOR, "html").click()
    WebDriverWait(driver, 5).until(expected_conditions.text_to_be_present_in_element(
        (By.CSS_SELECTOR, ".el-form-item:nth-child(2) .el-form-item__error"), "请输入大于0的正整数"))
    # 3
    element = driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(3) .el-input__inner")
    actions = ActionChains(driver)
    actions.double_click(element).perform()
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(3) .el-input__inner").send_keys("15.1")
    driver.find_element(By.CSS_SELECTOR, "html").click()
    WebDriverWait(driver, 5).until(expected_conditions.text_to_be_present_in_element(
        (By.CSS_SELECTOR, ".el-form-item:nth-child(3) .el-form-item__error"), "请输入大于0的正整数"))
    # 4
    element = driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(4) .el-input__inner")
    actions = ActionChains(driver)
    actions.double_click(element).perform()
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(4) .el-input__inner").send_keys("-7")
    driver.find_element(By.CSS_SELECTOR, "html").click()
    WebDriverWait(driver, 5).until(expected_conditions.text_to_be_present_in_element(
        (By.CSS_SELECTOR, ".el-form-item:nth-child(4) .el-form-item__error"), "请输入大于0的正整数"))
    # 5
    element = driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(5) .el-input__inner")
    actions = ActionChains(driver)
    actions.double_click(element).perform()
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(5) .el-input__inner").send_keys("0")
    driver.find_element(By.CSS_SELECTOR, "html").click()
    WebDriverWait(driver, 5).until(expected_conditions.text_to_be_present_in_element(
        (By.CSS_SELECTOR, ".el-form-item:nth-child(5) .el-form-item__error"), "请输入大于0的正整数"))
    # 提交
    driver.find_element(By.CSS_SELECTOR, ".el-button").click()
    WebDriverWait(driver, 5).until(
        expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".el-message__content"),
                                                          "请填写正确后再提交"))

