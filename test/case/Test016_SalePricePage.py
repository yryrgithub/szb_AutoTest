import unittest

from test.page.SalePricePage import SalePricePage
from test.common.multiMenuOperation import MultiMenuOperation


class TestSalePricePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.home = SalePricePage()
        cls.home.login_base()
        MultiMenuOperation(cls.home.driver).select_menu('销售价格')

    @classmethod
    def tearDownClass(cls):
        cls.home.quit_page()

    def test_home01_add_price_cancel(self):
        self.home.add_price('取消')

    def test_home02_add_price_confirm(self):
        self.home.add_price('确定')

    def test_home03_search(self):
        self.home.search_price()

    def test_home04_search(self):
        pass

    def test_home05_modify_cancel(self):
        self.home.modify_price('取消')

    def test_home06_modify_confirm(self):
        self.home.modify_price('确定')
