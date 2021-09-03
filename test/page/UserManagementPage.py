import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from test.common.TableOperation import TableOperation
from test.common.multiMenuOperation import MultiMenuOperation
from test.page.LoginPage import LoginPage
from utils.Logger import Logger

logger = Logger(logger='RoleManagementPage').get_log()


class UserManagementPage(LoginPage):

    def add_button_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class, "operate-left")]/button')

    def search_input_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class, "query-item")]/input')

    def search_button_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class, "operate-right")]/button')

    def user_id_element(self):
        return self.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[1]/div[1]/div/div/div[1]/input')

    def belonger_element(self):
        return self.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[1]/div[2]/div/div/div[1]/input')

    def mobile_element(self):
        return self.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[2]/div[1]/div/div/div[1]/input')

    def email_element(self):
        return self.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[2]/div[2]/div/div/div[1]/input')

    def user_password_element(self):
        return self.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[3]/div[1]/div/div/div[1]/input')

    def status_drop_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class, "el-select--medium")]/div[1]/input')

    def status_elements(self):
        return self.find_elements(By.XPATH, '/html/body/div[5]/div[1]/div[1]/ul/li')

    def userid_error_message_element(self):
        return self.find_element(By.XPATH ,'//form[contains(@class, "el-form")]/div[1]/div[1]/div/div/div[2]')

    def belonger_error_message_element(self):
        return self.find_element(By.XPATH ,'//form[contains(@class, "el-form")]/div[1]/div[2]/div/div/div[2]')

    def mobile_error_message_element(self):
        return self.find_element(By.XPATH ,'//form[contains(@class, "el-form")]/div[2]/div[1]/div/div/div[2]')

    def email_error_message_element(self):
        return self.find_element(By.XPATH ,'//form[contains(@class, "el-form")]/div[2]/div[2]/div/div/div[2]')

    def user_password_error_message_element(self):
        return self.find_element(By.XPATH ,'//form[contains(@class, "el-form")]/div[3]/div[1]/div/div/div[2]')

    def add_confirm_button_element(self):
        return self.find_element(By.XPATH,
                                 '//div[contains(@class, "container-absolute")]/div/div/div[3]/div/div[3]/div/button[2]')

    def add_cancel_button_element(self):
        return self.find_element(By.XPATH,
                                 '//div[contains(@class, "container-absolute")]/div/div/div[3]/div/div[3]/div/button[1]')

    def pop_up_close(self):
        return self.find_element(By.XPATH,
                                 '//div[contains(@class, "container-absolute")]/div/div/div[3]/div/div[1]/button/i')

    def get_table(self):
        time.sleep(1)
        # table、header、body_rows、body_rows_columns
        table_body = self.find_element(By.ID, 'table-container')
        table_rows = table_body.find_elements(By.TAG_NAME, 'tr')
        return table_rows

    # 操作表格中的单选框，并返回行数
    def row_click(self, header_text, column_index):
        """选择表格中行并且点击"""
        time.sleep(2)
        table_rows = self.get_table()
        table_rows_length = len(table_rows)
        for i in range(1, table_rows_length):
            table_value = table_rows[i].find_elements(By.TAG_NAME, 'td')[column_index]
            if table_value.text == header_text:
                table_operation = table_rows[i].find_element(By.TAG_NAME, 'div')
                if table_operation.text == header_text:
                    return i
                else:
                    return False
        else:
            pass

        # 获取短暂弹出的提示文字信息

    def get_tips(self):
        # 显示等待 获取短暂弹出提示的信息
        WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element(By.XPATH, '//p[contains(@class,"el-message")]'))
        return self.find_element(By.XPATH, '//p[contains(@class,"el-message")]').text

    def add_user(self, userid=None, belonger=None, mobile=None, email=None, password=None, status=None, button=None):
        self.add_button_element().click()
        if userid != None:
            self.user_id_element().clear()
            self.user_id_element().send_keys(userid)
        if belonger != None:
            self.belonger_element().clear()
            self.belonger_element().send_keys(belonger)
        if mobile != None:
            self.mobile_element().clear()
            self.mobile_element().send_keys(mobile)
        if email != None:
            self.email_element().clear()
            self.email_element().send_keys(email)
        if password != None:
            self.user_password_element().clear()
            self.user_password_element().send_keys(password)
        # self.status_element().send_keys(status)
        self.status_drop_element().click()
        statuses = self.status_elements()
        for i in range(len(statuses)):
            if statuses[i].text == status:
                statuses[i].click()
        if button == '确定':
            time.sleep(1)
            self.add_confirm_button_element().click()
        elif button == '取消':
            self.add_cancel_button_element().click()
        else:
            logger.info("此功能只支持确定和取消")

    def search_user(self, userid):
        self.search_input_element().send_keys(userid)
        self.search_button_element().click()
        time.sleep(2)
        result = self.row_click(header_text=userid, column_index=0)
        if result:
            logger.info("已查询到用户信息")
        else:
            logger.info("未查询到用户信息")

    def modify_user(self, belonger=None, mobile=None, email=None, status=None,
                    button=None):
        TableOperation(self.driver).row_click(header_text='rui.yang', row_text='修改', column_index=0)
        # self.add_button_element().click()
        if belonger != None:
            self.belonger_element().clear()
            self.belonger_element().send_keys(belonger)
        if mobile != None:
            self.mobile_element().clear()
            self.mobile_element().send_keys(mobile)
        if email != None:
            self.email_element().clear()
            self.email_element().send_keys(email)
        # self.status_element().send_keys(status)
        self.status_drop_element().click()
        statuses = self.status_elements()
        for i in range(len(statuses)):
            if statuses[i].text == status:
                statuses[i].click()
        if button == '确定':
            time.sleep(1)
            self.add_confirm_button_element().click()
        elif button == '取消':
            self.add_cancel_button_element().click()
        else:
            logger.info("此功能只支持确定和取消")

    def add_user_assert(self, assert_type, assert_message):
        if assert_type == 'userid empty' or assert_type == 'userid error':
            userid_message = self.userid_error_message_element().text
            assert userid_message == assert_message
            self.pop_up_close().click()
        elif assert_type == 'belonger empty' or assert_type == 'belonger error':
            belonger_message = self.belonger_error_message_element().text
            assert belonger_message == assert_message
            self.pop_up_close().click()
        elif assert_type == 'moblie empty' or assert_type == 'moblie error':
            moblie_message = self.mobile_error_message_element().text
            assert moblie_message == assert_message
            self.pop_up_close().click()
        elif assert_type == 'email empty' or assert_type == 'email error':
            email_message = self.email_error_message_element().text
            assert email_message == assert_message
            self.pop_up_close().click()
        elif assert_type == 'password empty':
            password_message = self.user_password_error_message_element().text
            assert password_message == assert_message
            self.pop_up_close().click()
        elif assert_type == 'add success':
            tips = self.get_tips()
            assert tips == assert_message
            self.pop_up_close().click()
        elif assert_type == 'add fail':
            tips = self.get_tips()
            assert tips == assert_message
            self.pop_up_close().click()
        else:
            logger.info('断言类型错误')


    def delete_user(self):
        pass


if __name__ == '__main__':
    l = UserManagementPage()
    l.login_base()
    MultiMenuOperation(l.driver).select_menu(menu_text='用户管理')
    # l.add_user(userid='admin2', belonger='admin2', mobile='13333300001', email='rui.yang@shuzun.net', password='123456',
    #            status='正常', button='确定')
    l.search_user(userid='rui.yang')
    l.modify_user(belonger='admin2', mobile='13333300001', email='rui.yang@shuzun.net', status='正常', button='确定')
