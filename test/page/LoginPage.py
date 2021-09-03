import time

from test.common.GetTips import GetTips
from test.page.BasePage import BasePage
from utils.ResultScreenshot import ResultScreenShot
from utils.readConfig import ReadConfig
from utils.Logger import Logger
from test.common.Login import Login
logger = Logger(logger='LoginPage').logger


class LoginPage(BasePage):

    # 基础登录，用于登录后其他页面测试
    def login_base(self):
        time.sleep(1)
        # username, password, code = ReadConfig().get_account()
        data = ReadConfig().get_account()
        username, password, code = data["base_username"], data["base_password"], data["base_code"]
        Login(self.driver).username_input_clear()
        Login(self.driver).username_input(username)
        Login(self.driver).password_input_clear()
        Login(self.driver).password_input(password)
        Login(self.driver).code_input_clear()
        Login(self.driver).code_input(code)
        Login(self.driver).login_button()
        logger.info("登录成功，页面进入系统首页")
        time.sleep(2)

    # 登录页测试，用于用户信息正常及异常情况测试
    def login_excel(self, username=None, password=None, code=None):
        if username != None:
            Login(self.driver).username_input_clear()
            Login(self.driver).username_input(username)
        if password != None:
            Login(self.driver).password_input_clear()
            Login(self.driver).password_input(password)
        if code != None:
            Login(self.driver).code_input_clear()
            Login(self.driver).code_input(code)
        time.sleep(1)
        Login(self.driver).login_button()

    # 登录断言
    def assert_login_excel(self, assert_type, assert_message):
        time.sleep(1)
        if assert_type == 'username empty':
            username_message = Login(self.driver).username_input_error_message()
            assert username_message == assert_message
            ResultScreenShot(driver=self.driver).get_screen_shot(picture_name="username error")
        elif assert_type == 'password empty':
            password_message =Login(self.driver).password_input_error_message()
            assert password_message == assert_message
            ResultScreenShot(driver=self.driver).get_screen_shot(picture_name="password error")
        elif assert_type == 'username error' or assert_type == 'password error' or assert_type == 'code error':
            tips_message = GetTips(self.driver).get_tips()
            assert tips_message == assert_message
            ResultScreenShot(driver=self.driver).get_screen_shot(picture_name="login fail")
        elif assert_type == 'login success':
            login_message = self.driver.switch_to.alert.text
            assert login_message == assert_message
            ResultScreenShot(driver=self.driver).get_screen_shot(picture_name="login success")
            # self.driver.refresh()
            time.sleep(2)
        else:
            logger.info('断言类型选择错误')

    time.sleep(1)


if __name__ == '__main__':
    # 读取json基本配置中的用户信息进行登录，用于测试登录成功进入主页的其他功能
    # LoginPage().login_base()
    # 读取excel中的用户信息进行登录，用于测试登录功能
    LoginPage().login_base()
