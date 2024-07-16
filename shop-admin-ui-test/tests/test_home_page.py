def test_show_stats(baseurl, driver):
    url = baseurl + "/home"
    # 访问页面
    driver.get(url)
    assert 1