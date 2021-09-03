import time
import unittest
from ddt import ddt, data, unpack

from test.common.multiMenuOperation import MultiMenuOperation
from test.page.CustomerConfigPage import CustomerConfigPage
from utils.ExcelRead import ExcelRead


@ddt
class TestCustomerConfigPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.home = CustomerConfigPage()
        cls.home.login_base()
        MultiMenuOperation(driver=cls.home.driver).select_menu('客户配置')

    @classmethod
    def tearDownClass(cls):
        cls.home.quit_page()

    sheet = 'CustomerConfig'
    case = ExcelRead(sheet_name=sheet).get_case_account()

    def test_home00_add_button_click_check(self):
        self.home.add_button_click_check()

    @data(*case)
    @unpack
    def test_home01_add_customer_confirm(self, customer_id,computer_abbreviation, computer_name, customer_type,
                                         customer_status, pay_type, limit_item, money,
                                         RSA_key, ip_whitelist, customer_type2, customer_mark, sale, contact,
                                         email, limit_speed, bill_sender, mobile, is_reset, note,
                                         bill_fields, assert_type, assert_message):
        self.home.add_customers(customer_id, computer_abbreviation, computer_name, customer_type,
                                customer_status, pay_type, limit_item, money,
                                RSA_key, ip_whitelist, customer_type2, customer_mark, sale, contact,
                                email, limit_speed, bill_sender, mobile, is_reset, note,
                                bill_fields, '确认')
        self.home.add_customer_assert(assert_type, assert_message)
        time.sleep(2)

    def test_home02_pop(self):
        self.home.popup_close()

    def test_home03_add_customer_cancel(self):
        self.home.add_customers_button_assert('新增客户')
        self.home.add_customers(customer_id='test123', button="取消")
        time.sleep(2)

    def test_home04_search(self):
        self.home.search(customers_id='国信')
        time.sleep(2)

    def test_home05_refresh_cache(self):
        time.sleep(2)
        self.home.refresh_cache()

    def test_home06_detail_check(self):
        self.home.operation(header_text='bonc', row_text='详情', column_index=0)
        time.sleep(1)
        self.home.popup_close()
        time.sleep(1)

    def test_home07_modify(self):
        self.home.operation(header_text='bonc', row_text='修改', column_index=0)
        self.home.popup_close()
        time.sleep(1)

    def test_home08_permission_assignment(self):
        self.home.operation(header_text='bonc', row_text='权限分配', column_index=0)
        # self.home.popup_close()
        time.sleep(1)
