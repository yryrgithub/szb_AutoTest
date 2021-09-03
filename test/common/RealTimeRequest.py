import os
import time

from selenium.webdriver.common.by import By
from test.common.DownloadFile import DownloadFile


class RealTimeRequest(object):

    def __init__(self, driver):
        self.driver = driver

    def customer_id_dropdown_element(self):
        return self.driver.find_element(By.XPATH, '//div[contains(@class, "operate-left")]/span/div[1]/div[1]/input')

    def quota_id_dropdown_element(self):
        return self.driver.find_element(By.XPATH, '//div[contains(@class, "operate-left")]/span/div[2]/div[1]/input')

    def datasource_id_dropdown_element(self):
        return self.driver.find_element(By.XPATH, '//div[contains(@class, "operate-left")]/span/div[3]/div[1]/input')

    def date_dropdown_element(self):
        return self.driver.find_element(By.XPATH, '//div[contains(@class, "el-range-editor")]/input[1]')

    def search_button_element(self):
        return self.driver.find_element(By.XPATH, '//div[contains(@class, "operate-right")]/button[1]')

    def download_button_element(self):
        return self.driver.find_element(By.XPATH, '//div[contains(@class, "operate-right")]/button[2]')

    def start_date_input_element(self):
        return self.driver.find_element(By.XPATH,
                                 '//div[contains(@class, "el-date-range-picker")]/div[1]/div/div[1]/span[1]/span[1]/div/input')

    def start_date_h_input_element(self):
        return self.driver.find_element(By.XPATH,
                                 '//div[contains(@class, "el-date-range-picker")]/div[1]/div/div[1]/span[1]/span[2]/div[1]/input')

    def end_date_input_element(self):
        return self.driver.find_element(By.XPATH, '//span[contains(@class, "is-right")]/span[1]/div/input')

    def end_date_h_input_element(self):
        return self.driver.find_element(By.XPATH, '//span[contains(@class, "is-right")]/span[2]/div[1]/input')

    def date_input_confirm_button(self):
        return self.driver.find_element(By.XPATH, '//button[contains(@class, "is-plain")]/span')

    def date_input_cancel_button(self):
        return self.driver.find_element(By.XPATH, '//div[contains(@class, "el-date-range-picker")]/div[2]/button[1]/span')

    # 下拉列表中选择客户ID
    def select_customer_id(self, *customers_id):
        self.customer_id_dropdown_element().click()
        # self.customer_id_dropdown_element().clear()
        time.sleep(1)
        for customer_id in customers_id:
            ele = self.driver.find_element(By.XPATH, "//li//span[text()='{}']".format(customer_id))
            # 下拉列表元素是选中状态时，不再勾选
            #     pele = self.find_element(By.XPATH, "//li//span[text()='{}']/parent::li".format(customer_id))
            #     print(pele.is_selected())
            #     if pele.is_selected():
            #       pass
            #     else:
            self.driver.execute_script('arguments[0].click()', ele)

    # 下拉列表中选择指标IDs
    def select_quota_id(self, *quotas_id):
        self.quota_id_dropdown_element().click()
        # self.quota_id_dropdown_element().clear()
        time.sleep(1)
        for quota_id in quotas_id:
            ele = self.driver.find_element(By.XPATH, "//li//span[text()='{}']".format(quota_id))
            self.driver.execute_script('arguments[0].click()', ele)

    # 下拉列表中选择数据源ID
    def select_datasource_id(self, *datasources_id):
        self.datasource_id_dropdown_element().click()
        # js = 'document.getElementsByXpath("//div[contains(@class,"operate-left)]/span/div[1]/div[1]/input").value=""'
        # self.driver.execute_script(js)
        # document.getElementByXpath('//div[contains(@class, "operate-left")]/span/div[1]/div[1]/input').value='';
        # self.datasource_id_dropdown_element().clear()
        time.sleep(1)
        for datasource_id in datasources_id:
            ele = self.driver.find_element(By.XPATH, "//li//span[text()='{}']".format(datasource_id))
            self.driver.execute_script('arguments[0].click()', ele)

    def select_date(self):
        self.date_dropdown_element().click()
        self.start_date_input_element().send_keys('2021-06-30')
        self.start_date_h_input_element().clear()
        self.start_date_h_input_element().send_keys('18:00:00')
        self.end_date_input_element().clear()
        self.end_date_input_element().send_keys('2021-07-01')
        self.end_date_h_input_element().clear()
        self.end_date_h_input_element().send_keys('10:00:00')
        self.date_input_confirm_button().click()

    # 下载后excel文件数据对比
    # def download_file_check(self):
    #     current_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    #     print(current_path)
    #     file_path1 = current_path + '/download/实时调用记录.xlsx'
    #     file_path2 = current_path + '/download/ComparisonDocument/实时调用记录.xlsx'
    #     DownloadFile().download_file_check(file_path1, '实时数据', file_path2, '实时数据')

    # 实现查询功能
    def search(self):
        time.sleep(1)
        self.search_button_element().click()

    def real_time_request_file_download(self, report_path):
        self.download_button_element().click()  # 点击下载按钮
        file1, data1 = DownloadFile().get_download_file(report_path)  # 获取最新下载的文件的路径及第一个sheet页名称
        # file2, data2 = DownloadFile().get_download_file(report_path_old)    # 获取正确的对比的文件的路径及第一个sheet页名称
        file2 = 'E:\\TestPython\\autoTestShuzunbao\\download\\ComparisonDocument\\实时调用记录.xlsx'
        data2 = '实时数据'
        DownloadFile().download_file_check(file1, data1, file2, data2)

if __name__ == '__main__':
    l = RealTimeRequest()
    current_path1 = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    print(current_path1)
    file_path = current_path1 + '/download/实时调用记录.xlsx'
    l.download_file_check()
    # l.login_base()
    # MultiMenuOperation(l.driver).select_menu(menu_text='实时调用')
    # l.select_customer_id('develop','bonc')
    # l.select_quota_id('RZ018--姓名-身份证号-银行卡号-手机号(简)')
    # l.select_datasource_id('DS_GX018')
    # l.search()
    # time.sleep(1)
    # l.download_file()
