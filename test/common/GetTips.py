import sys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class GetTips(object):

    def __init__(self, driver):
        self.driver = driver

    def get_tips(self):
        try:
        # 显示等待 获取短暂弹出提示的信息
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element(By.XPATH, '//p[contains(@class,"el-message")]'))
            return self.driver.find_element(By.XPATH, '//p[contains(@class,"el-message")]').text
        except Exception as e:
            print(e.args)
            return False
        # WebDriverWait(self.driver, 10).until(lambda x: x.find_element(By.XPATH, '//p[contains(@class,"el-message")]'))
        # return self.driver.find_element(By.XPATH, '//p[contains(@class,"el-message")]').text
