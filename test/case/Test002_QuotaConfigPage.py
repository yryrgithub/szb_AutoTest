import time
import unittest

from test.common.multiMenuOperation import MultiMenuOperation
from test.page.QuotaConfigPage import QuotaConfigPage
from test.page.DatasourceCostPage import DatasourceCostPage


class TestQuotaConfigPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.home = QuotaConfigPage()
        cls.home.login_base()
        MultiMenuOperation(driver=cls.home.driver).select_menu('指标配置')

    @classmethod
    def tearDownClass(cls):
        cls.home.quit_page()

    def test_home01_search(self):
        self.home.search(customer_id='develop')
        time.sleep(2)

    def test_home02_modify_cancel(self):
        self.home.operation(header_text1='develop', header_text2='AI002', row_text='修改', column_index1=0,
                            column_index2=2)
        self.home.modify(button_text='取消')

    def test_home03_modify_confirm(self):
        self.home.operation(header_text1='develop', header_text2='AI002', row_text='修改', column_index1=0,
                            column_index2=2)
        self.home.modify(button_text='确认')

    def test_home04_refresh_cache(self):
        self.home.refresh_cache()
        time.sleep(2)
