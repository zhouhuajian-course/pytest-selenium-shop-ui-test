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


def pytest_html_report_title(report):
    report.title = "商城后台UI测试"
    pass


def pytest_html_results_summary(prefix: list, summary: list, postfix: list):
    prefix.extend(["<p>所属部门：某某部门</p>", "<p>测试人员：某某</p>"])
    summary.extend(["<h2>测试结果</h2>"])
    # postfix.extend(["<p>1111111111111</p>"])
    pass