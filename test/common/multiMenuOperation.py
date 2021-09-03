import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.Logger import Logger

logger = Logger(logger='TestQuotaConfigPage').get_log()


class MultiMenuOperation(object):

    def __init__(self, driver):
        self.driver = driver

    def get_first_menu(self):
        # 定位左侧所有一级菜单元素
        menu_level1 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/ul')
        rows1 = menu_level1.find_elements_by_tag_name('div')
        menu_level = []
        for row in rows1:
            menu_level.append(row)
        # print(menu_level)
        return menu_level

    def select_menu(self, menu_text):
        time.sleep(1)
        menu_level = self.get_first_menu()
        for menu in menu_level:
            time.sleep(1)
            menu.click()
            # 定位左侧所有二级菜单元素
            menu_level2 = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[1]')
            rows2 = menu_level2.find_elements_by_tag_name('li')
            for row in rows2:
                if row.text == menu_text:
                    time.sleep(1)
                    # 被遮挡元素无法使用默认的WebElement.Click()可能会触发不了Click事件。
                    # row.click()
                    # 定位被遮挡元素
                    self.driver.execute_script('arguments[0].click()', row)
                    logger.info("进入%s页面进行测试", menu_text)
                    break
            if row.text == menu_text:
                break
            else:
                continue


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://139.224.57.204:8080/index.html#/login")
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[1]/div/div[1]/input').send_keys('admin')
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[2]/div/div[1]/input').send_keys('shuzun123')
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[3]/div/div/input').send_keys('123456')
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/button').click()
    time.sleep(2)
    MultiMenuOperation(driver=driver).select_menu('调用详情')
    # driver.quit()
