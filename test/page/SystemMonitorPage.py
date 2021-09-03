from selenium.webdriver.common.by import By
import time

from test.common.GetTips import GetTips
from test.common.multiMenuOperation import MultiMenuOperation
from test.page.LoginPage import LoginPage


class SystemMonitorPage(LoginPage):

    def customers_dropdown_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"operate-left")]//span//div[1]//div//input')

    def quota_dropdown_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"operate-left")]//span//div[2]//div//input')

    def date_dropdown_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"operate-right")]//input[1]')

    def search_button_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"operate-right")]//button[1]')

    def download_button_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"operate-right")]//button[2]')

    def select_customer_id(self,customers_id):
        time.sleep(1)
        self.customers_dropdown_element().click()
        self.find_element(By.XPATH, '//li//span[text()="{}"]'.format(customers_id)).click()

    def select_quota_id(self,quota_id):
        time.sleep(1)
        self.quota_dropdown_element().click()
        self.find_element(By.XPATH, '//li//span[text()="{}"]'.format(quota_id)).click()

    def search(self):
        time.sleep(1)
        self.search_button_element().click()
        if(GetTips(self.driver).get_tips()):
            tips = GetTips(self.driver).get_tips()
            assert tips == '客户ID不能为空'

    def download(self):
        time.sleep(1)
        self.download_button_element().click()

if __name__ == '__main__':
    l = SystemMonitorPage()
    l.login_base()
    MultiMenuOperation(l.driver).select_menu(menu_text='系统监控')
    l.select_customer_id('bonc')
    l.search()