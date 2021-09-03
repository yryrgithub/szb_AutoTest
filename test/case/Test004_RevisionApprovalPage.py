import unittest

from test.common.multiMenuOperation import MultiMenuOperation
from test.page.RevisionApprovalPage import RevisionApprovalPage


class TestRevisionApprovalPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.home = RevisionApprovalPage()
        cls.home.login_base()
        MultiMenuOperation(cls.home.driver).select_menu(menu_text='修改审批')

    @classmethod
    def tearDownClass(cls):
        cls.home.quit_page()

    def test_home01_search(self):
        self.home.search(customer_name='国信', approval_status='已通过')

    def test_home02_detail_operation(self):
        self.home.operation(header_text='1216623551877091328', row_text='详情', column_index=1)

    def test_home03_approval_operation(self):
        self.home.operation(header_text='1216623551877091328', row_text='审批', column_index=1)

    def test_home04_reject_operation(self):
        self.home.operation(header_text='1216623551877091328', row_text='驳回', column_index=1)