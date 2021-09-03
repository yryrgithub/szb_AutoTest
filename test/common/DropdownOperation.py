import time


class DropdownOperation(object):

    def __init__(self, driver):
        self.driver = driver

    def select_dropdown_element(self):
        # return self.driver.find_element_by_class_name('el-select-dropdown__list')
        return self.driver.find_element_by_tag_name('ul')

    def select_dropdown(self, dropdown_value):
        time.sleep(2)
        # 获取下拉框中的全部li元素，list
        # self.driver.find_element_by_xpath('//div[contains(@class, "el-select--small")]/div[1]/span/span/i').click()
        pages = self.select_dropdown_element()
        print(pages)
        li_list = pages.find_elements_by_tag_name('li')
        # li_list = self.driver.find_element_by_xpath('//li/*[contains(text(),dropdown_value)]')
        # print(li_list.tag_name)
        # print(li_list.text)
        # li_list.click()
        length = len(li_list)
        print("list =", li_list[1].text)
        for i in range(0, length):
            if li_list[i].text == dropdown_value:
                li_list[i].click()
                print(i)
                time.sleep(1)
                break
        else:
            print('下拉列表无此值')


if __name__ == '__main__':
    pass
