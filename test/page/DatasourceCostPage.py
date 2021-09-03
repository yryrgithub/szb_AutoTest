import time

from selenium.webdriver.common.by import By

from test.page.LoginPage import LoginPage
from test.common.multiMenuOperation import MultiMenuOperation
from test.common.TableOperation import TableOperation
from test.common.GetTips import GetTips
from test.common.PopupClose import PopupClose

class DatasourceCostPage(LoginPage):
    def add_cost_button_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"operate-left")]/button')

    def datasource_id_dropdown_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"operate-right")]/span/div')

    def cost_search_button_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"operate-right")]/button')

    def add_datasource_id_dropdown_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[1]//input')

    def start_time_input_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[2]//input')

    def cost_input_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[3]//input')

    def charge_type_dropdown_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[4]//input')

    def note_input_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[5]//input')

    def add_datasource_id_dropdown_error_message_element(self):
        return self.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[1]/div/div/div/div[2]')

    def start_time_input_error_message_element(self):
        return self.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[2]/div/div/div/div[2]')

    def cost_input_error_message_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[3]//div[2]')

    def charge_type_dropdown_error_message_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[4]//div[2]')

    def note_input_error_message_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[5]//div[2]')

    def add_const_cancel_button_element(self):
        return self.find_element(By.XPATH,
                                 '//div[contains(@class,"default-container")]/div[2]//div[3]//div[3]//button[1]')

    def add_cost_confirm_button_element(self):
        return self.find_element(By.XPATH,
                                 '//div[contains(@class,"default-container")]/div[2]//div[3]//div[3]//button[2]')

    # def pop_up_close(self):
    #     return self.find_element(By.XPATH, '//div[contains(@class, "container-absolute")]//div[3]/div/div[1]/button')

    # def select_datasource_id(self):
    #     self.add_datasource_id_dropdown_element().click()
    #     self.find_element(By.XPATH, '//li/span[text()="DS_C0009_1"]').click()
    #
    # def input_start_time(self):
    #     self.start_time_input_element().clear()
    #     self.start_time_input_element().send_keys('2021-07-09')
    #
    # def input_cost(self):
    #     self.cost_input_element().clear()
    #     self.cost_input_element().send_keys('0.1')
    #
    # def select_charge_type(self):
    #     self.charge_type_dropdown_element().click()
    #     self.find_element(By.XPATH, '//li/span[text()="查得计费"]').click()
    #
    # def input_note(self):
    #     self.note_input_element().clear()
    #     self.note_input_element().send_keys('sdddff')

    def add_cost(self, datasourceID=None, start_time=None, cost=None, charge_type=None, note=None, button=None):
        self.add_cost_button_element().click()
        # if datasourceID != None:
        #     self.datasource_id_dropdown_element().click()
        #     self.find_element(By.XPATH, '//li/span[text()="{}"]'.format(datasourceID)).click()
        if start_time != None:
            self.start_time_input_element().clear()
            self.start_time_input_element().send_keys(start_time)
            self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[2]//label').click()
        if cost != None:
            self.cost_input_element().clear()
            self.cost_input_element().send_keys(cost)
        if charge_type != None:
            self.charge_type_dropdown_element().click()
            self.find_element(By.XPATH, '//li/span[text()="{}"]'.format(charge_type)).click()
        if note != None:
            self.note_input_element().clear()
            self.note_input_element().send_keys(note)
        if button == "取消":
            self.add_const_cancel_button_element().click()
        elif button == "确定":
            self.add_cost_confirm_button_element().click()
        else:
            print("只支持确定或取消功能")

    def add_cost_assert(self, assert_type, assert_message):
        if assert_type == 'add fail' or assert_type == 'datasourceID empty':
            datasource_id_error_message = self.add_datasource_id_dropdown_error_message_element().text
            assert datasource_id_error_message == assert_message
            PopupClose(self.driver).popup_close()
            time.sleep(1)
        elif assert_type == 'start_time error' or assert_type == 'start_time empty':
            start_time_error_message = self.start_time_input_error_message_element().text
            assert start_time_error_message == assert_message
            PopupClose(self.driver).popup_close()
            time.sleep(1)
        elif assert_type == 'cost empty' or assert_type == 'cost error':
            cost_error_message = self.cost_input_error_message_element().text
            assert cost_error_message == assert_message
            PopupClose(self.driver).popup_close()
            time.sleep(1)
        elif assert_type == 'charge_type empty':
            charge_type_error_message = self.charge_type_dropdown_error_message_element().text
            assert charge_type_error_message == assert_message
            PopupClose(self.driver).popup_close()
            time.sleep(1)
        elif assert_type == 'add success':
            tips = GetTips(self.driver).get_tips()
            assert tips == assert_message
        else:
            print("断言类型错误")

    def search_cost(self, datasource_id=None):
        if datasource_id != None:
            self.datasource_id_dropdown_element().click()
            self.cost_search_button_element().click()
        else:
            self.cost_search_button_element().click()

    def modify_cost(self, cost,charge_type,note, button):
        TableOperation(self.driver).row_click('DS_BLK02_1', '修改', 0)
        tip = GetTips(self.driver).get_tips()
        if tip == "只能修改最后一条数据源成本":
            print('请选择最后一条数据源成本进行修改')
        else:
            self.cost_input_element().send_keys(cost)
            self.find_element(By.XPATH, '//li/span[text()="{}"]'.format(charge_type)).click()
            self.note_input_element().send_keys(note)
        if button == "取消":
            self.add_const_cancel_button_element().click()
        elif button == "确定":
            self.add_cost_confirm_button_element().click()
        else:
            print("只支持确定或取消功能")


if __name__ == '__main__':
    l = DatasourceCostPage()
    l.login_base()
    MultiMenuOperation(l.driver).select_menu("数据源成本")
    l.add_cost('取消')
    l.add_cost('确认')
    # l.modify_cost('取消')
    # l.modify_cost('确定')
