# coding: utf-8
# python13-api-test 
# study_mock 
# shen 
# 2019/2/18 22:43

"""
查看下rap接口定义？
mockserver定义？
"""
import requests
from unittest import mock
def request_baidu():
    # 抓百度的内容
    return requests.get('http://www.baidu.com').text.encode('utf-8')

def print_baidu():
    print(request_baidu())

request_baidu = mock.Mock(return_value='this is baidu')
print_baidu()

