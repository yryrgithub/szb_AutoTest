import unittest

from ddt import data, ddt, unpack

from test.common.multiMenuOperation import MultiMenuOperation
from test.page.UserManagementPage import UserManagementPage
from utils.ExcelRead import ExcelRead


@ddt
class TestUserManagementPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.home = UserManagementPage()
        cls.home.login_base()
        MultiMenuOperation(cls.home.driver).select_menu(menu_text='用户管理')

    @classmethod
    def tearDownClass(cls):
        cls.home.quit_page()

    sheet = "UserManagement"
    case = ExcelRead(sheet_name=sheet).get_case_account()

    @data(*case)
    @unpack
    def test_home01_add_user(self, userid, belonger, mobile, email, password, assert_type, assert_message):
        self.home.add_user(userid=userid, belonger=belonger, mobile=mobile, email=email, password=password, status='锁定',
                           button='确定')
        self.home.add_user_assert(assert_type=assert_type, assert_message=assert_message)

    def test_home02_search_user(self):
        self.home.search_user("rui.yang")

    def test_home03_modify_user(self):
        self.home.modify_user(belonger='admin2', mobile='13333300001', email='rui.yang@shuzun.net', status='正常', button='确定')

