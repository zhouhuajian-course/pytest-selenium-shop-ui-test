# 测试环境 灰度环境 生产环境
def test_login_success(baseurl, driver):
    url = baseurl + "/login"
    driver.get(url)
    assert 1


def test_login_fail(baseurl, driver):
    url = baseurl + "/login"
    driver.get(url)
    assert 1