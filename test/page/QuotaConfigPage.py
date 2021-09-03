import time
from selenium.webdriver.common.by import By

from test.common.GetTips import GetTips
from test.common.TableOperation import TableOperation
from test.page.LoginPage import LoginPage
from utils.Logger import Logger
from utils.ResultScreenshot import ResultScreenShot

logger = Logger(logger='QuotaConfigPage').logger


class QuotaConfigPage(LoginPage):

    def search_element(self):
        time.sleep(1)
        return self.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div[2]/div/input')

    def search_button_element(self):
        time.sleep(1)
        return self.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div[2]/button')

    def refresh_cache_element(self):
        time.sleep(1)
        return self.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div[1]/button')

    def popup_close_element(self):
        return self.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[3]/div/div[1]/button')

    def modify_cancel_element(self):
        return self.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[3]/div/div[3]/div/button[1]')

    def modify_confirm_element(self):
        return self.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[3]/div/div[3]/div/button[2]')

    def customer_id_element(self):
        return self.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[1]/div[1]/div/div/div/input')

    def computer_short_element(self):
        return self.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[1]/div[2]/div/div/div/input')

    def quota_id_element(self):
        return self.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[2]/div[1]/div/div/div/input')

    def quota_name_element(self):
        return self.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[2]/div[2]/div/div/div/input')

    def search(self, customer_id):
        time.sleep(2)
        self.search_element().send_keys(customer_id)
        self.search_button_element().click()
        ResultScreenShot(driver=self.driver).get_screen_shot("QuotaConfigPage")
        logger.info("查询功能测试，查询客户%s", customer_id)
        time.sleep(1)

    def refresh_cache(self):
        time.sleep(2)
        self.refresh_cache_element().click()
        tips = GetTips(self.driver).get_tips()
        if tips == '刷新缓存成功':
            logger.info('缓存刷新成功')
        else:
            logger.info('缓存刷新失败')
        ResultScreenShot(driver=self.driver).get_screen_shot("QuotaConfigPage")
        time.sleep(2)

    def modify(self, button_text):
        # MultiMenuOperation(driver=self.driver).select_menu('指标配置')
        # self.search()
        # self.operation('develop', '修改')
        customer_id_disable = self.customer_id_element().is_enabled()
        computer_short_disable = self.computer_short_element().is_enabled()
        quota_id_disable = self.quota_id_element().is_enabled()
        quota_name_disable = self.quota_name_element().is_enabled()
        assert customer_id_disable == False
        assert computer_short_disable == False
        assert quota_id_disable == False
        assert quota_name_disable == False
        time.sleep(1)
        if button_text == '确认':
            self.modify_confirm_element().click()
        elif button_text == '取消':
            self.modify_cancel_element().click()
        else:
            print('按钮只能是确认或取消')

    def operation(self, header_text1, header_text2, row_text, column_index1, column_index2):
        TableOperation(driver=self.driver).row_click_double(header_text1, header_text2, row_text, column_index1,
                                                            column_index2)
        ResultScreenShot(driver=self.driver).get_screen_shot("operation")

    def popup_close(self):
        self.popup_close_element().click()
        logger.info("X关闭弹窗")


if __name__ == '__main__':
    l = QuotaConfigPage()
    l.login_base()
    # l.search()
    time.sleep(1)
    l.refresh_cache()
