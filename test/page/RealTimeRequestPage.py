import os

from test.common.RealTimeRequest import RealTimeRequest
from test.page.LoginPage import LoginPage


class RealTimeRequestPage(LoginPage):

    # 下拉列表中选择客户ID
    def select_customer_id(self, *customers_id):
        RealTimeRequest(self.driver).select_customer_id(*customers_id)

    # 下拉列表中选择指标IDs
    def select_quota_id(self, *quotas_id):
        RealTimeRequest(self.driver).select_quota_id(*quotas_id)

    # 下拉列表中选择数据源ID
    def select_datasource_id(self, *datasources_id):
        RealTimeRequest(self.driver).select_datasource_id(*datasources_id)

    def select_date(self):
        RealTimeRequest(self.driver).select_date()

    def download_file(self, report_path):
        RealTimeRequest(self.driver).real_time_request_file_download(report_path)


    # 实现查询功能
    def search(self):
        RealTimeRequest(self.driver).search()


if __name__ == '__main__':
    l = RealTimeRequestPage()
    p = "E:\\TestPython\\autoTestShuzunbao\\download\\"
    l.download_file()
