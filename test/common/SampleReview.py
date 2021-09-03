import time

from selenium.webdriver.common.by import By

from test.common.TableOperation import TableOperation
from test.common.GetTips import GetTips


class SampleReview(object):

    def __init__(self, driver):
        self.driver = driver

    def sample_number_input_element(self):
        return self.driver.find_element(By.XPATH, '//div[contains(@class, "el-input--small")]/input')

    def sample_search_button_element(self):
        return self.driver.find_element(By.XPATH, '//button[contains(@class, "query-button")]')

    def review_result_input_element(self):
        return self.driver.find_element(By.XPATH,
                                        '//form[contains(@class, "el-form")]/div[3]/div[2]/div/div/div[1]/textarea')

    def note_input_element(self):
        return self.driver.find_element(By.XPATH,
                                        '//form[contains(@class, "el-form")]/div[4]/div[1]/div/div/div[1]/textarea')

    def replay_sample_confirm_button_element(self):
        return self.driver.find_element(By.XPATH,
                                        '//div[contains(@class, "container-absolute")]/div/div/div[3]/div/div[3]/div/button[2]')

    def reply_sample_cancel_button_element(self):
        return self.driver.find_element(By.XPATH,
                                        '//div[contains(@class, "container-absolute")]/div/div/div[3]/div/div[3]/div/button[1]')

    def sample_search(self, sample_number):
        self.sample_number_input_element().send_keys(sample_number)
        self.sample_search_button_element().click()

    def download_sample(self):
        TableOperation(self.driver).row_click('bonc_20210806111751', '异议附件', 0)
        tips = GetTips(self.driver).get_tips()
        if tips == '无异议附件':
            print('工单中无附件')
        else:
            print('附件下载成功')

    def upload_sample(self):
        time.sleep(2)
        TableOperation(self.driver).row_click('bonc_20210806111751', '回复附件', 0)
        tips = GetTips(self.driver).get_tips()
        if tips == '无下载附件':
            print('工单中无附件')
        else:
            print('附件下载成功')

    def sample_reply(self, review_result, note, button):
        text = TableOperation(self.driver).row_click('bonc_20210806111751',  '回复', 0)
        if text == '已回复':
            TableOperation(self.driver).row_click('bonc_20210806111751', '回复', 0)
            tips = GetTips(self.driver).get_tips()
            assert text == tips
        else:
            self.review_result_input_element().send_keys(review_result)
            self.note_input_element().send_keys(note)
            if button == '确定':
                self.replay_sample_confirm_button_element().click()
            elif button == '取消':
                self.reply_sample_cancel_button_element().click()
            else:
                print('只能是确定或取消按钮')
