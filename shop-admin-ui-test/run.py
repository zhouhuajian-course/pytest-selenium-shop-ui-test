import time

import pytest

if __name__ == '__main__':
    # pytest.main()
    # pytest.main(["./tests/test_login_page.py", "./tests/test_pms_add_product_page.py"])
    # pytest.main(["./tests/test_login_page.py", "./tests/test_pms_brand_page.py"])
    # pytest.main(["./tests/test_login_page.py", "./tests/test_oms_order_setting_page.py"])
    timestamp = str(int(time.time()))
    pytest.main([f"--html=./reports/report_{timestamp}.html", "--self-contained-html"])