# coding: utf-8  # 模板添加
# 当前项目的名称: python13-api-test
# 新文件名称：api_11.14_homework 
# 当前登录名：LuckyLu
# 创建日期：2019/1/15 11:03
# 文件IDE名称：PyCharm

# requirement
'''
接口地址：/loan/add 请求方式：GET/POST

参数	变量名	类型	说明	是否必填
用户 ID	memberId	int	用户的memberid	是
标题	title	string		是
借款金额	amount	double		是
年利率	loanRate	double	如年化 18.0%，存储为 18.0	是
借款期限	loanTerm	int	如 6 个月为 6，30 天为 30	是
借款期限类型	loanDateType	int	借款期限单位	0- 按月 2- 按天
4-按周	是
还款方式	repaymemtWay	int	4-一次性	5 按月等额本息 10 按
月等额本息线下 11 按月付息到期还本	是
竞标天数	biddingDays	int	1-10 天	是

结果说明
参数	变量名	类型	说明
结果	status	string	接口执行状态，1 表示成功 0 表示异常
返回码	code	string	10001：成功
20102：服务器异常
20103：参数错误：参数不能为空
20104：参数错误：用户ID memberId 必须否正整数
20105：不存在该会员
20106：参数错误：借款金额 amount 必须为大于 1000 并能被 100 整除的正整数
20107：参数错误：借款利率 loanRate 值必须大于 0 小于或等于 24
20108: 参 数 错 误 ： 借 款 日 期 类 型
loanDateType 只能为 0,2,4
20109:参数错误：请根据参数类型对应输入， 数值类型只能输入数字
数据	data	object

'''

import requests

'''
创建标的 借款用户
datas = {"mobilephone": "15777777777", "pwd": "123456"}
<RequestsCookieJar[<Cookie JSESSIONID=60B5CACF93F2F7428C8280925DF29038 for test.lemonban.com/futureloan>]>
'''

# get请求 未登陆直接创建  响应信息null
data = {"memberId":1114425, "title":"lucyktest1", "amount":10000, "loanRate":10.0, "loanTerm":6, "loanDateType":0, "repaymemtWay":4,
        "biddingDays":1, "mobilephone": "15777777777", "amount": 123}
resp = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/withdraw', params=data)
print(resp.status_code)  # 响应码
print(resp.text)  # 响应信息


# get请求 登陆获取cookies充值  响应信息 10001
data = {"mobilephone": "15666666666", "pwd": "123456"}
resp1 = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/login', params=data)
print(resp1.request._cookies)  # 请求cookies，cookies前面加下划线
get_cookies = resp1.cookies
print(get_cookies)

# 传入cookies值 取现
# data = {"mobilephone": "15666666666", "amount": 51}
# resp2 = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/withdraw', params=data, cookies=get_cookies)
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
data = {"mobilephone": "15666666666", "amount": "500000"}
resp2 = requests.post('http://test.lemonban.com/futureloan/mvc/api/member/withdraw', data=data, cookies=get_cookies)
print(resp2.text)










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

