import unittest
from ddt import ddt, data, unpack

from test.page.MonitorConfigurationPage import MonitorConfigurationPage
from test.common.multiMenuOperation import MultiMenuOperation
from utils.ExcelRead import ExcelRead


@ddt
class TestMonitorConfigPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.home = MonitorConfigurationPage()
        cls.home.login_base()
        MultiMenuOperation(cls.home.driver).select_menu('监控配置')

    @classmethod
    def tearDownClass(cls):
        cls.home.quit_page()

    sheet = 'MonitorConfiguration'
    case = ExcelRead(sheet_name=sheet).get_case_account()

    @data(*case)
    @unpack
    def test_home01_add_monitor_config_confirm(self, monitor_id, monitor_name, clear_delay_time, clear_interval_time,
                                               calculate_delay_time, calculate_interval_time, data_retention_time,
                                               sms_interval_time, sms_interval_type, threshold_numbers,
                                               threshold_proportion, lasted_data, receiver_mobile, warming_information,
                                               assert_type, assert_message):
        self.home.add_monitor_configuration(monitor_id, monitor_name, clear_delay_time, clear_interval_time,
                                            calculate_delay_time, calculate_interval_time, data_retention_time,
                                            sms_interval_time,sms_interval_type, threshold_numbers, threshold_proportion,
                                            lasted_data, receiver_mobile, warming_information, '确定')
        self.home.add_monitor_configuration_assert(assert_type, assert_message)

    def test_home02_add_monitor_config_cancel(self):
        self.home.add_monitor_configuration('1', '1', 1, 1, 1, 1, 1, 1, '一般消息延迟间隔时间', 1, 1, 1, '12323456754', '1', '取消')

    def test_home03_modify_monitor_config_cancel(self):
        self.home.monitor_config_modify('222223', '1', '取消')

    def test_home04_modify_monitor_config_confirm(self):
        self.home.monitor_config_modify('222223', '1', '确定')

    def test_home05_delete_monitor_config_cancel(self):
        self.home.monitor_config_delete('1', '取消', '取消')

    def test_home06_delete_monitor_config_cancel(self):
        self.home.monitor_config_delete('1', '取消', '确定')

    def test_home07_delete_monitor_config_cancel(self):
        self.home.monitor_config_delete('1', '确定', '取消')

    # def test_home08_delete_monitor_config_confirm(self):
    #     self.home.monitor_config_delete('1', '确定', '确定')
