# coding: utf-8
# homework_01.19
# request 
# shen 
# 2019/1/19 18:02

import requests
from common import contants
from conf.test_api_config import ReadConfig

class Request:
    "这个是一个request请求的类"

    def __init__(self):
        self.session = requests.sessions.session()  # 实例化一个session对象 具体说明看源码

    def request(self, method, url, data=None):
        method = method.upper()  # 将字符全部转成大写

        URL = ReadConfig(contants.api_conf_file).get_value('URL', 'path_url') + url

        if data is not None and type(data) == str:
            data = eval(data)  # 如果是字符串就转成字典

        if method == "GET":
            return self.session.request(method, url=URL, params=data)
        elif method == "POST":
            return self.session.request(method, url=URL, data=data)
        else:
            print("Un-support method !!!")

if __name__ == '__main__':
    res = Request()
    result = res.session.request("get", "http://test.lemonban.com/futureloan/mvc/api/member/login", params={"mobilephone": "15666666666", "pwd": "123456"})
    print(result.text)

    # print(res.session.cookies)
    # result = Request().request.request("get", "http://test.lemonban.com/futureloan/mvc/api/member/login", params={"mobilephone": "15666666666", "pwd": "123456")
    # print(result)















