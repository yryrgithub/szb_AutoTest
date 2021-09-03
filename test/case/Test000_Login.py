import unittest
from ddt import ddt, data, unpack

from test.page.LoginPage import LoginPage
from utils.ExcelRead import ExcelRead


@ddt
class TestLogin(unittest.TestCase):

    def setUp(self):
        self.login = LoginPage()

    def tearDown(self):
        self.login.quit_page()

    sheet = "Login"
    case = ExcelRead(sheet_name=sheet).get_case_account()
    @data(*case)
    @unpack
    def test_login(self, username, password, code, assert_type, assert_message):
        self.login.login_excel(username=username, password=password, code=code)
        self.login.assert_login_excel(assert_type=assert_type, assert_message=assert_message)
