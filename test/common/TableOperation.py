import time
from selenium import webdriver

from test.common.multiMenuOperation import MultiMenuOperation


class TableOperation(object):

    def __init__(self, driver):
        self.driver = driver

    def get_table(self):
        time.sleep(1)
        # table、header、body_rows、body_rows_columns
        table_body = self.driver.find_element_by_id('table-container')
        table_rows = table_body.find_elements_by_tag_name('tr')
        return table_rows

    # 只需单个值就可以定位某行操作
    def row_click(self, header_text, row_text, column_index):
        """选择表格中行并且点击"""
        time.sleep(2)
        table_rows = self.get_table()
        table_rows_length = len(table_rows)
        for i in range(1, table_rows_length):
            table_value = table_rows[i].find_elements_by_tag_name('td')[column_index]
            if table_value.text == header_text:
                table_operations = table_rows[i].find_elements_by_tag_name('button')
                for table_operation in table_operations:
                    if table_operation.text == row_text:
                        table_operation.click()
            # return table_operation.text
        else:
            pass

    # 需要多个值去定位一行操作
    def row_click_double(self, header_text1,header_text2, row_text, column_index1, column_index2):
        time.sleep(2)
        table_rows = self.get_table()
        table_rows_length = len(table_rows)
        for i in range(1, table_rows_length):
            table_value1 = table_rows[i].find_elements_by_tag_name('td')[column_index1]
            table_value2 = table_rows[i].find_elements_by_tag_name('td')[column_index2]
            if table_value1.text == header_text1 and table_value2.text == header_text2:
                table_operations = table_rows[i].find_elements_by_tag_name('button')
                for table_operation in table_operations:
                    if table_operation.text == row_text:
                        table_operation.click()
        else:
            pass


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://139.224.57.204:8080/index.html#/login")
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[1]/div/div[1]/input').send_keys('admin')
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[2]/div/div[1]/input').send_keys('shuzun123')
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[3]/div/div/input').send_keys('123456')
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/button').click()
    time.sleep(2)
    MultiMenuOperation(driver=driver).select_menu('修改审批')
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div/span/span/i').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div[2]/button').click()
    time.sleep(2)
    TableOperation(driver=driver).row_click(header_text='570478505267200', row_text='详情', column_index=1)
