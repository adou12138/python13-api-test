# python_13 
# test_debug 
# shen 
# 2019/1/11 20:47 

import logging
# 导入配置文件
from common import contants
from conf.test_api_config import ReadConfig
in_level = ReadConfig(contants.api_conf_file).get_value('LOG', 'in_level')
out_level = ReadConfig(contants.api_conf_file).get_value('LOG', 'out_level')
file_level = ReadConfig(contants.api_conf_file).get_value('LOG', 'file_level')
file_name = ReadConfig(contants.api_conf_file).get_value('LOG', 'file_name')
file_path = eval(ReadConfig(contants.api_conf_file).get_value('LOG', 'file_path'))
data_formatter = ReadConfig(contants.api_conf_file).get_value('LOG', 'formatter')

import os
# current_path = os.getcwd()
# report_path = os.path.join(current_path, "Report")

class MyLog:
    '这个是一个日志类'
    # def __init__(self, in_level, out_level, file_level, file_path, formatter):  # 传入配置文件信息
    #     self.in_level = in_level
    #     self.out_level = out_level
    #     self.file_level = file_level
    #     self.file_path = file_path
    #     self.formatter = formatter

    def my_log(self, out_level, msg):
        # 写一个属于自己的日志系统 收集器和输出渠道取交集显示日志信息
        # 收集器 --- 创建一个日志收集器 getLogger 函数 第一次过滤 先收集
        my_logger = logging.getLogger(file_name)  # 创建一个日志收集器
        my_logger.setLevel(in_level)  # 给这个日志收集器 设置级别setLevel()

        # 格式：规定日志输出的格式 自己拓展下
        formatter = logging.Formatter(data_formatter)
        # formatter = logging.Formatter('[%(asctime)s] - '  # 当前系统时间
        #                               '[%(levelname)s] - '  # 日志信息级别
        #                               '[%(filename)s] - '  # 当前日志所在的文件名、模块名级别
        #                               '[line: %(lineno)d] - '  # 出错的行数
        #                               '[%(name)s] - '  # 日志收集器名字
        #                               '[日志信息]: %(message)s')  # 日志输出的信息

        # 输出渠道 --- 指定输出渠道 第二次过滤 再输出
        ch = logging.StreamHandler()  # 创建一个输出到控制台的渠道
        ch.setLevel(out_level)  # 给渠道设置级别 如果不给级别，就会占用控制台 console 的渠道
        ch.setFormatter(formatter)

    # def out_put_info(self, file_path,out_level):
        # 输出到指定的文件 文件路径 绝对路径 相对路径 都可以用
        fh = logging.FileHandler(os.path.join(file_path, file_name), encoding='utf-8')
        fh.setLevel(file_level)
        fh.setFormatter(formatter)

        # 对接 日志收集器与输出渠道 进行对接  # !!!查看这里的视频说明
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        if out_level == 'DEBUG':
            my_logger.debug(msg)
        elif out_level == 'INFO':
            my_logger.info(msg)
        elif out_level == 'WARNING':
            my_logger.warning(msg)
        elif out_level == 'ERROR':
            my_logger.error(msg)
        else:
            my_logger.critical(msg)

        # 去掉日志的重复 每次收集完毕之后 记得移除掉日志收集器
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self, msg):  # 输出一条debug级别的信息
        self.my_log('DEBUG', msg)

    def info(self, msg):  # 输出一条info级别的信息
        self.my_log('INFO', msg)

    def warning(self, msg):  # 输出一条warning级别的信息
        self.my_log('WARNING', msg)

    def error(self, msg):  # 输出一条error级别的信息
        self.my_log('ERROR', msg)

    def critical(self, msg):  # 输出一条error级别的信息
        self.my_log('CRITICAL', msg)

if __name__ == '__main__':
    My_logger = MyLog()
    My_logger.debug('w 警告nn222')

