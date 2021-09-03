import os
import unittest
import time
import HTMLTestRunner


class Main1(object):

    @staticmethod
    def get_case():
        current_path = os.path.dirname(os.path.dirname(__file__))
        case_path = current_path + r'/case'
        discover = unittest.defaultTestLoader.discover(case_path, 'Test*.py')
        return discover

    @staticmethod
    def get_report(all_case, report_path):
        if report_path is None:
            current_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
            print(current_path)
            report_path = current_path + r'\reports'
        else:
            report_path = report_path

        title = u'数尊宝自动化测试报告'
        now = time.strftime('%Y{y}%m{m}%d{d}%H{h}%M{M}%S{s}').format(y="年", m="月", d="日", h="时", M="分", s="秒")

        report_abspath = os.path.join(report_path, title + now + '.html')
        fp = open(report_abspath, 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                               title=title,
                                               description='数尊宝自动化测试报告！')
        runner.run(all_case)
        fp.close()

    def run_case(self, report_path=None):
        all_case = self.get_case()
        self.get_report(all_case, report_path)


if __name__ == '__main__':
    path = os.path.join(os.path.dirname(__file__)+'111')
    print(path)
    # Main1().run_case()
