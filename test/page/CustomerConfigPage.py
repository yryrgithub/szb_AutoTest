import time
from selenium.webdriver.common.by import By

from test.common.GetTips import GetTips
from test.common.TableOperation import TableOperation
from test.common.multiMenuOperation import MultiMenuOperation
from test.page.LoginPage import LoginPage
from utils.Logger import Logger
from utils.ResultScreenshot import ResultScreenShot

logger = Logger(logger='CustomerConfigPage').get_log()


class CustomerConfigPage(LoginPage):

    def search_element(self):
        return self.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div[2]/div/input')

    def search_button_element(self):
        return self.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div[2]/button/i')

    def add_customer_element(self):
        return self.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div[1]/button[1]')

    def refresh_cache_element(self):
        return self.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div[1]/button[2]')

    def customer_id_element(self):
        return self.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[3]/div/div[2]/form/div[1]/div[1]/div/div/div[1]/input')

    def computer_abbreviation_element(self):
        return self.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[3]/div/div[2]/form/div[1]/div[2]/div/div/div[1]/input')

    def computer_name_element(self):
        return self.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[3]/div/div[2]/form/div[2]/div[1]/div/div/div[1]/input')

    def customer1_type_element(self):
        return self.find_element(By.XPATH,
                                 '//form[contains(@class, "el-form")]/div[2]/div[2]/div/div/div[1]/div/input')

    def bankcard_name_element(self):
        return self.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[3]/div/div[2]/form/div[3]/div[1]/div/div/div/input')

    def bankcard_number_element(self):
        return self.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[3]/div/div[2]/form/div[3]/div[2]/div/div/div/input')

    def customer_status_element(self):
        return self.find_element(By.XPATH,
                                 '//form[contains(@class, "el-form")]/div[4]/div[1]/div/div/div[1]/div/input')

    def expense_type_element(self):
        return self.find_element(By.XPATH,
                                 '//form[contains(@class, "el-form")]/div[4]/div[2]/div/div/div[1]/div/input')

    def limit_items_element(self):
        return self.find_element(By.XPATH,
                                 '//form[contains(@class, "el-form")]/div[5]/div[1]/div/div/div[1]/input')

    def money_element(self):
        return self.find_element(By.XPATH,
                                 '//form[contains(@class, "el-form")]/div[5]/div[2]/div/div/div[1]/input')

    def rsa_key_element(self):
        return self.find_element(By.XPATH,
                                 '//form[contains(@class, "el-form")]/div[6]/div[1]/div/div/div/input')

    def ip_whitelist_element(self):
        return self.find_element(By.XPATH,
                                 '//form[contains(@class, "el-form")]/div[6]/div[2]/div/div/div[1]/input')

    def customer_type_element(self):
        return self.find_element(By.XPATH,
                                 '//form[contains(@class, "el-form")]/div[7]/div[1]/div/div/div[1]/div/input')

    def customer_mark_element(self):
        return self.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[3]/div/div[2]/form/div[6]/div[1]/div/div/div/input')

    def contract_upload_element(self):
        return self.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[3]/div/div[2]/form/div[8]/div[1]/div/div/div/div/div[2]/div/div/button')

    def sale_select_element(self):
        return self.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[3]/div/div[2]/form/div[8]/div[2]/div/div/div/div/input')

    def contact_name_element(self):
        return self.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[3]/div/div[2]/form/div[9]/div[1]/div/div/div[1]/input')

    def contact_mobile_element(self):
        return self.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[3]/div/div[2]/form/div[9]/div[2]/div/div/div[1]/input')

    def contact_email_element(self):
        return self.find_element(By.XPATH,
                                  '//form[contains(@class, "el-form")]/div[10]/div[1]/div/div/div[1]/input')

    def reset_key_element(self):
        return self.find_element(By.XPATH,
                                 '//form[contains(@class, "el-form")]/div[10]/div[2]/div/div/div[1]/div/input')

    def node_element(self):
        return self.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[3]/div/div[2]/form/div[11]/div[2]/div/div/div/input')

    def email_senders_element(self):
        return self.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[3]/div/div[2]/form/div[12]/div[1]/div/div/div/div[1]/input')

    def email_fields_element(self):
        return self.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[3]/div/div[2]/form/div[12]/div[2]/div/div/div/div[1]/input')

    def limit_speed_element(self):
        return self.find_element(By.XPATH,
                                 '//form[contains(@class, "el-form")]/div[11]/div[1]/div/div/div[1]/input')

    def add_button_confirm_element(self):
        return self.find_element(By.XPATH,
                                 '//div[contains(@class, "container-absolute")]/div/div/div[3]/div/div[3]/div/button[2]')

    def add_button_cancel_element(self):
        return self.find_element(By.XPATH,
                                 '//div[contains(@class, "container-absolute")]/div/div/div[3]/div/div[3]/div/button[1]')

    def popup_close_element(self):
        return self.find_element(By.XPATH,
                                 '//div[contains(@class, "container-absolute")]/div/div/div[3]/div/div[1]/button/i')

    def customer_id_error_message(self):
        return self.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[1]/div[1]/div/div/div[2]')

    def computer_short_error_message(self):
        return self.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[1]/div[2]/div/div/div[2]')

    def computer_name_error_message(self):
        return self.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[2]/div[1]/div/div/div[2]')

    def customer1_type_error_message(self):
        return self.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[2]/div[2]/div/div/div[2]')

    def customer_status_error_message(self):
        return self.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[4]/div[1]/div/div/div[2]')

    def pay_type_error_message(self):
        return self.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[4]/div[2]/div/div/div[2]')

    def limit_item_error_message(self):
        return self.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[5]/div[1]/div/div/div[2]')

    def money_error_message(self):
        return self.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[5]/div[2]/div/div/div[2]')

    def customer_type2_error_message(self):
        return self.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[7]/div[1]/div/div/div[2]')

    def customer_mark_error_message(self):
        return self.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[7]/div[2]/div/div/div[2]')

    def sale_error_message(self):
        return self.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[8]/div[2]/div/div/div[2]')

    def contact_error_message(self):
        return self.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[9]/div[1]/div/div/div[2]')

    def mobile_error_message(self):
        return self.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[9]/div[2]/div/div/div[2]')

    def email_error_message(self):
        return self.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[10]/div[1]/div/div/div[2]')

    def private_key_error_message(self):
        return self.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[10]/div[2]/div/div/div[2]')

    def limit_speed_error_message(self):
        return self.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[11]/div[1]/div/div/div[2]')

    # def contact_error_message(self):
    #     return self.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[9]/div[1]/div/div/div[2]')

    def search(self, customers_id):
        MultiMenuOperation(driver=self.driver).select_menu('客户配置')
        time.sleep(1)
        self.search_element().send_keys(customers_id)
        self.search_button_element().click()
        ResultScreenShot(driver=self.driver).get_screen_shot("CustomerConfigPage")
        logger.info('查询客户：%s', customers_id)
        time.sleep(2)

    def add_button_click_check(self):
        self.add_customer_element().click()

    def add_customers(self, customer_id=None, computer_abbreviation=None, computer_name=None, customer_type=None,
                      customer_status=None, pay_type=None, limit_item=None, money=None,
                      RSA_key=None, ip_whitelist=None, customer_type2=None, customer_mark=None, sale=None, contact=None,
                      email=None, limit_speed=None, bill_sender=None, mobile=None, is_reset=None, note=None,
                      bill_fields=None, button='确认'):
        time.sleep(1)
        if customer_id != None:
            self.customer_id_element().clear()
            self.customer_id_element().send_keys(customer_id)
        if computer_abbreviation != None:
            self.computer_abbreviation_element().clear()
            self.computer_abbreviation_element().send_keys(computer_abbreviation)
        if computer_name != None:
            self.computer_name_element().clear()
            self.computer_name_element().send_keys(computer_name)
        if customer_type != None:
            self.customer1_type_element().click()
            self.driver.find_element(By.XPATH, '//li/span[contains(text(), "{}")]'.format(customer_type)).click()
        if customer_status != None:
            self.customer_status_element().click()
            self.driver.find_element(By.XPATH, '//li/span[contains(text(), "{}")]'.format(customer_status)).click()
        if pay_type != None:
            self.expense_type_element().click()
            self.driver.find_element(By.XPATH, '//li/span[contains(text(), "{}")]'.format(pay_type)).click()
        if limit_item != None:
            self.limit_items_element().clear()
            self.limit_items_element().send_keys(limit_item)
        if money != None:
            self.money_element().clear()
            self.money_element().send_keys(money)
        if RSA_key != None:
            self.rsa_key_element().clear()
            self.rsa_key_element().send_keys(RSA_key)
        if ip_whitelist != None:
            self.ip_whitelist_element().clear()
            self.ip_whitelist_element().send_keys(ip_whitelist)
        if customer_type2 != None:
            self.customer_type_element().click()
            self.driver.find_element(By.XPATH, '//li/span[contains(text(), "{}")]'.format(customer_type2)).click()
        if customer_mark != None:
            self.customer_mark_element().click()
            self.driver.find_element(By.XPATH, '//li/span[contains(text(), "{}")]'.format(customer_mark)).click()
        if sale != None:
            self.sale_select_element().click()
            self.driver.find_element(By.XPATH, '//li/span[contains(text(), "{}")]'.format(sale)).click()
        if contact != None:
            self.contact_name_element().clear()
            self.contact_name_element().send_keys(contact)
        if email != None:
            self.contact_email_element().clear()
            self.contact_email_element().send_keys(email)
        if limit_speed != None:
            self.limit_speed_element().clear()
            self.limit_speed_element().send_keys(limit_speed)
        if bill_sender != None:
            self.email_senders_element().clear()
            self.email_senders_element().send_keys(bill_sender)
        if mobile != None:
            self.contact_mobile_element().clear()
            self.contact_mobile_element().send_keys(mobile)
        if is_reset != None:
            self.reset_key_element().click()
            self.driver.find_element(By.XPATH, '//li/span[contains(text(), "{}")]'.format(is_reset)).click()
        if note != None:
            self.node_element().clear()
            self.node_element().send_keys(note)
        if bill_fields != None:
            self.email_fields_element().clear()
            self.email_fields_element().send_keys(bill_fields)
        time.sleep(1)
        if button == "确认":
            self.add_button_confirm_element().click()
            # logger.info('确认新增客户')
            ResultScreenShot(driver=self.driver).get_screen_shot("CustomerConfigPage")
        elif button == "取消":
            self.add_button_cancel_element().click()
            logger.info('取消新增客户')
            ResultScreenShot(driver=self.driver).get_screen_shot("CustomerConfigPage")
        else:
            logger.info("编辑弹窗中按钮是能是确认和取消")
        time.sleep(3)

    def add_customer_assert(self, assert_type, assert_message):
        print(assert_type, assert_message)
        if assert_type == 'input empty':
            customer_status_message = self.customer_status_error_message().text
            customer1_type_message = self.customer1_type_error_message().text
            pay_type_message = self.pay_type_error_message().text
            customer2_type_message = self.customer_type2_error_message().text
            customer_mark_message = self.customer_mark_error_message().text
            sale_message = self.sale_error_message().text
            private_key_message = self.private_key_error_message().text
            assert customer_status_message == assert_message
            assert customer1_type_message == assert_message
            assert pay_type_message == assert_message
            assert customer2_type_message == assert_message
            assert customer_mark_message == assert_message
            assert sale_message == assert_message
            assert private_key_message == assert_message
        elif assert_type == 'CustomerId error' or assert_type == 'input empty':
            customerId_message = self.customer_id_error_message().text
            assert customerId_message == assert_message
        elif assert_type == 'cusName error' or assert_type == 'input empty':
            computer_short_message = self.computer_short_error_message().text
            assert computer_short_message == assert_message
        elif assert_type == 'Customername error' or assert_type == 'input empty':
            computer_name_message = self.computer_name_error_message().text
            assert computer_name_message == assert_message
        elif assert_type == 'limit_items error':
            limit_items_message = self.limit_item_error_message().text
            assert limit_items_message == assert_message
        elif assert_type == 'money error':
            money_message = self.money_error_message().text
            assert money_message == assert_message
        elif assert_type == 'contact_name error' or assert_type == 'input empty':
            contact_name_message = self.contact_error_message().text
            assert contact_name_message == assert_message
        elif assert_type == 'email error' or assert_type == 'input empty':
            email_message = self.email_error_message().text
            assert email_message == assert_message
        elif assert_type == 'mobile error' or assert_type == 'input empty':
            mobile_message = self.mobile_error_message().text
            assert mobile_message == assert_message
        # elif assert_type == 'add success':
        #     email_message = GetTips(self.driver).get_tips()
        #     assert email_message == assert_message
        #     self.popup_close()
        else:
            print('断言类型错误！')

    def refresh_cache(self):
        time.sleep(2)
        self.refresh_cache_element().click()
        tips = GetTips(self.driver).get_tips()
        if tips == '刷新缓存成功':
            logger.info('缓存刷新成功')
        else:
            logger.info('缓存刷新失败')
        ResultScreenShot(driver=self.driver).get_screen_shot("CustomerConfigPage")

    def add_customers_button_assert(self, assert_message):
        self.add_customer_element().click()
        refresh_cache_message = self.find_element(By.XPATH,
                                                  '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[3]/div/div[1]/span').text
        print(refresh_cache_message)
        assert refresh_cache_message == assert_message
        logger.info('页面跳转到新增客户弹窗页面')
        ResultScreenShot(driver=self.driver).get_screen_shot("CustomerConfigPage")

    def operation(self, header_text, row_text, column_index):
        TableOperation(driver=self.driver).row_click(header_text=header_text, row_text=row_text,
                                                     column_index=column_index)
        ResultScreenShot(driver=self.driver).get_screen_shot("operation")
        logger.info('进行%s客户的%s操作', header_text, row_text)

    def popup_close(self):
        time.sleep(1)
        # self.add_customer_element().click()
        self.popup_close_element().click()
        logger.info('关闭弹窗')


if __name__ == '__main__':
    l = CustomerConfigPage()
    l.login_base()
    MultiMenuOperation(l.driver).select_menu('客户配置')
    l.popup_close()
    # l.search(customers_id='国信')
