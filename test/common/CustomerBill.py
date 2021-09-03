from selenium.webdriver.common.by import By

from test.common.GetTips import GetTips
from test.common.TableOperation import TableOperation


class CustomerBill(object):

    def __init__(self, driver):
        self.driver = driver

    def start_time_input_element(self):
        return self.driver.find_element(By.XPATH, '//div[contains(@class, "el-range-editor")]/input[1]')

    def end_time_input_element(self):
        return self.driver.find_element(By.XPATH, '//div[contains(@class, "el-range-editor")]/input[2]')

    def search_button_element(self):
        return self.driver.find_element(By.XPATH, '//div[contains(@class, "operate-right")]/button[1]')

    def download_button_element(self):
        return self.driver.find_element(By.XPATH, '//div[contains(@class, "operate-right")]/button[2]')

    def select_time(self, start_time, end_time):
        self.start_time_input_element().send_keys(start_time)
        self.end_time_input_element().send_keys(end_time)

    def search(self):
        self.search_button_element().click()

    def download_file(self):
        self.download_button_element().click()

    def search_check(self, start_tiem=None, end_time=None):
        if start_tiem == None and end_time == None:
            tips = GetTips(self.driver).get_tips()
            print(tips)
            assert tips == '开始日期和结束日期不能为空'
        elif start_tiem != None and end_time != None:
            tab = TableOperation(self.driver).get_table()
            if tab:
                print('已成功查询到数据')
            else:
                print('未查询到数据')
        else:
            print('断言类型错误！')




