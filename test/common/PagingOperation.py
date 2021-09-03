import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from test.common.DropdownOperation import DropdownOperation
from test.common.multiMenuOperation import MultiMenuOperation
from utils.ResultScreenshot import ResultScreenShot


class PagingOperation(object):

    def __init__(self, driver):
        self.driver = driver

    def first_page_element(self):
        return self.driver.find_element_by_class_name('btn-prev')

    def next_page_element(self):
        return self.driver.find_element_by_class_name('btn-next')

    def input_page_element(self):
        return self.driver.find_element_by_xpath('//*[@id="table-container"]/div[2]/span[3]/div/input')

    def page_numbers_dropdown_element(self):
        # 获取页面下拉框元素
        return self.driver.find_element_by_xpath('//*[@id="table-container"]/div[2]/span[2]/div/div[1]/input')

    def page_numbers_element(self):
        # 获取页码选择下拉框所在的div标签元素
        return self.driver.find_element_by_class_name('el-scrollbar__view')

    def select_page_number(self, page_number):
        time.sleep(1)
        self.page_numbers_dropdown_element().click()
        DropdownOperation(self.driver).select_dropdown(dropdown_value=page_number)

    def page_operation(self, page_text):
        time.sleep(1)
        if page_text == '首页' or page_text == '第一页':
            self.first_page_element().click()
            ResultScreenShot(driver=self.driver).get_screen_shot("page_operation首页")
        elif page_text == '下一页':
            self.next_page_element().click()
            ResultScreenShot(driver=self.driver).get_screen_shot("page_operation下一页")
            print(type(4))
        elif type(page_text) == int:
            time.sleep(2)
            # 模拟键盘删除键，删除已于的页码值
            self.input_page_element().send_keys(Keys.BACK_SPACE)
            self.input_page_element().send_keys(page_text)
            # 模拟键盘enter键
            self.input_page_element().send_keys(Keys.ENTER)
            ResultScreenShot(driver=self.driver).get_screen_shot("page_operation跳转页 ")
            time.sleep(1)
        else:
            print('只接受首页，第一页，下一页')


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://139.224.57.204:8080/index.html#/login")
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[1]/div/div[1]/input').send_keys('admin')
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[2]/div/div[1]/input').send_keys('shuzun123')
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[3]/div/div/input').send_keys('123456')
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/button').click()
    time.sleep(2)
    MultiMenuOperation(driver=driver).select_menu('客户配置')
    time.sleep(2)
    l = PagingOperation(driver=driver)
    l.select_page_number('20条/页')
    l.page_operation(page_text=5)

