import unittest

from test.page.ExemptionOperationPage import ExemptionOperationPage
from test.common.multiMenuOperation import MultiMenuOperation


class TestExemptionOperationPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.home = ExemptionOperationPage()
        cls.home.login_base()
        MultiMenuOperation(cls.home.driver).select_menu('减免操作')

    @classmethod
    def tearDownClass(cls):
        cls.home.quit_page()

    def test_home01_add_exemption_cancel(self):
        self.home.add_exemption('取消')

    def test_home02_add_exemption_confirm(self):
        self.home.add_exemption('确定')

