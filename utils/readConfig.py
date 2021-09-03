import json
import os


class ReadConfig(object):

    def __init__(self):
        pass

    def read_json(self, file_path):

        try:
            fp = open(file_path)
            data = json.load(fp)
            return data
        except:
            print("无数据或获取的文件非json格式")

        # 获取基础数据

    def get_account(self):
        current_path = os.path.dirname(os.path.dirname(__file__))
        print(current_path)
        file_path = current_path + '/settings/base_data.json'
        data = self.read_json(file_path)
        # return data["base_username"], data["base_password"], data["base_code"]
        return data

if __name__ == '__main__':
    file_path = '../settings/base_data.json'
    data = ReadConfig().read_json(file_path)
    l = ReadConfig().get_account()
    print(l)
    print(data)
    print(data['base_username'])
