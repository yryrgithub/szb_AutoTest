import unittest

from test.page.DataAuthorityPage import DataAuthorityPage
from test.common.multiMenuOperation import MultiMenuOperation


class TestDataAuthorityPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.home = DataAuthorityPage()
        cls.home.login_base()
        MultiMenuOperation(cls.home.driver).select_menu("数据权限")

    @classmethod
    def tearDownClass(cls):
        cls.home.quit_page()

    def test_home01_authority_config(self):
        pass

    def test_home02_search(self):
        self.home.search(user_id='bonc', customer_id='bonc')




