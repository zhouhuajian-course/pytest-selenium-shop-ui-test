import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_add_brand_then_delete(baseurl, driver):
    driver.get(baseurl + "/pms/brand")
    driver.find_element(By.CSS_SELECTOR, ".btn-add").click()

    brand_name = "brand-" + str(int(time.time()))
    driver.find_element(By.CSS_SELECTOR, ".is-required .el-input__inner").send_keys(brand_name)

    logo_path = os.path.abspath("./assets/logo.png")
    driver.find_element(By.NAME, "file").send_keys(logo_path)

    driver.find_element(By.CSS_SELECTOR,
                             ".el-form-item:nth-child(8) .el-radio:nth-child(1) .el-radio__inner").click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, ".el-form-item__content > .el-button--primary").click()
    driver.find_element(By.CSS_SELECTOR, ".el-button--small:nth-child(2)").click()
    # 验证
    driver.get(baseurl + "/pms/brand")
    driver.refresh()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".el-table__row:nth-child(1)")))
    assert driver.find_element(By.CSS_SELECTOR,
                                    ".el-table__row:nth-child(1) > .el-table_1_column_3 > .cell").text == brand_name
    assert driver.find_element(By.CSS_SELECTOR,
                                    ".el-table__row:nth-child(1) > .el-table_1_column_6 .el-switch__input").is_selected() is True
    assert driver.find_element(By.CSS_SELECTOR,
                                    ".el-table__row:nth-child(1) > .el-table_1_column_7 .el-switch__input").is_selected() is False
    # 删除
    driver.find_element(By.CSS_SELECTOR, ".el-table__row:nth-child(1) .el-button--danger > span").click()
    driver.find_element(By.CSS_SELECTOR, ".el-button--default:nth-child(2) > span").click()
    # 验证
    driver.refresh()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".el-table__row:nth-child(1)")))
    text = driver.find_element(By.CSS_SELECTOR, ".el-table__row:nth-child(1) > .el-table_1_column_3 > .cell").text
    assert text != brand_name