import os
import time

from selenium import webdriver

from utils.Logger import Logger
from utils.readConfig import ReadConfig

logger = Logger(logger='BasePage').get_log()


class BasePage(object):

    def __init__(self, driver_path=None, base_url=None):
        if driver_path is None:
            current_path = os.path.abspath(os.path.dirname(__file__))
            driver_path = current_path + '/../../drivers/chromedriver'
        else:
            driver_path = driver_path
        # 获取浏览器的操作指令
        options = webdriver.ChromeOptions()
        # 浏览器需要添加的参数值
        prefs = {'profile.default_conten_seeeings.popups': 0,
                 "download.default_directory": "E:\\TestPython\\autoTestShuzunbao\\download"}
        # 添加实验性质的设置参数
        options.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(driver_path, options=options)
        logger.info('打开谷歌浏览器')

        if base_url is None:
            self.base_url = 'http://139.224.57.204:8080/index.html#/login'
        else:
            self.base_url = base_url
        self.open_page()

    def open_page(self):
        self.driver.maximize_window()
        logger.info('窗口最大化')
        self.driver.implicitly_wait(10)
        self.driver.get(self.base_url)
        logger.info('打开测试系统地址')
        # time.sleep(2)

    def close_page(self):
        return self.driver.close()
        logger.info('关闭浏览器当前页')

    def quit_page(self):
        return self.driver.quit()
        logger.info('关闭整个浏览器')

    def find_element(self, by, element):
        time.sleep(1)
        return self.driver.find_element(by, element)

    def find_elements(self, by, element):
        time.sleep(1)
        return self.driver.find_elements(by, element)

    def switch_alter(self):
        time.sleep(1)
        l = self.driver.switch_to.alert()
        print(l)
        return self.driver.switch_to.alert.text

    def get_current_windows(self):
        handel = self.driver.current_window_handle
        return self.driver.switch_to.window(handel)


if __name__ == '__main__':
    current_path1 = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    print(current_path1)
    file_path = current_path1 + '/settings/base_data.json'
    print(file_path)
    data = ReadConfig().read_json(file_path)
    print(data)
    BasePage(base_url=data['base_url'])
