from selenium.webdriver.common.by import By

from test.page.LoginPage import LoginPage
from test.common.TableOperation import TableOperation
from test.common.multiMenuOperation import MultiMenuOperation
from test.common.BillManagement import BillManagement


class BillManagementPage(LoginPage):

    def bill_create(self, start_time, end_time, bill_name, button):
        BillManagement(self.driver).bill_create()
        BillManagement(self.driver).bill_start_time_input(start_time)
        BillManagement(self.driver).bill_end_time_input(end_time)
        BillManagement(self.driver).add_bill_name_input(bill_name)
        BillManagement(self.driver).add_bill_button(button)

    def bill_search(self, customer_id, bill_name):
        BillManagement(self.driver).select_customer_id_dropdown_element().click()
        BillManagement(self.driver).select_bill_name_element().sed_keys(bill_name)
        BillManagement(self.driver).search_button_element().click()

    def detail(self, customer_id, bill_name):
        TableOperation(self.driver).row_click_double(customer_id, bill_name, '详情', 1, 4)
        BillManagement(self.driver).detail_cancel_button_element().click()


if __name__ == '__main__':
    l = BillManagementPage()
    l.login_base()
    MultiMenuOperation(l.driver).select_menu("账单管理")
    l.bill_create()
    l.search_button_element()
    l.detail('jryzt', '201912')










