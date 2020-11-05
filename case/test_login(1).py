# coding:utf-8
import pytest
import time
from page.login_page import _login_result, _login, _get_alert

"""
case/test_login.py文件
** 作者：上海-悠悠 QQ交流群：874033608**
"""

class TestLogin():

    @pytest.fixture(scope="function",  autouse=True)
    def startPaget(self, driver, host):
        print("---让每个用例都从登录首页开始:---start!---")
        driver.get(host+"/zentao/user-login.html")
        driver.delete_all_cookies()
        driver.refresh()

    def test_login_fail(self, driver, host):
        """禅道-登录失败案例：admin111-111111"""
        _login(driver, host, "admin111", "111111")
        result1 = _get_alert(driver)
        print("测试结果：%s" % result1)
        assert "登录失败" in result1

    def test_login_pass(self, driver, host):
        '''禅道-登录成功案例'''
        _login(driver, host, "admin", "123456")
        result2 = _login_result(driver, "admin")
        print("登录结果：%s" % result2)
        assert result2

if __name__ == "__main__":
    pytest.main(["-s", "test_login.py"])