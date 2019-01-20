# coding: utf-8  # 模板添加
# 当前项目的名称: python13-api-test
# 新文件名称：api_11.14_homework 
# 当前登录名：LuckyLu
# 创建日期：2019/1/15 11:03
# 文件IDE名称：PyCharm

# requirement
'''
接口地址：/member/bidLoan 请求方式：GET/POST

参数	变量名	类型	说明	是否必填
用户 ID	memberId	int	用户id	是
密码	password	string	用户的登录密码	是
标 id	loanId	double	标id	是
投资金额	amount	double	投资金额	是

结果说明
参数	变量名	类型	说明
结果	status	string	接口执行状态，1 表示成功 0 表示异常
返回码	code:msg	string	10001：竞标成功
11002：服务器异常
11003：参数错误:所有参数都不能为空
11004：参数错误，memberId 必须否大于 0 的正整数
11005：参数错误，loanId 必须否大于 0 的正整数
11006：参数错误，password 长度必须大于 6
位且小于 18 位
11007：参数错误，投资金额必须能被 100整除的正整数
11008：不存在该用户
11009:不存在该标的
11010：该标不在竞标中状态，无法完成投标
11011：该标已经满标,无法进行投资
11012：该标可投金额不足
11013：请根据数值参数的类型对应输入合法的数字
数据	data	object


'''

import requests

'''
取现账户
datas = {"mobilephone": "15666666666", "pwd": "123456"}
<RequestsCookieJar[<Cookie JSESSIONID=60B5CACF93F2F7428C8280925DF29038 for test.lemonban.com/futureloan>]>
'''


# session = requests.session()
# session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/login", params={"mobilephone": "15666666666", "pwd": "123456"})
# res1 = session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/bidLoan", params={"Id": 1114421, "pwd": "123456", "loanId": 101, "amount": 100})
# print(res1.status_code)
# print(res1.text)
"""
后面都不对！！

"""
# 字符串拼接
# http://test.lemonban.com/futureloan/mvc/api/
url ="http://test.lemonban.com/futureloan/mvc/api/"
address = "member/bidLoan"
job = url+address
print(job)

# get请求 未登陆直接投标  响应信息null
# data = {"Id": 1114421, "pwd": "123456", "loanId": 10, "amount": 100}
# resp = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/withdraw', params=data)
# print(resp.status_code)  # 响应码
# print(resp.text)  # 响应信息


# get请求 登陆获取cookies充值  响应信息 10001
# data = {"mobilephone": "15666666666", "pwd": "123456"}
# resp1 = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/login', params=data)
# print(resp1.request._cookies)  # 请求cookies，cookies前面加下划线
# get_cookies = resp1.cookies
# print(get_cookies)

# 传入cookies值充值
# data = {"mobilephone": "15666666666", "amount": 51}
# resp2 = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/withdraw', params=data, cookies=get_cookies, timeout=(0.06, 0.06))
# print(resp2.text)

# 参数错误：手机号不能为空 响应信息20103
# data = {"mobilephone": None, "amount": None}
# resp2 = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/withdraw', params=data, cookies=get_cookies)
# print(resp2.text)

# 此手机号对应的会员不存在 响应信息20104
# data = {"mobilephone": "15999999999", "amount": 99.99}
# resp2 = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/withdraw', params=data, cookies=get_cookies)
# print(resp2.text)

# 手机格式不正确 响应信息20109
# data = {"mobilephone": "156666", "amount": 99.99}
# resp2 = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/withdraw', params=data, cookies=get_cookies)
# print(resp2.text)

# 请输入金额 响应信息20115
# data = {"mobilephone": "15666666666", "amount": None}
# resp2 = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/withdraw', params=data, cookies=get_cookies)
# print(resp2.text)

# 输入金额的金额小数不能超过两位 响应信息20116
# data = {"mobilephone": "15666666666", "amount": 99.999}
# resp2 = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/withdraw', params=data, cookies=get_cookies)
# print(resp2.text)

# 请输入范围在 0 到 50 万之间的正数金额（510000） 响应信息20117
# data = {"mobilephone": "15666666666", "amount": 510000}
# resp2 = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/withdraw', params=data, cookies=get_cookies)
# print(resp2.text)

# 请输入范围在 0 到 50 万之间的正数金额（-1） 响应信息20117
# data = {"mobilephone": "15666666666", "amount": -1}
# resp2 = requests.post('http://test.lemonban.com/futureloan/mvc/api/member/withdraw', data=data, cookies=get_cookies)
# print(resp2.text)

# 请输入数字 响应信息20118
# data = {"mobilephone": "15666666666", "amount": "123asd"}
# resp2 = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/withdraw', params=data, cookies=get_cookies)
# print(resp2.text)

# 请输入数字 响应信息20118
# data = {"mobilephone": "15666666666", "amount": "！@#￥%"}
# resp2 = requests.post('http://test.lemonban.com/futureloan/mvc/api/member/withdraw', data=data, cookies=get_cookies)
# print(resp2.text)

# 余额不足，请修改提现额度 响应信息20119
# data = {"mobilephone": "15666666668", "amount": "50"}
# resp2 = requests.post('http://test.lemonban.com/futureloan/mvc/api/member/withdraw', data=data, cookies=get_cookies)
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
# resp2 = requests.post('http://test.lemonban.com/futureloan/mvc/api/member/withdraw', data=data, cookies=get_cookies)
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

