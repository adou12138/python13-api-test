# coding: utf-8
# 当前项目的名称: python13-api-test 
# 新文件名称：api_method 
# 当前登录名：LuckyLu
# 创建日期：2019/1/17 16:30
# 文件IDE名称：PyCharm

import requests

class ApiMethod:
    '这是一个接口类'
    def __init__(self):  # 定义接口地址
        self.register_url = "http://test.lemonban.com/futureloan/mvc/api/member/register"
        self.login_url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
        self.rechager_url = "http://test.lemonban.com/futureloan/mvc/api/member/recharge"

    def login(self, data, method):  # api-sigin
        # data = {"mobilephone": "15666666666", "pwd": "123456"}
        if method == "get":
            resp = requests.get(self.login_url, params=data)
        else:
            resp = requests.post(self.login_url, data=data)
        # resp = requests.get(self.login_url, params=data)
        return resp.text

if __name__ == "__main__":
    re = ApiMethod().login({"mobilephone": "15666666666", "pwd": "123456"}, "post")
    print(re)

    # data = {"mobilephone": "15666666666", "pwd": "123456"}
    # resp = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/login', params=data, timeout=(0.06, 0.06))