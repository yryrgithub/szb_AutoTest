# from selenium import webdriver
# import time
#
# driver = webdriver.Chrome()
# driver.get('C://Users/SHUZUN/Desktop/1.html')
# upload = driver.find_element_by_id('file')
# time.sleep(5)
# upload.send_keys('F://login.csv')  # send_keys
# print (upload.get_attribute('value'))  # check value

# driver.quit()

from selenium import webdriver
import win32gui
import win32con
import time

dr = webdriver.Chrome()
dr.get('C://Users/SHUZUN/Desktop/1.html')
time.sleep(2)
upload = dr.find_element_by_id('file2')
upload.click()
time.sleep(1)

# win32gui
dialog = win32gui.FindWindow('#32770', '文件上传')  # 对话框
ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button

win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, 'F://login.csv')  # 往输入框输入绝对地址
win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button

print (upload.get_attribute('value'))
# dr.quit()