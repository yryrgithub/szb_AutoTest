import unittest
from test.page.SampleReviewPage import SampleReviewPage
from test.common.multiMenuOperation import MultiMenuOperation


class TestSampleReviewPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.home = SampleReviewPage()
        cls.home.login_base()
        MultiMenuOperation(cls.home.driver).select_menu('样本复核')

    @classmethod
    def tearDownClass(cls):
        cls.home.quit_page()

    def test_home01_sample_search(self):
        self.home.sample_search('bonc_20210806111751')

    def test_home02_sample_search(self):
        self.home.sample_search('')

    def test_home03_reply(self):
        self.home.sample_reply('ksdkd', '', '取消')

    def test_home04_reply(self):
        self.home.sample_reply('sdkkf', '', '确定')

    def test_home05_upload_sample(self):
        self.home.upload_sample()

    def test_home06_download_sample(self):
        self.home.download_sample()
