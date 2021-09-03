from selenium.webdriver.common.by import By


class PopupClose(object):

    def __init__(self, driver):
        self.driver = driver

    def popup_close_element(self):
        return self.driver.find_element(By.XPATH,
                                        '//div[contains(@class, "container-absolute")]//div[3]/div/div[1]/button')

    def popup_close(self):
        self.popup_close_element().click()
