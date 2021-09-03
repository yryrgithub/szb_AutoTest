import time

from selenium.webdriver.common.by import By

from test.common.GetTips import GetTips
from test.common.DownloadFile import DownloadFile
from test.common.TableOperation import TableOperation


class FinancialStatistics(object):

    def __init__(self, driver):
        self.driver = driver

    def customer_id_dropdown_element(self):
        return self.driver.find_element(By.XPATH, '//div[contains(@class, "operate-left")]/span/div[1]/div[1]/input')

    def quota_id_dropdown_element(self):
        return self.driver.find_element(By.XPATH, '//div[contains(@class, "operate-left")]/span/div[2]/div[1]/input')

    def datasource_id_dropdown_element(self):
        return self.driver.find_element(By.XPATH, '//div[contains(@class, "operate-left")]/span/div[3]/div[1]/input')

    def start_time_input_element(self):
        return self.driver.find_element(By.XPATH, '//div[contains(@class, "el-range-editor")]/input[1]')

    def end_time_input_element(self):
        return self.driver.find_element(By.XPATH, '//div[contains(@class, "el-range-editor")]/input[2]')

    def search_button_element(self):
        return self.driver.find_element(By.XPATH, '//div[contains(@class, "operate-right")]/button[1]')

    def download_button_element(self):
        return self.driver.find_element(By.XPATH, '//div[contains(@class, "operate-right")]/button[2]')

    def select_customer_id(self, *customers_id):
        self.customer_id_dropdown_element().click()
        for customer_id in customers_id:
            ele = self.driver.find_element(By.XPATH, '//*[contains(text(), "{}")]'.format(customer_id))
            self.driver.execute_script('arguments[0].click()', ele)

    def select_quota_id(self, *quotas_id):
        self.quota_id_dropdown_element().click()
        for quota_id in quotas_id:
            ele = self.driver.find_element(By.XPATH, '//*[contains(text(), "{}")]'.format(quota_id))
            self.driver.execute_script('arguments[0].click()', ele)

    def select_datasource_id(self, *datasources_id):
        self.datasource_id_dropdown_element().click()
        for datasource_id in datasources_id:
            ele = self.driver.find_element(By.XPATH, '//*[contains(text(), "{}")]'.format(datasource_id))
            self.driver.execute_script('arguments[0].click()', ele)

    def select_time(self, start_time, end_time):
        self.start_time_input_element().send_keys(start_time)
        self.end_time_input_element().send_keys(end_time)

    def search(self):
        self.search_button_element().click()
        time.sleep(1)

    def download(self):
        self.download_button_element().click()
        time.sleep(1)

    def download_check(self):
        file1, data1 = DownloadFile().get_download_file()
        file2 = 'E:\\TestPython\\autoTestShuzunbao\\download\\ComparisonDocument\\2019-04-02_2020-05-20.xlsx'
        data2 = 'sheet1'
        DownloadFile().download_file_check(file1, data1, file2, data2)

    def select_condition(self, customer_id=None, quota_id=None, datasource_id=None, start_time=None):
        if customer_id == None and start_time == None:
            tips = GetTips(self.driver).get_tips()
            assert tips == '客户ID、指标ID、数据源ID三者不能同时为空'
        elif customer_id == None and start_time != None:
            tips = GetTips(self.driver).get_tips()
            assert tips == '客户ID、指标ID、数据源ID三者不能同时为空'
        elif customer_id == None and start_time == None:
            tips = GetTips(self.driver).get_tips()
            assert tips == '开始日期和结束日期不能为空'
        elif customer_id != None and start_time != None:
            tab = TableOperation(self.driver).get_table()
            if tab:
                print('已成功查询到数据')
            else:
                print('未查询到数据')
        else:
            print('断言类型错误！')
        time.sleep(5)
