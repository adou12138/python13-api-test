# coding: utf-8  # 模板添加
# 当前项目的名称: python13-api-test
# 新文件名称：api_11.14_homework 
# 当前登录名：LuckyLu
# 创建日期：2019/1/15 11:03
# 文件IDE名称：PyCharm

# requirement
'''
接口地址：member/list 请求方式：GET/POST 参数：无

结果说明
参数	变量名	类型	说明
结果	status	string	接口执行状态，1表示成功 0表示异常
返回码	code:msg	string	10001：成功
20102：服务器异常

'''

import requests

'''
管理员账户
datas = {"mobilephone": "15555555555", "pwd": "123456"}
<RequestsCookieJar[<Cookie JSESSIONID="" for test.lemonban.com/futureloan>]>
'''

# get请求 未登陆直接执行回款记录  响应信息null
# data = {"id": "11909"}
# data = {"id": ""}
# data = {"id": "-1"}
# data = {"id": "1999"}
# data = {"id": "asd"}
# data = {"id": "11881"}

# resp = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/list', params="")
# # print(resp.status_code)  # 响应码
# # print(resp.text)  # 响应信息


# data = {"mobilephone": "15777777777", "amount": 10000}
# resp2 = requests.session('post', 'http://test.lemonban.com/futureloan/mvc/api/member/login', data={"mobilephone": "15666666666", "pwd": "123456"})
# print(resp2.text)
#
session = requests.session()
session.request('post', 'http://test.lemonban.com/futureloan/mvc/api/member/login', data={"mobilephone": "15555555555", "pwd": "123456"})
resp2 = session.request('post', 'http://test.lemonban.com/futureloan/mvc/api/member/list', data="")
print(resp2.text)