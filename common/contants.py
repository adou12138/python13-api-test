# coding: utf-8
# python13-api-test 
# contants 
# shen 
# 2019/1/18 22:19

import os
# 项目地址
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.abspath(__file__))
# print(base_dir)

# common 地址
common_dir = os.path.join(base_dir, "common")
do_excel_file = os.path.join(common_dir, "do_excel.py")
do_excel_study_file = os.path.join(common_dir, "do_excel_study.py")
mysql_file = os.path.join(common_dir, "mysql.py")
request_file = os.path.join(common_dir, "request.py")
test_api_config_file = os.path.join(common_dir, "test_api_config.py")
log_config_file = os.path.join(common_dir, "logger.py")

# conf 目录地址
conf_dir = os.path.join(base_dir, "conf")
global_api_conf_file = os.path.join(conf_dir, "global.conf")
test_api_conf_file = os.path.join(conf_dir, "test_api.conf")
test_api2_conf_file = os.path.join(conf_dir, "test_api2.conf")

# datas 目录地址
data_dir = os.path.join(base_dir, "datas")
excel_file = os.path.join(data_dir, "luckytest.xlsx")
json_test_file = os.path.join(data_dir, "json_test.json")
try_json_file = os.path.join(data_dir, "try_json.py")


# log 目录地址
log_dir = os.path.join(base_dir, "log")
log_config_file = os.path.join(log_dir, "test_api_log.py")
test_api_log_file = os.path.join(log_dir, "luckytestlog.log")
api_log_file = os.path.join(log_dir, "case.log")

# report 目录地址
reports_dir = os.path.join(base_dir, "reports")
test_api_method_suite_file = os.path.join(reports_dir, "test_api_method_suite.py")
report_file = os.path.join(reports_dir, "luckytest.html")
# report_file = os.path.join(reports_dir, "luckytest")  # 时间戳使用
# print(report_file)

# test_cases 目录地址
test_cases_dir = os.path.join(base_dir, "test_cases")
api_method_file = os.path.join(test_cases_dir, "api_method.py")
test_api_method_file = os.path.join(test_cases_dir, "test_api_method.py")
test_api_register_file = os.path.join(test_cases_dir, "test_api_register.py")

# htmlreport 目录地址 废弃不用
# html_reports_dir = os.path.join(base_dir, "htmlreports")
# html_report_file = os.path.join(html_reports_dir, "luckytest.html")

# sqlconfirm目录地址
sql_data_check_dir = os.path.join(base_dir, "sql_data_check")
withdraw_test_file = os.path.join(sql_data_check_dir, "withdraw.text")
recharge_test_file = os.path.join(sql_data_check_dir, "recharge.text")














