# coding: utf-8
# python13-api-test 
# logger 
# shen 
# 2019/2/13 22:39 

import logging
import logging.handlers
from common import contants
import os
from common.test_api_config import ReadConfig

config = ReadConfig()
in_level = eval(config.get_value('LogNew', 'in_level'))
out_level = eval(config.get_value('LogNew', 'out_level'))
file_out_level = eval(config.get_value('LogNew', 'file_out_level'))
data_formatter = config.get_value('LogNew', 'fmt')

# 输出到文件，文件路径请使用绝对路径 logs
# 输出到控制台，定义输出级别debug
# 不同的输出级别可配置

def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(in_level)
    # 定义输出格式

    # fmt = '[%(asctime)s] - '  # 当前系统时间
    # '[%(levelname)s] - '  # 日志信息级别
    # '[%(filename)s] - '  # 当前日志所在的文件名、模块名级别
    # '[line: %(lineno)d] - '  # 出错的行数
    # '[%(name)s] - '  # 日志收集器名字
    # '[日志信息]: %(message)s' # 日志输出的信息
    fmt =data_formatter
    formate = logging.Formatter(fmt)

    file_name = contants.api_log_file
    file_handler = logging.handlers.RotatingFileHandler(file_name, maxBytes=20*1024*1024, backupCount=10)
    file_handler.setLevel(file_out_level)
    file_handler.setFormatter(formate)

    # 输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(out_level)

    logger.addHandler(file_handler)
    logger.addHandler(ch)

    return logger

if __name__ == '__main__':
    logger = get_logger(logger_name='invest')
    logger.error('this is error')
    logger.info('this is info')