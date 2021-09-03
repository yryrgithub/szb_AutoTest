from test.common.HistoryRequest import HistoryRequest
from test.common.multiMenuOperation import MultiMenuOperation
from test.page.LoginPage import LoginPage


class HistoryRequestPage(LoginPage):

    # 客户ID下拉列表选择customer_id, *customers_id传入多个参数
    def select_customer_id(self, *customers_id):
        HistoryRequest(self.driver).select_customer_id(*customers_id)

    def select_quota_id(self, *quotas_id):
        HistoryRequest(self.driver).select_quota_id(*quotas_id)

    def select_datasource_id(self, *datasources_id):
        HistoryRequest(self.driver).select_datasource_id(*datasources_id)

    def select_time(self, start_time, end_time):
        HistoryRequest(self.driver).select_time(start_time, end_time)

    # 查询功能
    def search(self):
        HistoryRequest(self.driver).search()

    def history_request_download(self, report_path):
        HistoryRequest(self.driver).history_request_download(report_path)


if __name__ == '__main__':
    l = HistoryRequestPage()
    l.login_base()
    MultiMenuOperation(l.driver).select_menu("历史调用")
    # l.select_customer_id('bonc', 'ZXT')
    # l.select_quota_id('LT005--是否联通黑名单用户(联通)')
    # l.select_datasource_id('DS_LT005')
    # l.select_time('2021-02-01','2021-07-01')
    l.history_request_download('E:\\TestPython\\autoTestShuzunbao\\download')
    l.search()
