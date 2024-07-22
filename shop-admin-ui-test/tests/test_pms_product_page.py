from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_search_by_product_name(baseurl, driver):
    driver.get(baseurl + "/pms/product")
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(1) .el-input__inner").send_keys("TEST-测试电视")
    driver.find_element(By.CSS_SELECTOR, ".el-button--primary:nth-child(3)").click()
    trs = driver.find_elements(By.CSS_SELECTOR, "tbody > tr")
    for tr in trs:
        assert "TEST-测试电视" in tr.text


def test_search_by_product_serial_number(baseurl, driver):
    driver.get(baseurl + "/pms/product")
    driver.refresh()
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(2) .el-input__inner").send_keys(
        "TEST-1010101010")
    driver.find_element(By.CSS_SELECTOR, ".el-button--primary:nth-child(3) > span").click()
    WebDriverWait(driver, 5).until(
        expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".el-pagination__total"), "共 1 条"))
    WebDriverWait(driver, 5).until(
        expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".el-table_1_column_5 p:nth-child(2)"),
                                                          "货号：TEST-1010101010"))

