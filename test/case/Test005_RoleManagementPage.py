import unittest
from ddt import ddt, data, unpack

from test.common.multiMenuOperation import MultiMenuOperation
from test.page.RoleManagentPage import RoleManagementPage
from utils.ExcelRead import ExcelRead


@ddt
class TestRoleManagementPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.home = RoleManagementPage()
        cls.home.login_base()
        MultiMenuOperation(cls.home.driver).select_menu(menu_text='角色管理')

    @classmethod
    def tearDownClass(cls):
        cls.home.quit_page()

    sheet = "RoleManagement"
    case = ExcelRead(sheet_name=sheet).get_case_account()

    @data(*case)
    @unpack
    def test_home01_add_role_confirm(self, role_code, role_name, role_describe, assert_type, assert_message):
        self.home.add_role(role_code=role_code, role_name=role_name, role_describe=role_describe, role_status='锁定',
                           button='确定')
        self.home.add_role_assert(assert_type=assert_type, assert_message=assert_message)
        # self.home.add_role_check(role_name=role_name)

    @data(*case)
    @unpack
    def test_home02_add_role_confirm(self, role_code, role_name, role_describe, assert_type, assert_message):
        self.home.add_role(role_code=role_code, role_name=role_name, role_describe=role_describe, role_status='正常',
                           button='确定')
        self.home.add_role_assert(assert_type=assert_type, assert_message=assert_message)
        # self.home.add_role_check(role_name=role_name)

    def test_home03_add_role_cancel(self):
        self.home.add_role(role_code='test001', role_name='新增测试001', role_describe='新增测试001', role_status='正常',
                           button='取消')
        self.home.add_role_check(role_name='新增测试001')

    def test_home04_start_role(self):
        self.home.start_role(header_text='测试009', column_index=1)

    def test_home05_stop_role(self):
        self.home.stop_role(header_text='测试009', column_index=1)

    def test_home06_modify_role_confirm(self):
        self.home.modify_operation(role_name='修改001', role_describe='修改测试', role_status='锁定', header_text='test002',
                                   button='确定')

    def test_home07_modify_role_cancel(self):
        self.home.modify_operation(role_name='修改001', role_describe='修改测试', role_status='锁定', header_text='test002',
                                   button='取消')
