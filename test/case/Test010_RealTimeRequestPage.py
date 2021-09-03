import unittest

from test.page.RealTimeRequestPage import RealTimeRequestPage
from test.common.multiMenuOperation import MultiMenuOperation
from utils.readConfig import ReadConfig


class TestRealTimeRequestPage(unittest.TestCase):
    data = ReadConfig().get_account()
    report_path = data["report_path"]

    @classmethod
    def setUpClass(cls):
        cls.home = RealTimeRequestPage()
        cls.home.login_base()
        MultiMenuOperation(cls.home.driver).select_menu("实时调用")

    @classmethod
    def tearDownClass(cls):
        cls.home.quit_page()

    def test_home01_search1(self):
        self.home.select_customer_id('bonc')
        self.home.search()

    def test_home02_search2(self):
        self.home.select_customer_id('bonc', 'develop', 'ZXT')
        self.home.search()

    def test_home03_search3(self):
        self.home.select_customer_id('bonc')
        self.home.select_quota_id('MD002_3--手机号码在网时长')
        self.home.search()

    def test_home04_search4(self):
        self.home.select_customer_id('bonc', 'develop', 'ZXT')
        self.home.select_quota_id('MD002_3--手机号码在网时长', 'LT022_3--携号转网查询(联通)')
        self.home.search()

    def test_home05_search5(self):
        self.home.select_customer_id('bonc', 'develop', 'ZXT')
        self.home.select_quota_id('MD002_3--手机号码在网时长','LT022_3--携号转网查询(联通)')
        self.home.select_datasource_id('DS_GX002_3')
        self.home.search()

    def test_home06_search6(self):
        self.home.select_customer_id('bonc', 'develop', 'ZXT')
        self.home.select_quota_id('MD002_3--手机号码在网时长','LT022_3--携号转网查询(联通)')
        self.home.select_datasource_id('DS_GX002_3','DS_LT003')
        self.home.search()

    def test_home07_search7(self):
        self.home.search()

    def test_home08_download1(self):
        self.home.download_file(self.report_path)

    def test_home09_download2(self):
        self.home.select_customer_id('UMP')
        self.home.download_file(self.report_path)