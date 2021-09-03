import logging
import os
import time


class Logger(object):

    def __init__(self, logger):
        current_path = os.path.dirname(os.path.realpath(__file__))
        log_path = os.path.join(os.path.dirname(current_path), 'logs')
        # 判断log_path是否存在，不存在时新建一个
        if not os.path.exists(log_path): os.mkdir(log_path)

        # 创建一个logger，日志级别为DEBUG
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        log_time = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        log_name = os.path.join(log_path, '%s.log' % log_time)
        # 创建Handdler,用于输出到log文件中
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)
        # 创建Handdler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def get_log(self):
        return self.logger


if __name__ == '__main__':
    logger = Logger(logger='TestMyLog').get_log()
    logger.info('logceshi')
