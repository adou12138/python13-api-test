# coding: utf-8
# python13-api-test 
# contants 
# shen 
# 2019/1/18 22:19

import os
# 项目地址
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(base_dir)

# common 地址
common_dir = os.path.join(base_dir, "common")
# print(common_dir)
do_excel_file = os.path.join(common_dir, "do_excel.py")
# print(do_excel_file)
request_file = os.path.join(common_dir, "request.py")
# print(request_file)

# conf 目录地址
conf_dir = os.path.join(base_dir, "conf")
# print(conf_dir)
api_config_file = os.path.join(conf_dir, "test_api_config.py")
# print(api_config_file)
api_conf_file = os.path.join(conf_dir, "test_api.conf")
# print(api_conf_file)

# datas 目录地址
data_dir = os.path.join(base_dir, "datas")
# print(data_dir)
excel_file = os.path.join(data_dir, "luckytest.xlsx")
# print(excel_file)

# log 目录地址
log_dir = os.path.join(base_dir, "log")
# print(log_dir)
log_config_file = os.path.join(log_dir, "test_api_log.py")
# print(log_config_file)
log_log_file = os.path.join(log_dir, "luckytestlog.log")
# print(log_log_file)

# report 目录地址
reports_dir = os.path.join(base_dir, "reports")
# print(reports_dir)
test_api_method_suite_file = os.path.join(reports_dir, "test_api_method_suite.py")
# print(test_api_method_suite_file)
report_file = os.path.join(reports_dir, "luckytest.html")
# print(report_file)

# test_cases 目录地址
test_cases_dir = os.path.join(base_dir, "test_cases")
# print(test_cases_dir)
api_method_file = os.path.join(test_cases_dir, "api_method.py")
# print(api_method_file)
test_api_method_file = os.path.join(test_cases_dir, "test_api_method.py")
# print(test_api_method_file)


