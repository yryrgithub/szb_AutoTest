from test.common.multiMenuOperation import MultiMenuOperation
from test.page.LoginPage import LoginPage
from test.common.CustomerBill import CustomerBill


class CustomerBillPage(LoginPage):

    def search(self):
        CustomerBill(self.driver).search()

    def download_file(self):
        CustomerBill(self.driver).download_file()

    def input_time(self, start_time, end_time):
        CustomerBill(self.driver).start_time_input_element().send_keys(start_time)
        CustomerBill(self.driver).end_time_input_element().send_keys(end_time)



