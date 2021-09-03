# -*- coding: utf-8 -*-

import os
import time
import unittest
import HTMLTestRunner


class Main(object):
    @staticmethod
    def get_case():
        current_path = os.path.dirname(os.path.dirname(__file__))
        case_path = current_path + '/case/'
        discover = unittest.defaultTestLoader.discover(case_path, 'Test*.py')
        # print(discover)
        return discover

    @staticmethod
    def set_report(all_case, report_path=None):

        if report_path is None:
            current_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
            print(current_path)
            report_path = current_path + r'\reports'
        else:
            report_path = report_path
        # 输出的日期格式为2020-04-25 17:52:25时，会导致open带该格式日期的文件时报错
        # now = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        title = u'数尊宝后台管理系统自动化测试报告'
        now = time.strftime('%Y{y}%m{m}%d{d}%H{h}%M{M}%S{s}').format(y="年", m="月", d="日", h="时", M="分", s="秒")
        report_abspath = os.path.join(report_path, title + now + '.html')
        print(report_abspath)

        #  #-*- coding: utf-8 -*-  这句用于定义Python的默认编码格式。若代码或注释中含中文，python会使用unicode编码格式，这样会报错,python编程时最好习惯性地加上这句编码格式的声明。
        # fp = open("E:\\TestPython\\autoTestShuzunbao\\reports\\数尊宝后台管理系统2021年04月25日17时51分14秒.html", 'wb')
        fp = open(report_abspath, 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                               title=title,
                                               description="自动化测试报告")
        runner.run(all_case)
        fp.close()

    def run_case(self, report_path=None):
        all_case = self.get_case()
        self.set_report(all_case, report_path)


if __name__ == '__main__':
    Main().run_case()
