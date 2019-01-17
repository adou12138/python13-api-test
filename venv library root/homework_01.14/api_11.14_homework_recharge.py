# coding: utf-8  # 模板添加
# 当前项目的名称: python13-api-test
# 新文件名称：api_11.14_homework 
# 当前登录名：LuckyLu
# 创建日期：2019/1/15 11:03
# 文件IDE名称：PyCharm

# requirement
'''
接口地址：member/recharge 请求方式：GET/POST

参数	变量名	类型	说明	是否必填
手机号	mobilephone	String	充值人的手机号	是
充值额度	amount	Double	0 到 50 万之间的正数金额，最多精确到到
小数点后两位。	是

结果说明
参数	变量名	类型	说明
结果	status	string	接口执行状态，1 表示成功 0 表示异常
返回码	Code:msg	string	10001：成功
20102：服务器异常
20103：参数错误：参数不能为空
20104：此手机号对应的会员不存在
20109：手机格式不正确
20115：请输入金额
20116：输入金额的金额小数不能超过两位
20117：请输入范围在 0 到 50 万之间的正数金额
20118：请输入数字

'''

import requests

'''
充值账户
datas = {"mobilephone": "15666666666", "pwd": "123456"}
<RequestsCookieJar[<Cookie JSESSIONID=60B5CACF93F2F7428C8280925DF29038 for test.lemonban.com/futureloan>]>
'''

# get请求 未登陆直接充值  响应信息null
# data = {"mobilephone": "15666666666", "amount": 123}
# resp = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/recharge',params=data)
# print(resp.status_code)  # 响应码
# print(resp.text)  # 响应信息


# get请求 登陆获取cookies充值  响应信息 10001
data = {"mobilephone": "15666666666", "pwd": "123456"}
resp1 = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/login', params=data)
print(resp1.request._cookies)  # 请求cookies，cookies前面加下划线
get_cookies = resp1.cookies
print(get_cookies)
#
# # 传入cookies值充值
data = {"mobilephone": "15666666666", "amount": 51}
resp2 = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/recharge', params=data, cookies=get_cookies, timeout=(0.06, 0.06))
print(resp2.text)

# 请输入范围在 0 到 50 万之间的正数金额（510000） 响应信息20117
# data = {"mobilephone": "15666666666", "amount": 510000}
# resp2 = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/recharge', params=data, cookies=get_cookies)
# print(resp2.text)

# 请输入范围在 0 到 50 万之间的正数金额（-1） 响应信息20117
# data = {"mobilephone": "15666666666", "amount": -1}
# resp2 = requests.post('http://test.lemonban.com/futureloan/mvc/api/member/recharge', data=data, cookies=get_cookies)
# print(resp2.text)

# 请输入数字 响应信息20118
# data = {"mobilephone": "15666666666", "amount": "123asd"}
# resp2 = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/recharge', params=data, cookies=get_cookies)
# print(resp2.text)

# 请输入数字 响应信息20118
# data = {"mobilephone": "15666666666", "amount": "！@#￥%"}
# resp2 = requests.post('http://test.lemonban.com/futureloan/mvc/api/member/recharge', data=data, cookies=get_cookies)
# print(resp2.text)

# 输入金额的金额小数不能超过两位 响应信息20116
# data = {"mobilephone": "15666666666", "amount": 99.999}
# resp2 = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/recharge', params=data, cookies=get_cookies)
# print(resp2.text)

# 请输入金额 响应信息20115
# data = {"mobilephone": "15666666666", "amount": None}
# resp2 = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/recharge', params=data, cookies=get_cookies)
# print(resp2.text)

# 手机格式不正确 响应信息20109
# data = {"mobilephone": "156666", "amount": 99.99}
# resp2 = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/recharge', params=data, cookies=get_cookies)
# print(resp2.text)

# 此手机号对应的会员不存在 响应信息20104
# data = {"mobilephone": "15999999999", "amount": 99.99}
# resp2 = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/recharge', params=data, cookies=get_cookies)
# print(resp2.text)

# 参数错误：手机号不能为空 响应信息20103
# data = {"mobilephone": None, "amount": None}
# resp2 = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/recharge', params=data, cookies=get_cookies)
# print(resp2.text)


# 服务器异常 响应信息20102 服务器挂了


# post请求 登陆获取cookies充值  响应信息10001
# data = {'mobilephone': '15666666666', 'pwd': 123456}
# resp1 = requests.post('http://test.lemonban.com/futureloan/mvc/api/member/login', data=data)
# print(resp1.request._cookies)  # 请求cookies，cookies前面加下划线
# print(resp1.text)
# get_cookies = resp1.cookies
#
# # 传入cookies值充值
# data = {'mobilephone': '15666666666', 'amount': 123}
# resp2 = requests.post('http://test.lemonban.com/futureloan/mvc/api/member/recharge', data=data, cookies=get_cookies)
# print(resp2.text)


# post请求 用户登陆 响应信息10001 金额传入字符串
# datas = {'mobilephone': '15666666666', 'pwd': '123456'}
# resp1 = requests.post('http://test.lemonban.com/futureloan/mvc/api/member/login', datas=datas)
# print(resp1.request._cookies)  # 请求cookies，cookies前面加下划线
# get_cookies = resp1.cookies
# print(get_cookies)
#
# # 传入cookies值充值
# datas = {'mobilephone': '15666666666', 'amount': 250000}
# resp2 = requests.post('http://test.lemonban.com/futureloan/mvc/api/member/recharge', datas=datas, cookies=get_cookies)
# print(resp2.text)

