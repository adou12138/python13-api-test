# coding: utf-8  # 模板添加
# 当前项目的名称: python13-api-test
# 新文件名称：api_11.14_homework 
# 当前登录名：LuckyLu
# 创建日期：2019/1/15 11:03
# 文件IDE名称：PyCharm

# requirement
'''
接口地址：member/login
请求方式：GET/POST

参数	变量名	类型	说明	是否必填
手机号	mobilephone	String	会员手机号	是
密码	pwd	String	会员密码	是

结果说明
参数	变量名	类型	说明
结果	status	String	接口执行状态，1 表示成功 0 表示异常
返回码	Code:msg	String	10001：成功
20102：服务器异常
20103：参数错误：参数不能为空
20111：用户名或者密码错误
'''

import requests

'''
充值账户
datas = {"mobilephone": "15666666666", "pwd": "123456"}
'''
# get请求 登陆  响应信息10001
# data = {"mobilephone": "15666666666", "pwd": "123456"}
# resp = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/login',params=data, timeout=(0.06, 0.06))
# print(resp.request.url)  # 请求的url
# print(resp.request.body)  # 请求参数
# print(resp.status_code)  # 响应码
# print(resp.text)  # 响应信息
# print(resp.headers)  # 头部信息

# post请求 用户登陆 响应信息10001
# data = {"mobilephone": "15777777777", "pwd": "123456"}
# resp = requests.post('http://test.lemonban.com/futureloan/mvc/api/member/login', data=data)
# # print(resp.request.url)  # 请求url
# # print(resp.request.body)  # 请求参数
# # print(resp.request.headers)  # 请求headers
# print(resp.request._cookies)  # 请求cookies，cookies前面加下划线
# #
# print(resp.status_code)  # 响应码 10001
# print(resp.text)  # 响应信息
# # print(resp.cookies)  # 响应cookies
# # print(resp.headers)  # 响应headers
# print(resp.cookies)  # 响应cookies

# post请求 响应信息20111
# data = {"mobilephone": "15777777777", "pwd": "1234567"}
# resp = requests.post('http://test.lemonban.com/futureloan/mvc/api/member/login', data=data)
# print(resp.text)  # 响应信息

# post请求 响应信息20111
# data = {"mobilephone": "15777777778", "pwd": "123456"}
# resp = requests.post('http://test.lemonban.com/futureloan/mvc/api/member/login', data=data)
# print(resp.text)  # 响应信息


# post请求 密码为空 响应信息20103
# data = {"mobilephone": "157777", "pwd": ""}
# resp = requests.post('http://test.lemonban.com/futureloan/mvc/api/member/login', data=data)
# print(resp.text)  # 响应信息

# post请求 电话为空 响应信息20103
# data = {"mobilephone": "", "pwd": "123456"}
# resp = requests.post('http://test.lemonban.com/futureloan/mvc/api/member/login', data=data)
# print(resp.text)  # 响应信息

# post请求 响应信息20102 服务器异常 挂了才能测

session = requests.session()
# data = {"mobilephone": "15666666666", "pwd": "123456"}
# url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/login", params={"mobilephone": "15666666666", "pwd": "123456"})

# data = {"mobilephone": "15666666668", "amount": 51}
# resp2 = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/recharge', params=data, cookies=get_cookies, timeout=(0.06, 0.06))
res1 = session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/recharge", params={"mobilephone": "15666666668", "amount": 51})

print(res1.status_code)
print(res1.text)

