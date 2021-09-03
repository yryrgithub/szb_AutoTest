import time

from selenium.webdriver.common.by import By

from test.page.LoginPage import LoginPage
from test.common.multiMenuOperation import MultiMenuOperation
from test.common.TableOperation import TableOperation
from test.common.GetTips import GetTips


class RealTimeMonitorPage(LoginPage):

    def add_monitor_button_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"flex-box operate-left")]//button')

    def monitor_name_search_dropdown_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"flex-box operate-right")]//input')

    def monitor_search_button_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"flex-box operate-right")]//button')

    def add_monitor_id_dropdown_element(self):
        return self.find_element(By.XPATH,
                                 '//div[contains(@class,"el-dialog__body")]/form/div[1]/div[1]/div/div/div/div/input')

    def add_monitor_id_dropdown_message_element(self):
        return self.find_element(By.XPATH,
                                 '//div[contains(@class,"el-dialog__body")]/form/div[1]/div[1]/div/div/div[2]')

    def add_monitor_customer_id_dropdown_element(self):
        return self.find_element(By.XPATH,
                                 '//div[contains(@class,"el-dialog__body")]/form/div[1]/div[2]/div/div/div/div/input')

    def add_monitor_quota_id_dropdown_element(self):
        return self.find_element(By.XPATH,
                                 '//div[contains(@class,"el-dialog__body")]/form/div[2]/div[1]/div/div/div/div/input')

    def add_monitor_datasource_dropdown_id_element(self):
        return self.find_element(By.XPATH,
                                 '//div[contains(@class,"el-dialog__body")]/form/div[2]/div[2]/div/div/div/div/input')

    def add_monitor_errors_threshold_number_element(self):
        return self.find_element(By.XPATH,
                                 '//div[contains(@class,"el-dialog__body")]/form/div[3]/div[1]/div/div/div/input')

    def add_monitor_errors_threshold_number_message_element(self):
        return self.find_element(By.XPATH,
                                 '//div[contains(@class,"el-dialog__body")]/form/div[3]/div[1]/div/div/div[2]')

    def add_monitor_error_threshold_proportion_element(self):
        return self.find_element(By.XPATH,
                                 '//div[contains(@class,"el-dialog__body")]/form/div[3]/div[2]/div/div/div/input')

    def add_monitor_error_threshold_proportion_message_element(self):
        return self.find_element(By.XPATH,
                                 '//div[contains(@class,"el-dialog__body")]/form/div[3]/div[2]/div/div/div[2]')

    def add_monitor_cancel_button_element(self):
        return self.find_element(By.XPATH,
                                 '//div[contains(@class, "container-absolute")]/div/div/div[3]/div/div[3]/div/button[1]')

    def add_monitor_confirm_button_element(self):
        return self.find_element(By.XPATH,
                                 '//div[contains(@class, "container-absolute")]/div/div/div[3]/div/div[3]/div/button[2]')

    def monitor_delete_cancel_button_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-message-box__btns")]/button[1]')

    def monitor_delete_confirm_button_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-message-box__btns")]/button[2]')

    def pop_up_close(self):
        return self.find_element(By.XPATH, '//div[contains(@class, "container-absolute")]//div[3]/div/div[1]/button')

    def select_monitor_id(self, monitor_id):
        self.add_monitor_id_dropdown_element().click()
        time.sleep(1)
        self.find_element(By.XPATH, '//li//span[text()="{}"]'.format(monitor_id)).click()

    def select_monitor_customer_id(self, customer_id):
        self.add_monitor_customer_id_dropdown_element().click()
        time.sleep(1)
        self.find_element(By.XPATH, '//li//span[text()="{}"]'.format(customer_id)).click()

    def select_monitor_quota_id(self, quota_id):
        self.add_monitor_quota_id_dropdown_element().click()
        time.sleep(1)
        self.find_element(By.XPATH, '//li//span[text()="{}"]'.format(quota_id)).click()

    def select_monitor_datasource_id(self, datasource_id):
        self.add_monitor_datasource_dropdown_id_element().click()
        time.sleep(1)
        self.find_element(By.XPATH, '//li//span[text()="{}"]'.format(datasource_id)).click()

    def add_monitor(self, monitor_id, customer_id, quota_id, datasource_id, errors_threshold_number=None,
                    error_threshold_proportion=None, button=None):
        self.add_monitor_button_element().click()
        # self.select_monitor_id(monitor_id)
        # self.select_monitor_customer_id(customer_id)
        self.select_monitor_quota_id(quota_id)
        self.select_monitor_datasource_id(datasource_id)
        if errors_threshold_number != None:
            self.add_monitor_errors_threshold_number_element().clear()
            self.add_monitor_errors_threshold_number_element().send_keys(errors_threshold_number)
        if error_threshold_proportion != None:
            self.add_monitor_error_threshold_proportion_element().clear()
            self.add_monitor_error_threshold_proportion_element().send_keys(error_threshold_proportion)
        if button == '确定':
            self.add_monitor_confirm_button_element().click()
        elif button == '取消':
            self.add_monitor_cancel_button_element().click()
        else:
            print("只支持确定和取消功能")

    def add_monitor_assert(self, assert_type, assert_message):
        if assert_type == 'errors_threshold_number empty' or assert_type == 'errors_threshold_number error':
            errors_threshold_number_message = self.add_monitor_errors_threshold_number_message_element().text
            assert errors_threshold_number_message == assert_message
            self.pop_up_close().click()
        elif assert_type == 'error_threshold_proportion empty' or assert_type == 'error_threshold_proportion error':
            error_threshold_proportion_message = self.add_monitor_error_threshold_proportion_message_element().text
            assert error_threshold_proportion_message == assert_message
            self.pop_up_close().click()
        elif assert_type == 'monitor_id empyt':
            monitor_id_message = self.add_monitor_id_dropdown_message_element().text
            assert monitor_id_message == assert_message
            self.pop_up_close().click()
        elif assert_type == 'add fail':
            tips = GetTips(self.driver).get_tips()
            assert tips == assert_message
            self.pop_up_close().click()
        elif assert_type == 'add success':
            tips = GetTips(self.driver).get_tips()
            assert tips == assert_message
        else:
            print('断言类型错误！')

    def monitor_search(self, monitor_name):
        self.monitor_name_search_dropdown_element().click()
        self.find_element(By.XPATH, '//li/span[contains(text(),"{}")]'.format(monitor_name)).click()
        self.monitor_search_button_element().click()

    def monitor_modify(self, monitor_id, customer_id, button):
        time.sleep(1)
        TableOperation(self.driver).row_click_double(monitor_id, customer_id, '修改', 1, 2)
        if button == '取消':
            self.add_monitor_cancel_button_element().click()
        elif button == '确定':
            self.add_monitor_confirm_button_element().click()
        else:
            print("只能是取消或确定")

    def monitor_delete(self, monitor_id, customer_id, button):
        time.sleep(1)
        TableOperation(self.driver).row_click_double(monitor_id, customer_id, '删除', 1, 2)
        if button == '取消':
            self.monitor_delete_cancel_button_element().click()
        elif button == '确定':
            self.monitor_delete_confirm_button_element().click()
        else:
            print("只能是取消或确定")


if __name__ == '__main__':
    l = RealTimeMonitorPage()
    l.login_base()
    MultiMenuOperation(l.driver).select_menu("实时监控")
    # l.monitor_search('[指标]异常业务值_每分钟统计')
    l.add_monitor('[指标]异常业务值_每分钟统计', '数尊开发_测试', 'A0001', 'DS_A0001_1', '22', '0.11', '取消')
    # l.monitor_modify('[指标]异常业务值_每分钟统计', 'bonc')
    # l.monitor_delete('[指标]异常业务值_每分钟统计', 'bonc')
