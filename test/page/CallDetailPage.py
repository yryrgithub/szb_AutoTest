from selenium.webdriver.common.by import By

from test.page.LoginPage import LoginPage
from test.common.multiMenuOperation import MultiMenuOperation


class CallDetailPage(LoginPage):

    def customer_id_input_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[1]//input')

    def start_time_input_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[2]//input[1]')

    def end_time_input_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[2]//input[2]')

    def product_id_input_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[3]//input[1]')

    def api_id_input_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[3]//input[2]')

    def datasource_id_input_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[4]//input[1]')

    def parameter_input_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[4]//input[2]')

    def isfound_input_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[5]//input[1]')

    def iscache_input_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[5]//input[2]')

    def rescode_input_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[6]//input[1]')

    def number_limit_input_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[6]//input[2]')

    def condition_search_confirm_button_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog--center")]/div[3]//button')

    def condition_search_button_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"operate-right")]/button[1]')

    def call_detail_download_button_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"operate-right")]/button[2]')

    def condition_search_popup_close(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"container-absolute")]/div/div/div[3]/div/div/button')

    def start_time_confirm_button_element(self):
        return self.find_element(By.XPATH, '/html/body/div[4]/div[2]/button[2]')

    def end_time_confirm_button_element(self):
        return self.find_element(By.XPATH, '/html/body/div[8]/div[2]/button[2]')

    def condition_search_popup(self):
        self.start_time_input_element().click()
        self.find_element(By.XPATH, '//div[contains(@class,"el-date-picker__time-header")]/span[1]//input').send_keys(
            '2021-07-06')
        self.find_element(By.XPATH, '//div[contains(@class,"el-date-picker__time-header")]/span[2]//input').clear()
        self.find_element(By.XPATH, '//div[contains(@class,"el-date-picker__time-header")]/span[2]//input').send_keys(
            '00:00:00')
        self.start_time_confirm_button_element().click()
        self.end_time_input_element().click()
        self.find_element(By.XPATH, '//div[contains(@class,"el-date-picker__time-header")]/span[1]//input').send_keys(
            '2021-07-07')
        self.find_element(By.XPATH, '//div[contains(@class,"el-date-picker__time-header")]/span[2]//input').clear()
        self.find_element(By.XPATH, '//div[contains(@class,"el-date-picker__time-header")]/span[2]//input').send_keys(
            '00:00:00')
        self.end_time_confirm_button_element().click()
        self.condition_search_confirm_button_element().click()

    def condition_search(self):
        self.condition_search_button_element().click()
        self.condition_search_popup()

    def call_detail_download(self):
        self.call_detail_download_button_element().click()


if __name__ == '__main__':
    l = CallDetailPage()
    l.login_base()
    MultiMenuOperation(l.driver).select_menu("调用详情")
    l.condition_search_popup()




