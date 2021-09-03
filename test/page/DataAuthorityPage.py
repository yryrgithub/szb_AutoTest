import time

from selenium.webdriver.common.by import By

from test.page.LoginPage import LoginPage
from utils.Logger import Logger
from test.common.multiMenuOperation import MultiMenuOperation

logger = Logger(logger='DataAuthorityPage').get_log()


class DataAuthorityPage(LoginPage):

    def data_authority_button_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class, "operate-left")]/button[1]')

    def delete_button_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class, "operate-left")]/button[2]')

    def search_button_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"operate-right")]//button')

    def user_id_drop_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"operate-right")]//div[1]/div')

    def customer_id_drop_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"operate-right")]//div[2]/div/input')

    def get_table(self):
        table = self.find_element(By.ID, 'table-container')
        return table.find_elements_by_tag_name('tr')

    def select_row(self, header_text, column_index):
        rows = self.get_table()
        length = len(rows)
        for i in range(1, length):
            headers = rows[i].find_elements_by_tag_name('td')[column_index]
            if headers.text == header_text:
                table_operation1 = rows[i].find_element_by_tag_name('span')
                table_operation = rows[i].find_element_by_tag_name('input')
                if table_operation.is_selected():
                    pass
                else:
                    table_operation1.click()
                    logger.info("选中%s列进行操作", header_text)
            return i
        else:
            logger.info("未在表格中找到需要操作的元素")
            return False
            pass

    def search_message_select(self, user_id):
        self.user_id_drop_element().click()
        time.sleep(1)
        users_id = self.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul')
        # customers_id = self.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul')
        users_id_drop = users_id.find_elements_by_tag_name('li')
        # customers_id_drop = customers_id.find_elements_by_tag_name('li')
        length = len(users_id_drop)
        for i in range(length):
            if users_id_drop[i].text == user_id:
                users_id_drop[i].click()
                break
            else:
                pass

    def search_message_select1(self, customer_id):
        time.sleep(2)
        self.customer_id_drop_element().click()
        time.sleep(1)
        # self.find_element(By.XPATH, "//li//span[text()='{}']".format(customer_id)).click()
        f = self.find_element(By.XPATH, "//li//span[text()='bonc']")
        self.driver.execute_script('arguments[0].click()', f)
        print(f)

        # customers_id = self.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul')
        # # customers_id = self.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul')
        # customer_id_drop = customers_id.find_elements_by_tag_name('li')
        # # customers_id_drop = customers_id.find_elements_by_tag_name('li')
        # length = len(customer_id_drop)
        # for j in range(length):
        #     if customer_id_drop[j].text == customer_id:
        #         customer_id_drop[j].click()
        #         break
        #     else:
        #         pass

    def search(self, user_id, customer_id):
        self.search_message_select(user_id=user_id)
        self.search_message_select1(customer_id=customer_id)
        self.search_button_element().click()
        result = self.select_row(header_text=user_id, column_index=1)
        if result:
            logger.info("成功查询到用户")
        else:
            logger.info("未查询到用户信息")


if __name__ == '__main__':
    l = DataAuthorityPage()
    l.login_base()
    MultiMenuOperation(l.driver).select_menu(menu_text='数据权限')
    # l.select_row(header_text='admin', column_index=1)
    l.search(user_id='bonc', customer_id='bonc')
