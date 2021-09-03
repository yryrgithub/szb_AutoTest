import unittest

from test.common.multiMenuOperation import MultiMenuOperation
from test.page.DataSourceConfigPage import DataSourcesConfigPage
from utils.ResultScreenshot import ResultScreenShot


class TestDataSourcesConfigPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.home = DataSourcesConfigPage()
        cls.home.login_base()
        MultiMenuOperation(driver=cls.home.driver).select_menu('数据源配置')

    @classmethod
    def tearDownClass(cls):
        cls.home.quit_page()

    # def test_home01_add_config_confirm(self):
    #     self.home.add_config(button='确认')

    def test_home02_add_config_cancel(self):
        self.home.add_config(button='取消')

    def test_home03_search(self):
        self.home.search(customer_id='develop', quota_id='RZ028')
        ResultScreenShot(driver=self.home.driver).get_screen_shot("TestDataSourcesConfigPage-search")

    def test_home04_edit_status_start_confirm(self):
        self.home.edit(button='确认', status='启用')
        ResultScreenShot(driver=self.home.driver).get_screen_shot("edit_status_start_confirm")

    # def test_home05_edit_status_start_cancel(self):
    #     self.home.edit(button='取消', status='启用')
    #     ResultScreenShot(driver=self.home.driver).get_screen_shot("edit_status_start_cancel")
    #
    # def test_home06_edit_status_stop_confirm(self):
    #     self.home.edit(button='确认', status='停用')
    #     ResultScreenShot(driver=self.home.driver).get_screen_shot("edit_status_stop_confirm")
    #
    # def test_home07_edit_status_stop_cancel(self):
    #     self.home.edit(button='取消', status='停用')
    #     ResultScreenShot(driver=self.home.driver).get_screen_shot("edit_status_stop_cancel")


if __name__ == '__main__':
    unittest.main()
