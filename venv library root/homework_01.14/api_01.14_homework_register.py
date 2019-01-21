# coding: utf-8  # 模板添加
# 当前项目的名称: python13-api-test
# 新文件名称：api_11.14_homework 
# 当前登录名：LuckyLu
# 创建日期：2019/1/15 11:03
# 文件IDE名称：PyCharm


# 1，熟读前程贷需求文档，数据库结构。
# （自取：https://www.ketangpai.com/Courseware/index/courseid/MDAwMDAwMDAwMLOcy5WGqads.html）
# 2，使用requests完成其中注册，登录，充值接口的调用 （温馨提示，充值需要传登录之后返回的cookies）
#
# requests文档参考：（其中快速上手都照着练习一下，你会发现对requests摸得透透的！）
#
# http://cn.python-requests.org/zh_CN/latest/

# http://test.lemonban.com/futureloan/mvc/api/member/register

# requirement
'''
接口地址：member/register 请求方式：GET/POST

参数	变量名	类型	说明	是否必填
手机号	mobilephone	String	新会员的手机号	是
密码	pwd	String	6 到 18 位（最少 6 位，最长 18 位）	是
注册名	regname	String	相当于昵称	否

结果说明
参数	变量名	类型	说明
结果	status	String	接口执行状态，1 表示成功 0 表示异常
返回码	Code:msg	String	10001：成功
20102：服务器异常
20103：参数错误：参数不正常不能为空
20108：密码长度必须为 6~18
20109：手机号码格式不正确
20110：手机号码已被注册
'''

import requests

# get请求 用户注册
data = {"mobilephone": "15666666678", "pwd": "123456"}
resp = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/register', params=data)
print(resp.request.url)  # 请求的url
print(resp.request.body)  # 请求参数
print(resp.status_code)  # 响应码
print(resp.text)  # 响应信息
print(resp.headers)  # 响应头部信息

# get请求添加注册名(regname)
# data = {'mobilephone': '15555555555', 'pwd': '123456', 'regname': 'luckytest'}
# resp = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/register',params=data)
# print(resp.request.url)
# print(resp.request.body)
# print(resp.status_code)
# print(resp.text)
# print(resp.headers)

# post请求 用户注册 注册名(regname)是可以重复的？
# data = {'mobilephone': '15777777777', 'pwd': '123456', 'regname': 'luckytest'}
# resp = requests.post('http://test.lemonban.com/futureloan/mvc/api/member/register',data=data)
# print(resp.request.url)  # 请求url
# print(resp.request.body)  # 请求参数
# print(resp.request.headers)  # 请求headers
# print(resp.request._cookies)  # 请求cookies，cookies前面加下划线
#
# print(resp.status_code)  # 响应码 10001
# print(resp.text)  # 响应信息
# print(resp.cookies)  # 响应cookies
# print(resp.headers)  # 响应headers

# post请求 手机号码已被注册 响应信息20110
# data = {"mobilephone": "15777777777", "pwd": "123456", "regname": "luckytest"}
# resp = requests.post('http://test.lemonban.com/futureloan/mvc/api/member/register', data=data)
# print(resp.text)  # 响应信息

# post请求 手机号码格式不正确 响应信息20109
# data = {"mobilephone": "157777", "pwd": "123456", "regname": "luckytest"}
# resp = requests.post('http://test.lemonban.com/futureloan/mvc/api/member/register', data=data)
# print(resp.text)  # 响应信息

# post请求 密码长度必须为6~18（小于6位） 响应信息20108
# data = {"mobilephone": "15777777777", "pwd": "123", "regname": "luckytest"}
# resp = requests.post('http://test.lemonban.com/futureloan/mvc/api/member/register', data=data)
# print(resp.text)  # 响应信息

# post请求 密码长度必须为6~18（大于18位） 响应信息20108
# data = {"mobilephone": "15777777777", "pwd": "1234567890123456789", "regname": "luckytest"}
# resp = requests.post('http://test.lemonban.com/futureloan/mvc/api/member/register', data=data)
# print(resp.text)  # 响应信息

# post请求 密码不能为空 响应信息20103
# data = {"mobilephone": "15777777777", "pwd": "", "regname": "luckytest"}
# resp = requests.post('http://test.lemonban.com/futureloan/mvc/api/member/register', data=data)
# print(resp.text)  # 响应信息

# post请求 手机号不能为空 响应信息20103
# data = {"mobilephone": "", "pwd": "123456", "regname": "luckytest"}
# resp = requests.post('http://test.lemonban.com/futureloan/mvc/api/member/register', data=data)
# print(resp.text)  # 响应信息

# post请求 响应信息20102 服务器异常 挂了才能测
