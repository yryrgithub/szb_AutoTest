import unittest
from ddt import ddt, data, unpack

from test.page.RealTimeMonitorPage import RealTimeMonitorPage
from test.common.multiMenuOperation import MultiMenuOperation
from utils.ExcelRead import ExcelRead


@ddt
class TestRealTimeMonitorPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.home = RealTimeMonitorPage()
        cls.home.login_base()
        MultiMenuOperation(cls.home.driver).select_menu('实时监控')

    @classmethod
    def tearDownClass(cls):
        cls.home.quit_page()

    sheet = "RealTimeMonitor"
    case = ExcelRead(sheet_name=sheet).get_case_account()

    @data(*case)
    @unpack
    def test_home01_add_real_time_monitor_cancel(self, monitor_id, customer_id, quota_id, datasource_id,
                                                 errors_threshold_number, error_threshold_proportion, assert_type,
                                                 assert_message):
        self.home.add_monitor(monitor_id, customer_id, quota_id, datasource_id, errors_threshold_number,
                              error_threshold_proportion, '确定')
        self.home.add_monitor_assert(assert_type, assert_message)

    def test_home02_add_real_time_monitor_confirm(self):
        self.home.add_monitor('[指标]异常业务值_每分钟统计', '数尊开发_测试', 'A0001', 'DS_A0001_1', '22', '0.11', '取消')

    # def test_home02_search_monitor(self):
    #     self.home.monitor_search('3')

    def test_home03_modify_real_time_monitor_cancel(self):
        self.home.monitor_modify('[客户]查询失败率_近百条统计', 'mogujie', '取消')

    def test_home04_modify_real_time_monitor_confirm(self):
        self.home.monitor_modify('[客户]查询失败率_近百条统计', 'mogujie', '确定')

    def test_home05_delete_real_time_monitor_cancel(self):
        self.home.monitor_delete('[客户]查询失败率_近百条统计', 'mogujie', '取消')

    # def test_home06_delete_real_time_monitor_cancel(self):
    #     self.home.monitor_delete('[客户]查询失败率_近百条统计', 'shoufuyou', '确定')
    def test_home06_download_file(self):
        self.home
