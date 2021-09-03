import time

from selenium.webdriver.common.by import By

from test.common.PopupClose import PopupClose
from test.page.LoginPage import LoginPage
from test.common.TableOperation import TableOperation
from test.common.multiMenuOperation import MultiMenuOperation
from test.common.GetTips import GetTips


class MonitorConfigurationPage(LoginPage):

    def add_config_button_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"flex-box operate-left")]/button')

    def monitor_id_input_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[1]/div[1]//input')

    def monitor_name_input_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[1]/div[2]//input')

    def clear_delay_time_input_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[2]/div[1]//input')

    def clear_interval_time_input_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[2]/div[2]//input')

    def calculate_delay_time_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[3]/div[1]//input')

    def calculate_interval_time_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[3]/div[2]//input')

    def data_retention_time_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[4]/div[1]//input')

    def sms_interval_time_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[4]/div[2]//input')

    def sms_interval_type_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[5]/div[1]//input')

    def threshold_numbers_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[5]/div[2]//input')

    def threshold_proportion_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[6]/div[1]//input')

    def lasted_data_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[6]/div[2]//input')

    def receiver_mobile_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[7]/div[1]//input')

    def warming_information_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[7]/div[2]//input')

    def monitor_id_input_error_message_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[1]/div[1]//div[2]')

    def monitor_name_input_error_message_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[1]/div[2]//div[2]')

    def clear_delay_time_input_error_message_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[2]/div[1]//div[2]')

    def clear_interval_time_input_error_message_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[2]/div[2]//div[2]')

    def calculate_delay_time_error_message_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[3]/div[1]//div[2]')

    def calculate_interval_time_error_message_element(self):
        return self.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[3]/div[2]/div/div/div[2]')

    def data_retention_time_error_message_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[4]/div[1]//div[2]')

    def sms_interval_time_error_message_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[4]/div[2]//div[2]')

    def sms_interval_type_element_error_message_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[5]/div[1]//div[2]')

    def threshold_numbers_error_message_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[5]/div[2]//div[2]')

    def threshold_proportion_error_message_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[6]/div[1]//div[2]')

    def lasted_data_error_message_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[6]/div[2]//div[2]')

    def receiver_mobile_error_message_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[7]/div[1]//div[2]')

    def warming_information_error_message_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[7]/div[2]//div[2]')

    def add_monitor_config_cancel_button_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"container-absolute")]//div[3]//div[3]//button[1]')

    def add_monitor_config_confirm_button_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"container-absolute")]//div[3]//div[3]//button[2]')

    def delete_monitor_config_cancel_button_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-message-box__btns")]/button[1]')

    def delete_monitor_config_confirm_button_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-message-box__btns")]/button[2]')

    def add_monitor_configuration(self, monitor_id=None, monitor_name=None, clear_delay_time=None,
                                  clear_interval_time=None,
                                  calculate_delay_time=None, calculate_interval_time=None, data_retention_time=None,
                                  sms_interval_time=None,
                                  sms_interval_type=None, threshold_numbers=None, threshold_proportion=None,
                                  lasted_data=None, receiver_mobile=None,
                                  warming_information=None, button=None):
        self.add_config_button_element().click()
        if monitor_id != None:
            self.monitor_id_input_element().clear()
            self.monitor_id_input_element().send_keys(monitor_id)
        if monitor_name != None:
            self.monitor_name_input_element().clear()
            self.monitor_name_input_element().send_keys(monitor_name)
        if clear_delay_time != None:
            self.clear_delay_time_input_element().clear()
            self.clear_delay_time_input_element().send_keys(clear_delay_time)
        if clear_interval_time != None:
            self.clear_interval_time_input_element().clear()
            self.clear_interval_time_input_element().send_keys(clear_interval_time)
        if calculate_delay_time != None:
            self.calculate_delay_time_element().clear()
            self.calculate_delay_time_element().send_keys(calculate_delay_time)
        if calculate_interval_time != None:
            self.calculate_interval_time_element().clear()
            self.calculate_interval_time_element().send_keys(calculate_interval_time)
        if data_retention_time != None:
            self.data_retention_time_element().clear()
            self.data_retention_time_element().send_keys(data_retention_time)
        if sms_interval_time != None:
            self.sms_interval_time_element().clear()
            self.sms_interval_time_element().send_keys(sms_interval_time)
        if sms_interval_type != None:
            self.sms_interval_type_element().click()
            self.find_element(By.XPATH, '//li/span[text()="{}"]'.format(sms_interval_type)).click()
        if threshold_numbers != None:
            self.threshold_numbers_element().clear()
            self.threshold_numbers_element().send_keys(threshold_numbers)
        if threshold_proportion != None:
            self.threshold_proportion_element().clear()
            self.threshold_proportion_element().send_keys(threshold_proportion)
        if lasted_data != None:
            self.lasted_data_element().clear()
            self.lasted_data_element().send_keys(lasted_data)
        if receiver_mobile != None:
            self.receiver_mobile_element().clear()
            self.receiver_mobile_element().send_keys(receiver_mobile)
        if warming_information != None:
            self.warming_information_element().clear()
            self.warming_information_element().send_keys(warming_information)
        if button == "确定":
            self.add_monitor_config_confirm_button_element().click()
            time.sleep(1)
        elif button == "取消":
            self.add_monitor_config_cancel_button_element().click()
            time.sleep(1)
        else:
            print("只支持确定或取消功能")

    def add_monitor_configuration_assert(self, assert_type, assert_message):
        if assert_type == 'monitor_id empty' or assert_type == 'monitor_id error':
            monitor_id_error_message = self.monitor_id_input_error_message_element().text
            assert monitor_id_error_message == assert_message
            PopupClose(self.driver).popup_close()
            time.sleep(1)
        elif assert_type == 'clear_delay_time empty' or assert_type == 'clear_delay_time error':
            clear_delay_time_error_message = self.clear_delay_time_input_error_message_element().text
            assert clear_delay_time_error_message == assert_message
            PopupClose(self.driver).popup_close()
            time.sleep(1)
        elif assert_type == 'clear_interval_time empty' or assert_type == 'clear_interval_time error':
            clear_interval_time_error_message = self.clear_interval_time_input_error_message_element().text
            assert clear_interval_time_error_message == assert_message
            PopupClose(self.driver).popup_close()
            time.sleep(1)
        elif assert_type == 'calculate_delay_time empty' or assert_type == 'calculate_delay_time error':
            calculate_delay_time_error_message = self.calculate_delay_time_error_message_element().text
            assert calculate_delay_time_error_message == assert_message
            PopupClose(self.driver).popup_close()
            time.sleep(1)
        elif assert_type == 'calculate_interval_time empty' or assert_type == 'calculate_interval_time error':
            calculate_interval_time_error_message = self.calculate_interval_time_error_message_element().text
            assert calculate_interval_time_error_message == assert_message
            PopupClose(self.driver).popup_close()
            time.sleep(1)
        elif assert_type == 'data_retention_time empty' or assert_type == 'data_retention_time error':
            data_retention_time_error_message = self.data_retention_time_error_message_element().text
            assert data_retention_time_error_message == assert_message
            PopupClose(self.driver).popup_close()
            time.sleep(1)
        elif assert_type == 'sms_interval_time empty' or assert_type == 'sms_interval_time error':
            sms_interval_time_time_error_message = self.sms_interval_time_error_message_element().text
            assert sms_interval_time_time_error_message == assert_message
            PopupClose(self.driver).popup_close()
            time.sleep(1)
        elif assert_type == 'threshold_numbers empty' or assert_type == 'threshold_numbers error':
            threshold_numbers_time_error_message = self.threshold_numbers_error_message_element().text
            assert threshold_numbers_time_error_message == assert_message
            PopupClose(self.driver).popup_close()
            time.sleep(1)
        elif assert_type == 'threshold_proportion empty' or assert_type == 'threshold_proportion error':
            threshold_proportion_error_message = self.threshold_proportion_error_message_element().text
            assert threshold_proportion_error_message == assert_message
            PopupClose(self.driver).popup_close()
            time.sleep(1)
        elif assert_type == 'lasted_data empty' or assert_type == 'lasted_data error':
            lasted_data_error_message = self.lasted_data_error_message_element().text
            assert lasted_data_error_message == assert_message
            PopupClose(self.driver).popup_close()
            time.sleep(1)
        elif assert_type == 'receiver_mobile empty':
            receiver_mobile_error_messsage = self.receiver_mobile_error_message_element().text
            assert receiver_mobile_error_messsage == assert_message
            PopupClose(self.driver).popup_close()
            time.sleep(1)
        elif assert_type == 'sms_interval_type empty':
            sms_interval_type_error_messsage = self.sms_interval_type_element_error_message_element().text
            assert sms_interval_type_error_messsage == assert_message
            PopupClose(self.driver).popup_close()
            time.sleep(1)
        elif assert_type == 'warming_information empty':
            warming_information_error_message = self.warming_information_error_message_element().text
            assert warming_information_error_message == assert_message
            PopupClose(self.driver).popup_close()
            time.sleep(1)
        elif assert_type == 'monitor_name empty':
            monitor_name_error_message = self.monitor_name_input_error_message_element().text
            assert monitor_name_error_message == assert_message
            PopupClose(self.driver).popup_close()
            time.sleep(1)
        elif assert_type == 'add success':
            tips = GetTips(self.driver).get_tips()
            assert tips == assert_message
        elif assert_type == 'add fail':
            tips = GetTips(self.driver).get_tips()
            assert tips == assert_message
            PopupClose(self.driver).popup_close()
            time.sleep(1)
        else:
            print('断言类型错误')

    def monitor_config_modify(self, monitor_id, monitor_name, button):
        TableOperation(self.driver).row_click(monitor_id, '修改', 0)
        self.threshold_numbers_element().clear()
        self.threshold_numbers_element().send_keys(monitor_name)
        if button == "取消":
            self.add_monitor_config_cancel_button_element().click()
        elif button == "确定":
            self.add_monitor_config_confirm_button_element().click()
        else:
            print("只支持确定或取消功能")

    def monitor_config_delete(self, monitor_id, button1, button2):
        TableOperation(self.driver).row_click(monitor_id, '删除', 0)
        if button1 == "取消":
            self.delete_monitor_config_cancel_button_element().click()
        elif button1 == "确定":
            self.delete_monitor_config_confirm_button_element().click()
            if button2 == "取消":
                self.delete_monitor_config_cancel_button_element().click()
            elif button2 == "确定":
                self.delete_monitor_config_confirm_button_element().click()
                tip_message = GetTips(self.driver).get_tips()
                if tip_message == "删除成功!":
                    print('%s:监控配置删除成功' % monitor_id)
                else:
                    print('%s:监控配置删除失败' % monitor_id)
            else:
                print("只支持确定或取消功能")
        else:
            print("只支持确定或取消功能")


if __name__ == '__main__':
    l = MonitorConfigurationPage()
    l.login_base()
    MultiMenuOperation(l.driver).select_menu("监控配置")
    l.add_monitor_configuration('', '1', 1, 1, 1, 1, 1, 1, '一般消息延迟间隔时间', 1, 1, 1, '12323456754', '1', '确定')
    # l.monitor_config_modify('222223', '1', '确定')
    # l.monitor_config_delete('22', '确定', '确定')
    l.add_monitor_configuration_assert('monitor_id empty','不能为空')
