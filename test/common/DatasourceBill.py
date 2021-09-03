from selenium.webdriver.common.by import By


class DatasourceBill(object):

    def __init__(self, driver):
        self.driver = driver

    def start_time_input_element(self):
        self.driver.find_element(By.XPATH, '//div[contains(@class, "el-range-editor")]/input[1]')

    def end_time_input_element(self):
        self.driver.find_element(By.XPATH, '//div[contains(@class, "el-range-editor")]/input[2]')

    def search_button_element(self):
        self.driver.find_element(By.XPATH, '//div[contains(@class, "operate-right")]/button[1]')

    def download_button_element(self):
        self.driver.find_element(By.XPATH, '//div[contains(@class, "operate-right")]/button[2]')

    def select_time(self, start_time, end_time):
        self.start_time_input_element().send_key(start_time)
        self.end_time_input_element().send_key(end_time)

    def search(self):
        self.search_button_element().click()

    def download(self):
        self.download_button_element().click()



