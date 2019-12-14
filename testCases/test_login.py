# @Time    : 2019/12/12 10:53
# @Author  : Hugh
# @email   : 609799548@qq.com

import ddt
import unittest
from selenium import webdriver
from pageElement.login_page import LoginPage

data = [
    {'username': 'qiujiajin', 'password': '123456', 'except': '登录成功！'},
    {'username': 'qiujiajie', 'password': '123456', 'except': '用户不存在'},
    {'username': 'chenxiaojun', 'password': '12345678', 'except': '用户名或密码错误'}
]


@ddt.ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.page = LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def setUp(self) -> None:
        self.driver.get('http://hughjiajin.iicp.net/login.html')

    @ddt.data(*data)
    def test_login(self, d):
        """输入账号、密码， 点击登录"""
        self.page.send_username(d['username'])
        self.page.send_password(d['password'])
        self.page.click_login_button()
        t = self.page.get_alert_text()
        self.assertEqual(t, d['except'])


if __name__ == '__main__':
    unittest.main()