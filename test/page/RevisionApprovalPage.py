import time

from py import log
from selenium.webdriver.common.by import By

from test.common.DropdownOperation import DropdownOperation
from test.common.TableOperation import TableOperation
from test.common.multiMenuOperation import MultiMenuOperation
from test.page.LoginPage import LoginPage


class RevisionApprovalPage(LoginPage):

    def customer_name_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class, "operate-right")]/div[1]/input')

    def approval_status_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class, "el-select--small")]/div[1]/input')

    def search_element(self):
        return self.find_element(By.XPATH, '//i[contains(@class, "el-icon-search")]')

    def detail_cancel_button_element(self):
        return self.find_element(By.XPATH,
                                 '//div[contains(@class, "container-absolute")]/div/div/div[3]/div/div[3]/div/button/span')

    # def approval_status_element1(self):
    #     return self.find_element(By.XPATH, '//li/*[contains(text(), "待审核")]')

    def search(self, customer_name, approval_status):
        self.customer_name_element().send_keys(customer_name)
        self.approval_status_element().click()
        # self.find_element(By.XPATH, '//i[contains(@class, "el-icon-circle-close")]').click()
        DropdownOperation(self.driver).select_dropdown(approval_status)
        time.sleep(1)
        self.search_element().click()

    def operation(self, header_text, row_text, column_index):
        TableOperation(self.driver).row_click(header_text=header_text, row_text=row_text, column_index=column_index)
        time.sleep(2)
        if row_text == '详情':
            detail_text = self.find_element(By.XPATH,
                                            '//div[contains(@class, "container-absolute")]/div/div/div[3]/div/div[1]/span').text
            assert detail_text == '详情'
            self.detail_cancel_button_element().click()
        elif row_text == '审批':
            pass
        elif row_text == '驳回':
            pass
        else:
            print("操作功能只能是详情，审批，或驳回")


if __name__ == '__main__':
    l = RevisionApprovalPage()
    l.login_base()
    MultiMenuOperation(l.driver).select_menu('修改审批')
    time.sleep(2)
    l.search(customer_name='国信', approval_status='已通过')
    # l.operation(header_text='1215570478505267200', row_text='详情', column_index=1)
    # l.operation(header_text='1215570478505267200', row_text='驳回', column_index=1)
