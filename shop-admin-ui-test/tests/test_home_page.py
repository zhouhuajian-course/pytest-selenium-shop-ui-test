import pytest


@pytest.mark.skip(reason="未实现，故跳过")
def test_show_stats(baseurl, driver):
    url = baseurl + "/home"
    # 访问页面
    driver.get(url)
    assert 1


def test_show_summary(baseurl, driver):
    assert 1