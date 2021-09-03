import unittest

from test.common.CustomerBill import CustomerBill
from test.page.CustomerBillPage import CustomerBillPage
from test.common.multiMenuOperation import MultiMenuOperation


class TestCustomerBillPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.home = CustomerBillPage()
        cls.home.login_base()
        MultiMenuOperation(cls.home.driver).select_menu('客户侧对账')

    @classmethod
    def tearDownClass(cls):
        cls.home.quit_page()

    def test_home01_search1(self):
        self.home.search()
        CustomerBill(self.home.driver).search_check()

    def test_home01_search2(self):
        self.home.input_time('2019-11-01', '2019-11-02')
        self.home.search()
        CustomerBill(self.home.driver).search_check('2019-11-01', '2019-11-02')
