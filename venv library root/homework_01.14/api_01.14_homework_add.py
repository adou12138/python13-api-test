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
data = {"memberId": 1114425, "title": "lucyktest1", "amount": 10000, "loanRate": 10.0, "loanTerm": 6,
        "loanDateType": 0, "repaymemtWay": 4, "biddingDays": 1}

'''

# get请求 未登陆直接创建  响应信息null
# data = {"memberId": 1114425, "title": "lucyktest1", "amount": 10000, "loanRate": 10.0, "loanTerm": 6,
#         "loanDateType": 0, "repaymemtWay": 4, "biddingDays": 1}
# resp = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/withdraw', params=data)
# print(resp.status_code)  # 响应码
# print(resp.text)  # 响应信息


# 加标成功
session = requests.session()
session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/member/login', params={"mobilephone": "15777777777", "pwd": "123456"})
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
# print(req1.text)

# 参数错误：参数不能为空 memberid为空 响应信息 20103
# data = {"memberId": "", "title": "lucyktest1", "amount": 10000, "loanRate": 10.0, "loanTerm": 6,
#         "loanDateType": 0, "repaymemtWay": 4, "biddingDays": 1}
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
# print(req1.text)

# 参数错误：参数不能为空 title为空 响应信息 20103
# data = {"memberId": "1114425", "title": "", "amount": 10000, "loanRate": 10.0, "loanTerm": 6,
#         "loanDateType": 0, "repaymemtWay": 4, "biddingDays": 1}
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
# print(req1.text)

# 参数错误：参数不能为空 amount为空 响应信息 20103
# data = {"memberId": "1114425", "title": "lucyktest1", "amount": '', "loanRate": 10.0, "loanTerm": 6,
#         "loanDateType": 0, "repaymemtWay": 4, "biddingDays": 1}
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
# print(req1.text)

# 参数错误：参数不能为空 loanRate为空 响应信息 20103
# data = {"memberId": "1114425", "title": "lucyktest1", "amount": 10000, "loanRate": '', "loanTerm": 6,
#         "loanDateType": 0, "repaymemtWay": 4, "biddingDays": 1}
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
# print(req1.text)

# 参数错误：参数不能为空 loanTerm为空 响应信息 20103
# data = {"memberId": "1114425", "title": "lucyktest1", "amount": 10000, "loanRate": 10.0, "loanTerm": '',
#         "loanDateType": 0, "repaymemtWay": 4, "biddingDays": 1}
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
# print(req1.text)

# 参数错误：参数不能为空 loanDateType为空 响应信息 20103
# data = {"memberId": "1114425", "title": "lucyktest1", "amount": 10000, "loanRate": 10.0, "loanTerm": 6,
#         "loanDateType": '', "repaymemtWay": 4, "biddingDays": 1}
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
# print(req1.text)

# 参数错误：参数不能为空 repaymemtWay为空 响应信息 20103
# data = {"memberId": "1114425", "title": "lucyktest1", "amount": 10000, "loanRate": 10.0, "loanTerm": 6,
#         "loanDateType": 0, "repaymemtWay": '', "biddingDays": 1}
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
# print(req1.text)

# 参数错误：参数不能为空 biddingDays为空 响应信息 20103
# data = {"memberId": "1114425", "title": "lucyktest1", "amount": 10000, "loanRate": 10.0, "loanTerm": 6,
#         "loanDateType": 0, "repaymemtWay": 4, "biddingDays": ''}
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
# print(req1.text)

# 参数错误：用户ID memberId 不存在该会员
# data = {"memberId": "563434", "title": "lucyktest1", "amount": 10000, "loanRate": 10.0, "loanTerm": 6,
#         "loanDateType": 0, "repaymemtWay": 4, "biddingDays": 1}
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
# print(req1.text)

# 参数错误：用户ID memberId 必须否正整数 memberId: -1
# data = {"memberId": "-1", "title": "lucyktest1", "amount": 10000, "loanRate": 10.0, "loanTerm": 6,
#         "loanDateType": 0, "repaymemtWay": 4, "biddingDays": 1}
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
# print(req1.text)

"""
# !!!! 参数错误：用户ID memberId 必须否正整数 memberId: 0 !!!
data = {"memberId": "0", "title": "lucyktest1", "amount": 10000, "loanRate": 10.0, "loanTerm": 6,
        "loanDateType": 0, "repaymemtWay": 4, "biddingDays": 1}
req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
print(req1.text)
"""

# 参数错误：请根据参数类型对应输入， 数值类型只能输入数字 memberId=abc
# data = {"memberId": "abc", "title": "lucyktest1", "amount": 10000, "loanRate": 10.0, "loanTerm": 6,
#         "loanDateType": 0, "repaymemtWay": 4, "biddingDays": 1}
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
# print(req1.text)

# 参数错误：请根据参数类型对应输入， 数值类型只能输入数字 memberId=##$@%
# data = {"memberId": "###@$", "title": "lucyktest1", "amount": 10000, "loanRate": 10.0, "loanTerm": 6,
#         "loanDateType": 0, "repaymemtWay": 4, "biddingDays": 1}
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
# print(req1.text)

# 参数错误：请根据参数类型对应输入， 数值类型只能输入数字 amount=abc
# data = {"memberId": "1114425", "title": "lucyktest1", "amount": "abc", "loanRate": 10.0, "loanTerm": 6,
#         "loanDateType": 0, "repaymemtWay": 4, "biddingDays": 1}
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
# print(req1.text)

# 参数错误：请根据参数类型对应输入， 数值类型只能输入数字 amount=#$@#%
# data = {"memberId": "1114425", "title": "lucyktest1", "amount": "#$@#%", "loanRate": 10.0, "loanTerm": 6,
#         "loanDateType": 0, "repaymemtWay": 4, "biddingDays": 1}
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
# print(req1.text)

# 参数错误：借款金额 amount 必须为大于 1000 并能被 100 整除的正整数 amount=-1
# data = {"memberId": "1114425", "title": "lucyktest1", "amount": -1, "loanRate": 10.0, "loanTerm": 6,
#         "loanDateType": 0, "repaymemtWay": 4, "biddingDays": 1}
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
# print(req1.text)

# 参数错误：借款金额 amount 必须为大于 1000 并能被 100 整除的正整数 amount=0
# data = {"memberId": "1114425", "title": "lucyktest1", "amount": 0, "loanRate": 10.0, "loanTerm": 6,
#         "loanDateType": 0, "repaymemtWay": 4, "biddingDays": 1}
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
# print(req1.text)


# 参数错误：借款金额 amount 必须为大于 1000 并能被 100 整除的正整数 amount=10
# data = {"memberId": "1114425", "title": "lucyktest1", "amount": 10, "loanRate": 10.0, "loanTerm": 6,
#         "loanDateType": 0, "repaymemtWay": 4, "biddingDays": 1}
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
# print(req1.text)

# 参数错误：借款金额 amount 必须为大于 1000 并能被 100 整除的正整数 amount=99
# data = {"memberId": "1114425", "title": "lucyktest1", "amount": 99, "loanRate": 10.0, "loanTerm": 6,
#         "loanDateType": 0, "repaymemtWay": 4, "biddingDays": 1}
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
# print(req1.text)

# 参数错误：借款金额 amount 必须为大于 1000 并能被 100 整除的正整数 amount=101
# data = {"memberId": "1114425", "title": "lucyktest1", "amount": 101, "loanRate": 10.0, "loanTerm": 6,
#         "loanDateType": 0, "repaymemtWay": 4, "biddingDays": 1}
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
# print(req1.text)

# 参数错误：请根据参数类型对应输入， 数值类型只能输入数字 loanRat=abc
# data = {"memberId": "1114425", "title": "lucyktest1", "amount": 10000, "loanRate": 'abc', "loanTerm": 6,
#         "loanDateType": 0, "repaymemtWay": 4, "biddingDays": 1}
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
# print(req1.text)

# 参数错误：请根据参数类型对应输入， 数值类型只能输入数字 loanRat=###%%^
# data = {"memberId": "1114425", "title": "lucyktest1", "amount": 10000, "loanRate": '###%%^', "loanTerm": 6,
#         "loanDateType": 0, "repaymemtWay": 4, "biddingDays": 1}
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
# print(req1.text)

# 参数错误：请根据参数类型对应输入， 数值类型只能输入数字 loanRat=-1
# data = {"memberId": "1114425", "title": "lucyktest1", "amount": 10000, "loanRate": -1, "loanTerm": 6,
#         "loanDateType": 0, "repaymemtWay": 4, "biddingDays": 1}
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
# print(req1.text)

# 参数错误：请根据参数类型对应输入， 数值类型只能输入数字 loanRat=0
# data = {"memberId": "1114425", "title": "lucyktest1", "amount": 10000, "loanRate": 0, "loanTerm": 6,
#         "loanDateType": 0, "repaymemtWay": 4, "biddingDays": 1}
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
# print(req1.text)

# 参数错误：请根据参数类型对应输入， 数值类型只能输入数字 loanRat=25
# data = {"memberId": "1114425", "title": "lucyktest1", "amount": 10000, "loanRate": 25, "loanTerm": 6,
#         "loanDateType": 0, "repaymemtWay": 4, "biddingDays": 1}
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
# print(req1.text)

# 加标成功 loanRat=24
# data = {"memberId": "1114425", "title": "lucyktest1", "amount": 10000, "loanRate": 24, "loanTerm": 6,
#         "loanDateType": 0, "repaymemtWay": 4, "biddingDays": 1}
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
# print(req1.text)

# 参数错误：loanTerm=999
# data = {"memberId": "1114425", "title": "lucyktest1", "amount": 10000, "loanRate": 24, "loanTerm": 999,
#         "loanDateType": 0, "repaymemtWay": 4, "biddingDays": 1}
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
# print(req1.text)

# 参数错误：请根据参数类型对应输入， 数值类型只能输入数字 loanTerm=dsf
# data = {"memberId": "1114425", "title": "lucyktest1", "amount": 10000, "loanRate": 24, "loanTerm": 'dsf',
#         "loanDateType": 0, "repaymemtWay": 4, "biddingDays": 1}
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
# print(req1.text)

# 参数错误：请根据参数类型对应输入， 数值类型只能输入数字 loanTerm=￥@#%
# data = {"memberId": "1114425", "title": "lucyktest1", "amount": 10000, "loanRate": 24, "loanTerm": '￥@#%',
#         "loanDateType": 0, "repaymemtWay": 4, "biddingDays": 1}
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
# print(req1.text)

# 参数错误：借款日期类型 loanDateType=@#%@#%
# data = {"memberId": "1114425", "title": "lucyktest1", "amount": 10000, "loanRate": 24, "loanTerm": 6,
#         "loanDateType": '@#%@#%', "repaymemtWay": 4, "biddingDays": 1}
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
# print(req1.text)

# 参数错误：借款日期类型 loanDateType=abc
# data = {"memberId": "1114425", "title": "lucyktest1", "amount": 10000, "loanRate": 24, "loanTerm": 6,
#         "loanDateType": 'abc', "repaymemtWay": 4, "biddingDays": 1}
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
# print(req1.text)

"""
# 参数错误：借款日期类型 loanDateType=-1 异常
# data = {"memberId": "1114425", "title": "lucyktest1", "amount": 10000, "loanRate": 24, "loanTerm": 6,
#         "loanDateType": -1, "repaymemtWay": 4, "biddingDays": 1}
# req1 = session.request('got', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
# print(req1.text)
"""

# 参数错误：借款日期类型 loanDateType=1
# data = {"memberId": "1114425", "title": "lucyktest1", "amount": 10000, "loanRate": 24, "loanTerm": 6,
#         "loanDateType": 1, "repaymemtWay": 4, "biddingDays": 1}
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
# print(req1.text)

# 加标成功 loanDateType=0
# data = {"memberId": "1114425", "title": "lucyktest1", "amount": 10000, "loanRate": 24, "loanTerm": 6,
#         "loanDateType": 0, "repaymemtWay": 4, "biddingDays": 1}
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
# print(req1.text)

# 加标成功 loanDateType=2
# data = {"memberId": "1114425", "title": "lucyktest1", "amount": 10000, "loanRate": 24, "loanTerm": 6,
#         "loanDateType": 2, "repaymemtWay": 4, "biddingDays": 1}
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
# print(req1.text)

# 加标成功 loanDateType=4
# data = {"memberId": "1114425", "title": "lucyktest1", "amount": 10000, "loanRate": 24, "loanTerm": 6,
#         "loanDateType": 4, "repaymemtWay": 4, "biddingDays": 1}
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
# print(req1.text)

# 参数错误：还款方式 repaymemtWay=abc
# data = {"memberId": "1114425", "title": "lucyktest1", "amount": 10000, "loanRate": 24, "loanTerm": 6,
#         "loanDateType": 0, "repaymemtWay": 'abc', "biddingDays": 1}
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
# print(req1.text)

# 参数错误：还款方式 repaymemtWay=(*&^%^%
# data = {"memberId": "1114425", "title": "lucyktest1", "amount": 10000, "loanRate": 24, "loanTerm": 6,
#         "loanDateType": 0, "repaymemtWay": '(*&^%^%', "biddingDays": 1}
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
"""
# 参数错误：借款日期类型 repaymemtWay=-1 !!! 不应该加标成功
data = {"memberId": "1114425", "title": "lucyktest1", "amount": 10000, "loanRate": 24, "loanTerm": 6,
        "loanDateType": 0, "repaymemtWay": -1, "biddingDays": 1}
req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
print(req1.text)
# print(req1.text)
"""

#  加标成功 借款日期类型 repaymemtWay=4
# data = {"memberId": "1114425", "title": "lucyktest1", "amount": 10000, "loanRate": 24, "loanTerm": 6,
#         "loanDateType": 0, "repaymemtWay": 4, "biddingDays": 1}
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
# print(req1.text)

# 参数错误：竞标天数 biddingDays=abc
# data = {"memberId": "1114425", "title": "lucyktest1", "amount": 10000, "loanRate": 24, "loanTerm": 6,
#         "loanDateType": 0, "repaymemtWay": 4, "biddingDays": 'abc'}
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
# print(req1.text)

# 参数错误：竞标天数 biddingDays=&^%%
# data = {"memberId": "1114425", "title": "lucyktest1", "amount": 10000, "loanRate": 24, "loanTerm": 6,
#         "loanDateType": 0, "repaymemtWay": 4, "biddingDays": '&^%%'}
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
# print(req1.text)

"""
# 参数错误：竞标天数 biddingDays=-1 !!! 不应该加标成功
data = {"memberId": "1114425", "title": "lucyktest1", "amount": 10000, "loanRate": 24, "loanTerm": 6,
        "loanDateType": 0, "repaymemtWay": 4, "biddingDays": -1}
req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
print(req1.text)

# 参数错误：竞标天数 biddingDays=0 !!! 不应该加标成功
data = {"memberId": "1114425", "title": "lucyktest1", "amount": 10000, "loanRate": 24, "loanTerm": 6,
        "loanDateType": 0, "repaymemtWay": 4, "biddingDays": 0}
req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
print(req1.text)
"""

# 加标成功 竞标天数 biddingDays=1
data = {"memberId": "1114425", "title": "lucyktest1", "amount": 10000, "loanRate": 24, "loanTerm": 6,
        "loanDateType": 0, "repaymemtWay": 4, "biddingDays": -1}
req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add', params=data)
print(req1.text)
