import unittest

from test.page.CustomerChargingPage import CustomerChargingPage
from test.common.multiMenuOperation import MultiMenuOperation


class TestCustomerChargingPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.home = CustomerChargingPage()
        cls.home.login_base()
        MultiMenuOperation(cls.home.driver).select_menu('客户充值')

    @classmethod
    def tearDownClass(cls):
        cls.home.quit_page()

    def test_home01_charging_cancel(self):
        self.home.add_charging('取消')

