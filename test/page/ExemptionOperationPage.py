from selenium.webdriver.common.by import By

from test.page.LoginPage import LoginPage
from test.common.multiMenuOperation import MultiMenuOperation
from test.common.TableOperation import TableOperation
from test.common.GetTips import GetTips


class ExemptionOperationPage(LoginPage):
    def add_exemption_button_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"operate-left")]/button')

    def customer_id_dropdown_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[1]/div[1]//input')

    def exemption_quota_dropdown_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[1]/div[1]//input')

    def exemption_number_input_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[3]/div[1]//input')

    def price_input_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[3]/div[2]//input')

    def note_input_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[4]/div[1]//input')

    def add_const_cancel_button_element(self):
        return self.find_element(By.XPATH,
                                 '//div[contains(@class,"default-container")]/div[2]//div[3]//div[3]//button[1]')

    def add_exemption_confirm_button_element(self):
        return self.find_element(By.XPATH,
                                 '//div[contains(@class,"default-container")]/div[2]//div[3]//div[3]//button[2]')

    def select_customer_id(self):
        self.customer_id_dropdown_element().click()
        self.find_element(By.XPATH, '//li/span[text()="develop"]').click()

    def select_exemption_quota(self):
        self.exemption_quota_dropdown_element().click()
        self.find_element(By.XPATH, '//li/span[text()="BLK005"]').click()

    def input_exemption_number(self):
        self.exemption_number_input_element().clear()
        self.exemption_number_input_element().send_keys('2')

    def input_price(self):
        self.price_input_element().clear()
        self.price_input_element().send_keys('0.1')

    def input_note(self):
        self.note_input_element().clear()
        self.note_input_element().send_keys('sdddff')

    def add_exemption(self, button):
        self.add_exemption_button_element().click()
        self.input_exemption_number()
        self.input_price()
        self.input_note()
        if button == "取消":
            self.add_const_cancel_button_element().click()
        elif button == "确定":
            self.add_exemption_confirm_button_element().click()
        else:
            print("只支持确定或取消功能")

    def search_exemption(self):
        self.exemption_search_button_element().click()

    def modify_exemption(self, button):
        TableOperation(self.driver).row_click('DS_BLK02_1', '修改', 0)
        tip = GetTips(self.driver).get_tips()
        if tip == "只能修改最后一条数据源成本":
            print('请选择最后一条数据源成本进行修改')
        else:
            self.input_exemption()
            self.select_charge_type()
            self.input_note()
        if button == "取消":
            self.add_const_cancel_button_element().click()
        elif button == "确定":
            self.add_exemption_confirm_button_element().click()
        else:
            print("只支持确定或取消功能")


if __name__ == '__main__':
    l = ExemptionOperationPage()
    l.login_base()
    MultiMenuOperation(l.driver).select_menu("减免操作")
    l.add_exemption('取消')
    # l.add_exemption('确定')
    l.modify_exemption('取消')
    # l.modify_exemption('确定')
