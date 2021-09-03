import unittest

from test.page.CallDetailPage import CallDetailPage
from test.common.multiMenuOperation import MultiMenuOperation


class TestCallDetailPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.home = CallDetailPage()
        cls.home.login_base()
        MultiMenuOperation(cls.home.driver).select_menu('调用详情')

    @classmethod
    def tearDownClass(cls):
        cls.home.quit_page()

    def test_home01_condition_search_popup(self):
        self.home.condition_search_popup()

    def test_home02_condition_search(self):
        self.home.condition_search()

    def test_home03_call_detail_download(self):
        self.home.call_detail_download()
