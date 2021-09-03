import unittest

from test.page.BillManagementPage import BillManagementPage
from test.common.multiMenuOperation import MultiMenuOperation


class TestBillManagementPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.home = BillManagementPage()
        cls.home.login_base()
        MultiMenuOperation(cls.home.driver).select_menu('账单管理')

    @classmethod
    def tearDownClass(cls):
        cls.home.quit_page()

    def test_home01_bill_create_cancel(self):
        self.home.bill_create('2021-07-07', '2021-07-10', '202107', '取消')

    def test_home02_bill_create_confirm(self):
        self.home.bill_create('2021-07-07', '2021-07-10', '202107', '确定')

    def test_home03_detail(self):
        self.home.detail('jryzt', '201912')