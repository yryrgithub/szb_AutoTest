from selenium.webdriver.common.by import By

from test.common.PopupClose import PopupClose

class BillManagement():

    def __init__(self, driver):
        self.driver = driver

    def bill_create_element(self):
        return self.driver.find_element(By.XPATH, '//div[contains(@class,"operate-left")]/button[1]')

    def bill_download_button_element(self):
        return self.driver.find_element(By.XPATH, '//div[contains(@class,"operate-left")]/button[2]')

    def bill_repeal_button_element(self):
        return self.driver.driver.find_element(By.XPATH, '//div[contains(@class,"operate-left")]/button[3]')

    def select_customer_id_dropdown_element(self):
        return self.driver.find_element(By.XPATH, '//div[contains(@class,"operate-right")]/span/div//input')

    def select_bill_name_element(self):
        return self.driver.find_element(By.XPATH, '//div[contains(@class,"operate-right")]/div//input')

    def search_button_element(self):
        return self.driver.find_element(By.XPATH, '//div[contains(@class,"operate-right")]/button')

    def bill_create_cancel_button_element(self):
        return self.driver.find_element(By.XPATH,
                                        '//div[contains(@class, "container-absolute")]//div[4]/div/div[3]/div/button[1]')

    def detail_cancel_button_element(self):
        return self.driver.find_element(By.XPATH,
                                        '//div[contains(@class, "container-absolute")]//div[3]/div/div[3]//button')

    def bill_create_confirm_button_element(self):
        return self.driver.find_element(By.XPATH,
                                        '//div[contains(@class, "container-absolute")]//div[4]/div/div[3]/div/button[2]')

    def bill_start_time_input_element(self):
        return self.driver.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[1]/div/div/div/div/input')

    def bill_end_time_input_element(self):
        return self.driver.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[2]/div/div/div/div/input')

    def add_bill_name_element(self):
        return self.driver.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[3]/div/div/div/div/input')

    def select_customer_id(self, customer_id):
        self.select_customer_id_dropdown_element().click()
        self.driver.find_element(By.XPATH, '//li/span[text()="{}"]'.format(customer_id)).click()

    def input_bill_name(self, bill_name):
        self.select_bill_name_element().clear()
        self.select_bill_name_element().send_keys(bill_name)

    def input_bill_name_clear(self):
        self.select_bill_name_element().clear()

    def bill_create(self):
        self.bill_create_element().click()

    def bill_start_time_input(self, start_time):
        self.bill_start_time_input_element().send_keys(start_time)
        self.driver.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[1]/div/div/label').click()

    def bill_end_time_input(self, end_time):
        self.bill_end_time_input_element().send_keys(end_time)
        self.driver.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[2]/div/div/label').click()

    def add_bill_name_input(self, bill_name):
        self.add_bill_name_element().send_keys(bill_name)

    def add_bill_button(self, button):
        if button == '确定':
            self.bill_create_confirm_button_element().click()
            PopupClose(self.driver).popup_close()
        elif button == '取消':
            self.bill_create_cancel_button_element().click()
        else:
            print("按钮只能是确定或取消")


if __name__ == '__main__':
    l = BillManagement()
