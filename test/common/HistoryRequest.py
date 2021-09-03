import time
from selenium.webdriver.common.by import By

from test.common.multiMenuOperation import MultiMenuOperation
from utils.ResultScreenshot import ResultScreenShot
from test.common.DownloadFile import DownloadFile


class HistoryRequest(object):

    def __init__(self, driver):
        self.driver = driver

    # 定位下拉列表框
    def select_customer_id_element(self):
        return self.driver.find_element(By.XPATH,
                                        '//div[contains(@class, "operate-left")]/span/div[1]/div[1]/input')

    def select_quota_id_element(self):
        return self.driver.find_element(By.XPATH,
                                        '//div[contains(@class, "operate-left")]/span/div[2]/div[1]/input')

    def select_datasource_id_element(self):
        return self.driver.find_element(By.XPATH,
                                        '//div[contains(@class, "operate-left")]/span/div[3]/div[1]/input')

    # 定位下拉列表中的元素
    def select_customer_id_dropdown_element(self):
        return self.driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[1]/ul')

    # 定位查询按钮元素
    def search_element(self):
        return self.driver.find_element(By.XPATH,
                                        '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div[2]/button[1]')

    def download_button_element(self):
        return self.driver.find_element(By.XPATH, '//div[contains(@class, "operate-right")]/button[2]')

    def start_time_input_element(self):
        return self.driver.find_element(By.XPATH, '//div[contains(@class, "el-range-editor")]/input[1]')

    def end_time_input_element(self):
        return self.driver.find_element(By.XPATH, '//div[contains(@class, "el-range-editor")]/input[2]')

    # 客户ID下拉列表选择customer_id, *customers_id传入多个参数
    def select_customer_id(self, *customers_id):
        time.sleep(1)
        # MultiMenuOperation(driver=self.driver).select_menu('历史调用')
        self.select_customer_id_element().click()
        time.sleep(1)
        for customer_id in customers_id:
            ele = self.driver.find_element(By.XPATH, "//span[contains(text(),'{}')]".format(customer_id))
            self.driver.execute_script('arguments[0].click()', ele)
        ResultScreenShot(driver=self.driver).get_screen_shot("HistoryRequestPage-select_customer_id")
        time.sleep(1)

    def select_quota_id(self, *quotas_id):
        time.sleep(1)
        self.select_quota_id_element().click()
        time.sleep(1)
        for quota_id in quotas_id:
            ele = self.driver.find_element(By.XPATH, "//span[contains(text(),'{}')]".format(quota_id))
            self.driver.execute_script('arguments[0].click()', ele)
        ResultScreenShot(driver=self.driver).get_screen_shot("HistoryRequestPage-select_quota_id")
        time.sleep(1)

    def select_datasource_id(self, *datasources_id):
        time.sleep(1)
        # MultiMenuOperation(driver=self.driver).select_menu('历史调用')
        self.select_datasource_id_element().click()
        time.sleep(1)
        for datasource_id in datasources_id:
            ele = self.driver.find_element(By.XPATH, "//span[contains(text(),'{}')]".format(datasource_id))
            self.driver.execute_script('arguments[0].click()', ele)
        ResultScreenShot(driver=self.driver).get_screen_shot("HistoryRequestPage-select_quota_id")
        time.sleep(1)

    def select_time(self, start_time, end_time):
        self.start_time_input_element().send_keys(start_time)
        self.end_time_input_element().send_keys(end_time)
    # 查询功能
    def search(self):
        time.sleep(2)
        self.search_element().click()
        time.sleep(1)
        ResultScreenShot(driver=self.driver).get_screen_shot("HistoryRequestPage-search")
        time.sleep(2)

    # 历史查询下载功能 ，下载后并比较下载数据是否正确
    def history_request_download(self, report_path):
        self.download_button_element().click()  # 点击下载按钮
        file1, data1 = DownloadFile().get_download_file(report_path)  # 获取最新下载的文件的路径及第一个sheet页名称
        # file2, data2 = DownloadFile().get_download_file(report_path_old)    # 获取正确的对比的文件的路径及第一个sheet页名称
        file2 = 'E:\\TestPython\\autoTestShuzunbao\\download\\ComparisonDocument\\历史调用记录.xlsx'
        data2 = '历史数据'
        DownloadFile().download_file_check(file1, data1, file2, data2)

