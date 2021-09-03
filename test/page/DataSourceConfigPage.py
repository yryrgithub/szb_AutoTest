import time

from selenium.webdriver.common.by import By

from test.common.DropdownOperation import DropdownOperation
from test.common.multiMenuOperation import MultiMenuOperation
from test.page.LoginPage import LoginPage
from utils.Logger import Logger

logger = Logger(logger='DataSourcesConfigPage').get_log()


class DataSourcesConfigPage(LoginPage):

    def refresh_cache_button_element(self):
        return self.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div[1]/button[1]')

    def add_config_button_element(self):
        return self.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div[1]/button[2]')

    def customer_id_input_element(self):
        return self.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div[2]/div[1]/input')

    def quota_id_input_element(self):
        return self.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div[2]/div[2]/input')

    def search_button_element(self):
        return self.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div[2]/button')

    def expand_button_element(self):
        return self.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/div')

    def expand_edit_button_element(self):
        return self.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[9]/div/button')

    def weight_input_element(self):
        return self.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[7]/div/div/input')

    def status_input_element(self):
        return self.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[8]/div/div/div')

    def edit_confirm_element(self):
        return self.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[9]/div/button[1]')

    def edit_cancel_element(self):
        return self.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[9]/div/button[2]')

    def add_config_cancel_button_element(self):
        return self.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[3]/div/button[1]')

    def add_config_confirm_button_element(self):
        return self.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[3]/div/button[2]')

    def refresh_cache(self):
        time.sleep(1)
        self.refresh_cache_button_element().click()
        logger.info('刷新缓存')

    def add_config(self, button):
        self.add_config_button_element().click()
        time.sleep(2)
        if button == '确认':
            self.add_config_confirm_button_element().click()
            logger.info('确认新增配置')
            time.sleep(1)
        elif button == '取消':
            self.add_config_cancel_button_element().click()
            logger.info('取消新增配置')
            time.sleep(1)
        else:
            logger.info('按钮只能是确认或取消')

    def edit(self, button, status):
        time.sleep(2)
        self.expand_edit_button_element().click()
        time.sleep(1)
        self.weight_input_element().clear()
        logger.info('清空权重输入框')
        self.weight_input_element().send_keys('80')
        logger.info('输入新的权重值')
        self.status_input_element().click()
        time.sleep(2)
        DropdownOperation(self.driver).select_dropdown(dropdown_value=status)
        logger.info('下拉列表选择客户状态')
        if button == '确认':
            self.edit_confirm_element().click()
            logger.info('确认编辑')
            time.sleep(1)
        elif button == '取消':
            self.edit_cancel_element().click()
            logger.info('取消编辑')
            time.sleep(1)
        else:
            logger.info('按钮只能是确认或取消')
        time.sleep(2)

    def search(self, customer_id, quota_id):
        time.sleep(1)
        self.customer_id_input_element().send_keys(customer_id)
        self.quota_id_input_element().send_keys(quota_id)
        time.sleep(1)
        self.search_button_element().click()
        logger.info('查询客户%s+产品%s', customer_id, quota_id)
        time.sleep(2)
        self.expand_button_element().click()


if __name__ == '__main__':
    l = DataSourcesConfigPage()
    l.login_base()
    MultiMenuOperation(driver=l.driver).select_menu('数据源配置')
    l.search(customer_id='develop', quota_id='RZ028')
    l.edit(button='确认', status='停用')
    # l.add_config(button='取消')
