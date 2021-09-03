import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from test.common.GetTips import GetTips
from test.common.TableOperation import TableOperation
from test.common.multiMenuOperation import MultiMenuOperation
from test.page.LoginPage import LoginPage
from utils.Logger import Logger
from utils.ResultScreenshot import ResultScreenShot

logger = Logger(logger='RoleManagementPage').get_log()


class RoleManagementPage(LoginPage):

    def add_role_button_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"flex-box operate-left")]/button[1]')

    def start_role_button_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"flex-box operate-left")]/button[2]')

    def stop_role_button_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"flex-box operate-left")]/button[3]')

    def delete_role_button_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"flex-box operate-left")]/button[4]')

    def check_box_element(self):
        return self.find_element(By.XPATH,
                                 '//table[contains(@class, "el-table__body")]/tbody/tr[1]/td[1]/div/label/span/span')

    def add_role_code_element(self):
        return self.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[1]/div/div/div/div[1]/input')

    def add_role_name_element(self):
        return self.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[2]/div/div/div/div[1]/input')

    def add_role_describe_element(self):
        return self.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[3]/div/div/div/div/input')

    def add_role_status_drop_element(self):
        return self.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[4]/div/div/div/div/div/input')

    def add_role_status_element(self):
        return self.find_elements(By.XPATH, '/html/body/div[5]/div[1]/div[1]/ul/li')

    def add_cancel_button_element(self):
        return self.find_element(By.XPATH,
                                 '//div[contains(@class, "container-absolute")]/div/div/div[3]/div/div[3]/div/button[1]')

    def add_confirm_button_element(self):
        return self.find_element(By.XPATH,
                                 '//div[contains(@class, "container-absolute")]/div/div/div[3]/div/div[3]/div/button[2]')

    def delete_confirm_button_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class, "el-message-box__btns")]/button[2]')

    def delete_cancel_button_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class, "el-message-box__btns")]/button[1]')

    def role_code_error_element(self):
        return self.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[1]/div/div/div/div[2]')

    def role_name_error_element(self):
        return self.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[2]/div/div/div/div[2]')

    def role_describe_error_element(self):
        return self.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[3]/div/div/div/div[2]')

    def pop_up_close(self):
        return self.find_element(By.XPATH,
                                 '//div[contains(@class, "container-absolute")]/div/div/div[3]/div/div[1]/button/i')
        logger.info("关闭弹窗")

    def get_table(self):
        time.sleep(1)
        # table、header、body_rows、body_rows_columns
        table_body = self.driver.find_element_by_id('table-container')
        table_rows = table_body.find_elements_by_tag_name('tr')
        return table_rows

    # 操作表格中的单选框，并返回行数
    def row_click(self, header_text, column_index):
        """选择表格中行并且点击"""
        time.sleep(2)
        table_rows = self.get_table()
        table_rows_length = len(table_rows)
        for i in range(1, table_rows_length):
            table_value = table_rows[i].find_elements_by_tag_name('td')[column_index]
            if table_value.text == header_text:
                table_operation = table_rows[i].find_element_by_tag_name('span')
                table_operation1 = table_rows[i].find_element_by_tag_name('input')
                if table_operation1.is_selected():
                    pass
                else:
                    table_operation.click()
                    logger.info("选中%s列进行操作", header_text)
                return i
        else:
            logger.info("未在表格中找到需要操作的元素")
            return False
            pass

    # 获取短暂弹出的提示文字信息
    # def get_tips(self):
    #     # 显示等待 获取短暂弹出提示的信息
    #     WebDriverWait(self.driver, 10).until(lambda x: x.find_element(By.XPATH, '//p[contains(@class,"el-message")]'))
    #     return self.find_element(By.XPATH, '//p[contains(@class,"el-message")]').text

    # 新增或修改角色输入操作
    def role_operation(self, role_name=None, role_describe=None, role_status=None, button=None):
        if role_name != None:
            self.add_role_name_element().clear()
            self.add_role_name_element().send_keys(role_name)
        else:
            self.add_role_name_element().click()
        if role_describe != None:
            self.add_role_describe_element().clear()
            self.add_role_describe_element().send_keys(role_describe)
        else:
            self.add_role_describe_element().click()
        self.add_role_status_drop_element().click()
        statuses = self.add_role_status_element()
        for i in range(len(statuses)):
            if statuses[i].text == role_status:
                statuses[i].click()
        if button == '确定':
            time.sleep(1)
            self.add_confirm_button_element().click()
        elif button == '取消':
            self.add_cancel_button_element().click()
        else:
            logger.info("此功能只支持确定和取消")

    # 新增角色
    def add_role(self, role_code=None, role_name=None, role_describe=None, role_status=None, button=None):
        self.add_role_button_element().click()
        if role_code != None:
            self.add_role_code_element().send_keys(role_code)
        else:
            self.add_role_code_element().click()
        self.role_operation(role_name=role_name, role_describe=role_describe, role_status=role_status, button=button)
        # self.add_role_check(role_name=role_name)

    # 判断新增角色是否成功新增到表里
    def add_role_check(self, role_name):
        # tips = self.get_tips()
        # if tips == '处理成功':
        MultiMenuOperation(self.driver).select_menu(menu_text='角色管理')
        result = self.row_click(header_text=role_name, column_index=1)
        if result:
            logger.info('新增角色成功或该角色已存在')
        else:
            logger.info('新增角色失败，页面中未查找到该角色')

    # 新增角色断言 特殊字符校验 不为空等
    def add_role_assert(self, assert_type, assert_message):
        time.sleep(1)
        if assert_type == 'code message empty' or assert_type == 'code message error':
            code_message = self.role_code_error_element().text
            assert code_message == assert_message
            ResultScreenShot(driver=self.driver).get_screen_shot(picture_name="code message empty")
            self.pop_up_close().click()
        elif assert_type == 'name message empty' or assert_type == 'name message error':
            name_message = self.role_name_error_element().text
            assert name_message == assert_message
            ResultScreenShot(driver=self.driver).get_screen_shot(picture_name="name message error")
            self.pop_up_close().click()
        elif assert_type == 'describe message empty' or assert_type == 'describe message error':
            describe_message = self.role_describe_error_element().text
            assert describe_message == assert_message
            ResultScreenShot(driver=self.driver).get_screen_shot(picture_name="describe message error")
            self.pop_up_close().click()
        elif assert_type == 'add success':
            ResultScreenShot(driver=self.driver).get_screen_shot(picture_name="add success")
            tips = GetTips(self.driver).get_tips()
            assert tips == assert_message
        elif assert_type == 'add fail':
            ResultScreenShot(driver=self.driver).get_screen_shot(picture_name="add fail")
            tips = GetTips(self.driver).get_tips()
            assert tips == assert_message
            self.pop_up_close().click()
        else:
            print('断言类型选择错误')
    time.sleep(1)

    # 启用角色功能
    def start_role(self, header_text, column_index):
        time.sleep(2)
        i = self.row_click(header_text, column_index)
        self.start_role_button_element().click()
        table_rows = self.get_table()
        status = table_rows[i].find_elements_by_tag_name('td')[4]
        print(status)
        tips = GetTips(self.driver).get_tips
        if tips == "操作成功" and status.text == "正常":
            logger.info("角色已正常启用")
        else:
            logger.info("角色启用异常")

    # 停用角色功能
    def stop_role(self, header_text, column_index):
        time.sleep(2)
        i = self.row_click(header_text, column_index)
        self.stop_role_button_element().click()
        table_rows = self.get_table()
        status = table_rows[i].find_elements_by_tag_name('td')[4]
        tips = GetTips(self.driver).get_tips()
        if tips == "操作成功" and status.text == "锁定":
            logger.info("角色已正常停用")
        else:
            logger.info("角色停用异常")

    # 删除角色功能
    def delete_role(self, header_text, column_index, button):
        role_value = self.row_click(header_text, column_index)
        if role_value:
            self.delete_role_button_element().click()
            if button == '确定':
                self.delete_confirm_button_element().click()
                self.role_operation_assert(opration='删除')
            elif button == '取消':
                self.delete_cancel_button_element().click()
            else:
                logger.info("此功能只支持确定和取消")
        else:
            logger.info('待删除角色%s不存在', header_text)

    # 修改功能
    def modify_operation(self, role_name, role_describe, role_status, header_text, button):
        l = TableOperation(self.driver).row_click(header_text=header_text, row_text='修改', column_index=2)
        print(l)
        self.role_operation(role_name=role_name, role_describe=role_describe, role_status=role_status, button=button)

    # 人员分配功能
    def personnel_allotment(self):
        pass

    # 权限分配功能
    def authority_assignment(self):
        pass


if __name__ == '__main__':
    l = RoleManagementPage()
    l.login_base()
    MultiMenuOperation(l.driver).select_menu(menu_text='角色管理')
    # l.add_role(role_code='fsf@#$%^', role_name='fsf@#$%', role_describe='fsf@#$%', role_status='锁定', button='确定')
    # MultiMenuOperation(l.driver).select_menu(menu_text='角色管理')
    # l.stop_role(header_text='11w', column_index=1)
    l.modify_operation(role_name='修改001', role_describe='修改测试', role_status='锁定', header_text='test002',
                                   button='确定')
