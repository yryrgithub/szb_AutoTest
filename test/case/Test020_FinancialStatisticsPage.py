import unittest

from test.page.FinancialStatisticsPage import FinancialStatisticsPage
from test.common.FinancialStatistics import FinancialStatistics
from test.common.multiMenuOperation import MultiMenuOperation


class TestFinancialStatisticsPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.home = FinancialStatisticsPage()
        cls.home.login_base()
        MultiMenuOperation(cls.home.driver).select_menu('财务统计')

    @classmethod
    def tearDownClass(cls):
        cls.home.quit_page()

    def test_home01_search1(self):
        self.home.search()
        FinancialStatistics(self.home.driver).select_condition()

    def test_home01_search2(self):
        FinancialStatistics(self.home.driver).select_customer_id('develop')
        self.home.search()
        FinancialStatistics(self.home.driver).select_condition(customer_id='develop')

    def test_home01_search3(self):
        FinancialStatistics(self.home.driver).select_customer_id('develop', 'bonc')
        self.home.search()
        FinancialStatistics(self.home.driver).select_condition(customer_id='develop')

    def test_home01_search4(self):
        FinancialStatistics(self.home.driver).select_customer_id('develop', 'bonc')
        FinancialStatistics(self.home.driver).select_quota_id('MD001_1--手机号码当前状态')
        self.home.search()
        FinancialStatistics(self.home.driver).select_condition(customer_id='develop', quota_id='MD001_1')

    def test_home01_search5(self):
        FinancialStatistics(self.home.driver).select_customer_id('develop', 'bonc')
        FinancialStatistics(self.home.driver).select_quota_id('MD001_1--手机号码当前状态', 'MD004_3--姓名-身份证-手机号码(简)')
        self.home.search()
        FinancialStatistics(self.home.driver).select_condition(customer_id='develop', quota_id='MD001_1')

    def test_home01_search6(self):
        FinancialStatistics(self.home.driver).select_customer_id('develop', 'bonc')
        FinancialStatistics(self.home.driver).select_quota_id('MD001_1--手机号码当前状态', 'MD004_3--姓名-身份证-手机号码(简)')
        FinancialStatistics(self.home.driver).select_datasource_id('DS_SZTY_01')
        self.home.search()
        FinancialStatistics(self.home.driver).select_condition(customer_id='develop', quota_id='MD001_1',
                                                               datasource_id='DS_SZTY_01')

    def test_home01_search7(self):
        FinancialStatistics(self.home.driver).select_customer_id('develop', 'bonc')
        FinancialStatistics(self.home.driver).select_quota_id('MD001_1--手机号码当前状态', 'MD004_3--姓名-身份证-手机号码(简)')
        FinancialStatistics(self.home.driver).select_datasource_id('DS_SZTY_01', 'DS_GX004_3')
        self.home.search()
        FinancialStatistics(self.home.driver).select_condition(customer_id='develop', quota_id='MD001_1',
                                                               datasource_id='DS_SZTY_01')

    def test_home01_search8(self):
        MultiMenuOperation(self.home.driver).select_menu('财务统计')
        FinancialStatistics(self.home.driver).select_time(start_time='2018-07-02', end_time='2020-08-13')
        self.home.search()
        FinancialStatistics(self.home.driver).select_condition(start_time='2018-07-02')

    def test_home01_search9(self):
        FinancialStatistics(self.home.driver).select_customer_id('develop', 'bonc')
        FinancialStatistics(self.home.driver).select_quota_id('MD001_1--手机号码当前状态', 'MD004_3--姓名-身份证-手机号码(简)')
        FinancialStatistics(self.home.driver).select_datasource_id('DS_SZTY_01')
        FinancialStatistics(self.home.driver).select_time(start_time='2018-07-02', end_time='2020-08-13')
        self.home.search()
        FinancialStatistics(self.home.driver).select_condition(customer_id='develop', quota_id='MD001_1',
                                                               datasource_id='DS_SZTY_01', start_time='2018-07-02')

    def test_home02_download1(self):
        MultiMenuOperation(self.home.driver).select_menu('财务统计')
        self.home.download()
        FinancialStatistics(self.home.driver).select_condition()

    def test_home02_download2(self):
        FinancialStatistics(self.home.driver).select_customer_id('develop')
        self.home.download()
        FinancialStatistics(self.home.driver).select_condition(customer_id='develop')

    def test_home02_download3(self):
        FinancialStatistics(self.home.driver).select_customer_id('develop', 'bonc')
        self.home.download()
        # FinancialStatistics(self.home.driver).select_condition(customer_id='develop')

    def test_home02_download4(self):
        FinancialStatistics(self.home.driver).select_customer_id('develop', 'bonc')
        FinancialStatistics(self.home.driver).select_quota_id('MD001_1--手机号码当前状态')
        self.home.download()
        # FinancialStatistics(self.home.driver).select_condition(customer_id='develop', quota_id='MD001_1')

    def test_home02_download5(self):
        FinancialStatistics(self.home.driver).select_customer_id('develop', 'bonc')
        FinancialStatistics(self.home.driver).select_quota_id('MD001_1--手机号码当前状态', 'MD004_3--姓名-身份证-手机号码(简)')
        self.home.download()
        # FinancialStatistics(self.home.driver).select_condition(customer_id='develop', quota_id='MD001_1')

    def test_home02_download6(self):
        FinancialStatistics(self.home.driver).select_customer_id('develop', 'bonc')
        FinancialStatistics(self.home.driver).select_quota_id('MD001_1--手机号码当前状态', 'MD004_3--姓名-身份证-手机号码(简)')
        FinancialStatistics(self.home.driver).select_datasource_id('DS_SZTY_01')
        self.home.download()
        # FinancialStatistics(self.home.driver).select_condition(customer_id='develop', quota_id='MD001_1',datasource_id='DS_SZTY_01')

    def test_home02_download7(self):
        FinancialStatistics(self.home.driver).select_customer_id('develop', 'bonc')
        FinancialStatistics(self.home.driver).select_quota_id('MD001_1--手机号码当前状态', 'MD004_3--姓名-身份证-手机号码(简)')
        FinancialStatistics(self.home.driver).select_datasource_id('DS_SZTY_01', 'DS_GX004_3')
        self.home.download()
        # FinancialStatistics(self.home.driver).select_condition(customer_id='develop', quota_id='MD001_1',datasource_id='DS_SZTY_01')

    def test_home02_download8(self):
        FinancialStatistics(self.home.driver).select_time(start_time='2018-07-02', end_time='2020-08-13')
        self.home.download()
        # FinancialStatistics(self.home.driver).select_condition(start_time='2018-07-02')

    def test_home02_download9(self):
        FinancialStatistics(self.home.driver).select_customer_id('develop', 'bonc')
        FinancialStatistics(self.home.driver).select_quota_id('MD001_1--手机号码当前状态', 'MD004_3--姓名-身份证-手机号码(简)')
        FinancialStatistics(self.home.driver).select_datasource_id('DS_SZTY_01')
        FinancialStatistics(self.home.driver).select_time(start_time='2018-07-02', end_time='2020-08-13')
        self.home.download()
        # FinancialStatistics(self.home.driver).select_condition(customer_id='develop', quota_id='MD001_1',datasource_id='DS_SZTY_01', start_time='2018-07-02')



    # def test_home02_download1(self):
    #     self.home.download()
    #
    # def test_home02_download2(self):
    #     self.home.download()
