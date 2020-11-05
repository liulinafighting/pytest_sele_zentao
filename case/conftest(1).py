import pytest
from page.login_page import _login

"""
case/conftest.py文件
** 作者：上海-悠悠 QQ交流群：874033608**
登录功能调用
"""

@pytest.fixture(scope='session')
def login(driver, host):
    """登录功能fixture"""
    _login(driver, host)
