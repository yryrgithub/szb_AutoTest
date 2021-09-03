import os
import pandas as pd


class DownloadFile(object):

    def download_file_check(self, file1, sheet1, file2, sheet2):
        dt1 = pd.read_excel(file1, sheet1)
        dt2 = pd.read_excel(file2, sheet2)
        # data = dt1.head()
        data1 = dt1.ix[:]
        data2 = dt2.ix[:]
        # data1.q
        if data1.equals(data2):
            print('下载成功，文件数据正确')
        else:
            # different = data1[data1 != data2]
            # # different = pd.concat([data1,data2]).drop_duplicates()
            print('下载失败，文件数据错误:')
        # print(data1)
        # print(dt1)

    def get_download_file(self, report_path):
        # report_path = 'E:\\TestPython\\autoTestShuzunbao\\download\\ComparisonDocument'
        lists = os.listdir(report_path)
        # print(lists)
        lists.sort(key=lambda fn: os.path.getmtime(report_path+"/"+fn))
        files_path = os.path.join(report_path, lists[-1])
        xls = pd.ExcelFile(files_path)
        sheet = xls.sheet_names[0]
        # print(files_path)
        # print(sheet)
        return files_path, sheet


if __name__ == '__main__':
    DownloadFile().get_download_file()
    # DownloadFile().get_download_file_sheet_name()