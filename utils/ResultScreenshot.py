import os
import time
from selenium import webdriver


class ResultScreenShot(object):

    def __init__(self, driver):
        self.driver = driver

    def get_screen_shot(self, picture_name):
        # time.sleep(2)
        picture_time = time.strftime("%H_%M_%S", time.localtime(time.time()))
        directory_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        # print(picture_time)
        # print(directory_time)
        try:
            current_path = os.path.dirname(os.path.dirname(__file__))
            File_Path = current_path + '/data/image' + '/' + directory_time + '/'
            if not os.path.exists(File_Path):
                os.makedirs(File_Path)
                print("目录新建成功：%s" % File_Path)
            else:
                print("目录已存在！！！")
        except BaseException as msg:
            print("新建目录失败：%s" % msg)

        try:
            url = self.driver.save_screenshot(File_Path + picture_name + picture_time + '.png')
            print("%s ：截图成功！！！" % url)
        except BaseException as pic_msg:
            print("截图失败：%s" % pic_msg)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://139.224.57.204:8080/index.html#/login")
    time.sleep(2)
    ResultScreenShot(driver=driver).get_screen_shot(picture_name="login")
