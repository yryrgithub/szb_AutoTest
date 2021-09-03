import time

import win32con
import win32gui
from selenium.webdriver.common.by import By

from test.page.LoginPage import LoginPage
from test.common.multiMenuOperation import MultiMenuOperation
from test.common.TableOperation import TableOperation
from test.common.GetTips import GetTips


class CustomerChargingPage(LoginPage):
    # 充值按钮元素定位
    def add_charging_button_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"operate-left")]/button')

    # 主页客户id下拉列表元素定位
    def customer_id_dropdown_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"operate-right")]/span/div')

    # 主页查询按钮元素定位
    def charging_search_button_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"operate-right")]/button')

    # 充值弹窗页客户id下拉列表元素定位
    def add_customer_id_dropdown_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[1]/div[1]//input')

    # 交易流水号输入框元素定位
    def charge_number_input_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[3]/div[1]//input')

    def charging_time_input_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[3]/div[2]//input')

    def charging_input_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[4]/div[1]//input')

    def note_input_element(self):
        return self.find_element(By.XPATH, '//div[contains(@class,"el-dialog__body")]/form/div[4]/div[2]//input')

    def add_const_cancel_button_element(self):
        return self.find_element(By.XPATH,
                                 '//div[contains(@class,"default-container")]/div[2]//div[3]//div[3]//button[1]')

    def add_charging_confirm_button_element(self):
        return self.find_element(By.XPATH,
                                 '//div[contains(@class,"default-container")]/div[2]//div[3]//div[3]//button[2]')

    def start_time_input_element(self):
        return self.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[3]/div[2]/div/div/div[1]/input')

    def add_charge_input_element(self):
        return self.find_element(By.XPATH, '//form[contains(@class, "el-form")]/div[4]/div[1]/div/div/div[1]/input')

    def select_customer_id(self):
        self.add_customer_id_dropdown_element().click()
        self.find_element(By.XPATH, '//li/span[text()="DS_C0009_1"]').click()

    def input_charge_number(self):
        self.charge_number_input_element().clear()
        self.charge_number_input_element().send_keys('1')

    def input_start_time(self):
        self.start_time_input_element().clear()
        self.start_time_input_element().send_keys('2021-06-29')
        time.sleep(1)
        self.find_element(By.XPATH, '//*[contains(text(), "充值时间：")]').click()

    def input_charge(self):
        self.add_charge_input_element().clear()
        self.add_charge_input_element().send_keys('22')

    def input_note(self):
        self.note_input_element().clear()
        self.note_input_element().send_keys('sdddff')

    def add_charging(self, button):
        self.add_charging_button_element().click()
        self.input_charge_number()
        self.input_start_time()
        self.input_charge()
        self.input_note()
        self.file_upload()
        if button == "取消":
            self.add_const_cancel_button_element().click()
        elif button == "确定":
            self.add_charging_confirm_button_element().click()
        else:
            print("只支持确定或取消功能")

    def search_charging(self):
        self.charging_search_button_element().click()

    def file_upload(self):
        upload = self.find_element(By.XPATH, '//button[contains(@class, "btn-upload")]/span')
        upload.click()
        time.sleep(2)
        # win32gui  查找窗口句柄 '#32770'：窗口的类名， '打开'：窗口的标题，
        dialog = win32gui.FindWindow('#32770', u'打开')
        '''LRESULT SendMessage(    
                                HWND hWnd,     
                                UINT Msg,     
                                WPARAM wParam,     
                                LPARAM lParam   
                                ); 
        hWnd：其窗口程序将接收消息的窗口的句柄。如果此参数为HWND_BROADCAST，则消息将被发送到系统中所有顶层窗口，包括无效或不可见的非自 身拥有的窗口、被覆盖的窗口和弹出式窗口，但消息不被发送到子窗口。
        Msg：指定被发送的消息。
        wParam：指定附加的消息指定信息。
        IParam：指定附加的消息指定信息。                        
        '''
        dialog = win32gui.FindWindow('#32770', '打开')  # 对话框
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
        button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button

        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, 'F:\login.csv')  # 往输入框输入绝对地址
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button

        print(upload.get_attribute('value'))


if __name__ == '__main__':
    l = CustomerChargingPage()
    l.login_base()
    MultiMenuOperation(l.driver).select_menu("客户充值")
    # l.file_upload()
    # l.add_charging('取消')
    l.add_charging('确定')
