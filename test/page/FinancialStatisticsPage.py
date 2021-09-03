from test.page.LoginPage import LoginPage
from test.common.FinancialStatistics import FinancialStatistics


class FinancialStatisticsPage(LoginPage):

    def search(self):
        FinancialStatistics(self.driver).search()

    def download(self):
        FinancialStatistics(self.driver).download()
        # FinancialStatistics(self.driver).download_check()
