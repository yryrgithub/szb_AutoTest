from selenium.webdriver.common.by import By

from test.page.LoginPage import LoginPage
from test.common.multiMenuOperation import MultiMenuOperation
from test.common.TableOperation import TableOperation
from test.common.GetTips import GetTips


class SalePricePage(LoginPage):
    def add_price_button_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"operate-left")]/button')

    def customer_id_dropdown_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"operate-right")]/span/div')

    def price_search_button_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"operate-right")]/button')

    def add_customer_id_dropdown_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[1]//input')

    def add_quota_id_dropdown_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[2]//input')

    def add_quota_type_dropdown_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[3]//input')

    def charge_type_dropdown_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[4]//input')

    def start_time_input_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[5]//input')

    def price_input_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[6]//input')

    def note_input_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[7]//input')

    def add_const_cancel_button_element(self):
        return self.find_element(By.XPATH,
                                 '//div[contains(@class,"default-container")]/div[2]//div[3]//div[3]//button[1]')

    def add_price_confirm_button_element(self):
        return self.find_element(By.XPATH,
                                 '//div[contains(@class,"default-container")]/div[2]//div[3]//div[3]//button[2]')

    def select_customer_id(self):
        self.add_customer_id_dropdown_element().click()
        self.find_element(By.XPATH, '//li/span[text()="develop"]').click()

    def input_start_time(self):
        self.start_time_input_element().clear()
        self.start_time_input_element().send_keys('2021-07-09')

    def input_price(self):
        self.price_input_element().clear()
        self.price_input_element().send_keys('0.1')

    def select_charge_type(self):
        self.charge_type_dropdown_element().click()
        self.find_element(By.XPATH, '//li/span[text()="查得计费"]').click()

    def input_note(self):
        self.note_input_element().clear()
        self.note_input_element().send_keys('sdddff')

    def add_price(self, button):
        self.add_price_button_element().click()
        self.input_price()
        self.input_note()
        if button == "取消":
            self.add_const_cancel_button_element().click()
        elif button == "确定":
            self.add_price_confirm_button_element().click()
        else:
            print("只支持确定或取消功能")

    def search_price(self):
        self.price_search_button_element().click()

    def modify_price(self, button):
        TableOperation(self.driver).row_click('188w_test', '修改', 0)
        tip = GetTips(self.driver).get_tips()
        if tip == "只能修改最后一条指标价格":
            print('请选择最后一条指标价格进行修改')
        else:
            self.input_price()
            self.select_charge_type()
            self.input_note()
        if button == "取消":
            self.add_const_cancel_button_element().click()
        elif button == "确定":
            self.add_price_confirm_button_element().click()
        else:
            print("只支持确定或取消功能")


if __name__ == '__main__':
    l = SalePricePage()
    l.login_base()
    MultiMenuOperation(l.driver).select_menu("销售价格")
    l.add_price('取消')
    l.add_price('确定')
    # l.modify_price('取消')
    # l.modify_price('确定')
