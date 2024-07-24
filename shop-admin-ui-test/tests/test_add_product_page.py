import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_add_product_simple(baseurl, driver):
    driver.get(baseurl + "/pms/add-product")
    # NoSuchElementException 隐式等待
    driver.find_element(By.CSS_SELECTOR, ".el-cascader__label").click()
    driver.find_element(By.CSS_SELECTOR, ".el-cascader-menu__item:nth-child(1)").click()
    driver.find_element(By.XPATH, "//li[contains(.,\'冰箱\')]").click()

    # 商品名称 商品副标题
    timestamp = str(int(time.time()))
    product_name = "商品名称-" + timestamp
    product_subtitle = "商品副标题-" + timestamp

    driver.find_element(By.CSS_SELECTOR, ".is-required:nth-child(2) .el-input__inner").send_keys(product_name)
    driver.find_element(By.CSS_SELECTOR, ".is-required:nth-child(3) .el-input__inner").send_keys(product_subtitle)

    driver.find_element(By.CSS_SELECTOR, ".is-required .el-select .el-input__inner").click()
    driver.find_element(By.XPATH, "//li[contains(.,\'测试品牌9\')]").click()

    driver.find_element(By.CSS_SELECTOR,
                             ".el-form-item__content > .el-button--primary:nth-child(1) > span").click()
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(17) .el-button--primary > span").click()
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(6) .el-button--primary > span").click()
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(3) .el-button--primary").click()
    driver.find_element(By.CSS_SELECTOR, ".el-button--default:nth-child(2) > span").click()
    # 验证
    driver.get(baseurl + "/pms/product")
    first_row = WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".el-table__row:nth-child(1)")))
    assert product_name in first_row.text
    assert "测试品牌9" in first_row.text
    # 点击编辑
    driver.find_element(By.CSS_SELECTOR, ".el-table__row:nth-child(1) .el-button--default:nth-child(2)").click()
    WebDriverWait(driver, 5).until(
        expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".el-cascader__label"), "家用电器 / 冰箱"))

    value = driver.find_element(By.CSS_SELECTOR, ".is-required:nth-child(2) .el-input__inner").get_attribute(
        "value")
    assert value == product_name
    value = driver.find_element(By.CSS_SELECTOR, ".is-required:nth-child(3) .el-input__inner").get_attribute(
        "value")
    assert value == product_subtitle
    value = driver.find_element(By.CSS_SELECTOR, ".is-required .el-select .el-input__inner").get_attribute("value")
    assert value == "测试品牌9"
