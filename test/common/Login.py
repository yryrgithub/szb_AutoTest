from selenium.webdriver.common.by import By
from utils.Logger import Logger

logger = Logger(logger='LoginPage').logger


class Login(object):

    def __init__(self, driver):
        self.driver = driver

    def username_element(self):
        return self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/form/div[1]/div/div[1]/input')

    def password_element(self):
        return self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/form/div[2]/div/div[1]/input')

    def username_error_text_element(self):
        return self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/form/div[1]/div/div[2]')

    def password_error_text_element(self):
        return self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/form/div[2]/div/div[2]')

    def code_element(self):
        return self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/form/div[3]/div/div/input')

    def login_button_element(self):
        return self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/form/button')

    def check_box_element(self):
        return self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/form/div[4]/label/span[1]/span')

    def get_code_element(self):
        return self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/form/div[3]/div/div/span/span/button')

    def username_input(self, username):
        self.username_element().send_keys(username)

    def username_input_clear(self):
        self.username_element().clear()

    def password_input(self, password):
        self.password_element().send_keys(password)

    def password_input_clear(self):
        self.password_element().clear()

    def code_input(self, code):
        self.code_element().send_keys(code)

    def code_input_clear(self):
        self.code_element().clear()

    def login_button(self):
        self.login_button_element().click()

    def username_input_error_message(self):
        return self.username_error_text_element().text

    def password_input_error_message(self):
        return self.password_error_text_element().text


if __name__ == '__main__':
    # 读取json基本配置中的用户信息进行登录，用于测试登录成功进入主页的其他功能
    # LoginPage().login_base()
    # 读取excel中的用户信息进行登录，用于测试登录功能
    pass
