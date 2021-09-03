import unittest
from ddt import ddt, data, unpack

from test.page.DatasourceCostPage import DatasourceCostPage
from test.common.multiMenuOperation import MultiMenuOperation
from utils.ExcelRead import ExcelRead

@ddt
class TestDatasourceCostPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.home = DatasourceCostPage()
        cls.home.login_base()
        MultiMenuOperation(cls.home.driver).select_menu('数据源成本')

    @classmethod
    def tearDownClass(cls):
        cls.home.quit_page()

    sheet = 'DatasourceCost'
    case = ExcelRead(sheet_name=sheet).get_case_account()

    @data(*case)
    @unpack
    def test_home01_add_cost_confirm(self, datasourceID, start_time, cost, charge_type, note, assert_type, assert_message):
        self.home.add_cost(datasourceID, start_time, cost, charge_type, note, '确定')
        self.home.add_cost_assert(assert_type, assert_message)

    # def test_home02_add_cost_cancel(self):
    #     self.home.add_cost('取消')
    #
    # def test_home03_search(self):
    #     self.home.search_cost()
    #
    # def test_home04_search_with_datasource(self):
    #     self.home.search_cost('DS_A0001_1')
    #
    # def test_home05_modify_cost_cancel(self):
    #     self.home.modify_cost('取消')
    #
    # def test_home06_modify_cost_confirm(self):
    #     self.home.modify_cost('确定')
