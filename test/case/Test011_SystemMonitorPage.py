import unittest

from test.page.SystemMonitorPage import SystemMonitorPage
from test.common.multiMenuOperation import MultiMenuOperation


class TestSystemMonitorPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.home = SystemMonitorPage()
        cls.home.login_base()
        MultiMenuOperation(cls.home.driver).select_menu("系统监控")

    @classmethod
    def tearDownClass(cls):
        cls.home.quit_page()

    def test_home01_search1(self):
        self.home.search()

    def test_home02_search2(self):
        self.home.select_customer_id('bonc')
        self.home.search()

    def test_home03_search3(self):
        self.home.select_customer_id('bonc')
        self.home.select_quota_id('BLK05--数尊黑名单5')
        self.home.search()

    def test_home04_download1(self):
        self.home.download()

    def test_home05_download2(self):
        self.home.select_customer_id('bonc')
        self.home.download()

    def test_home06_download3(self):
        self.home.select_customer_id('bonc')
        self.home.select_quota_id('BLK05--数尊黑名单5')
        self.home.download()