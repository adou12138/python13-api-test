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
'投资人'={'mobilephone':15666666678, 'id':1115697}
<RequestsCookieJar[<Cookie JSESSIONID=60B5CACF93F2F7428C8280925DF29038 for test.lemonban.com/futureloan>]>
'''


# session = requests.session()
# session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/login", params={"mobilephone": "15666666666", "pwd": "123456"})
# res1 = session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/bidLoan", params={"Id": 1114421, "pwd": "123456", "loanId": 101, "amount": 100})
# print(res1.status_code)
# print(res1.text)



# get请求 未登陆直接投标  响应信息null
# data = {"memberId": 0, "password": "123456", "loanId": 10, "amount": 100}
# resp = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/bidloan', params=data)
# print(resp.status_code)  # 响应码
# print(resp.text)  # 响应信息

# 登陆后，参数错误:所有参数都不能为空 memberId=""
data = {"memberId": "", "password": "123456", "loanId": 10, "amount": 100}
session = requests.session()
session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/login", params={"mobilephone": "15666666678", "pwd": "123456"})
res1 = session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/bidLoan", params=data)
print(res1.text)

# 登陆后，参数错误:所有参数都不能为空 password=""
# data = {"memberId": 1115697, "password": "", "loanId": 10, "amount": 100}
# session = requests.session()
# session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/login", params={"mobilephone": "15666666678", "pwd": "123456"})
# res1 = session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/bidLoan", params=data)
# print(res1.text)

# 登陆后，参数错误:所有参数都不能为空 loanId=""
# data = {"memberId": 1115697, "password": "123456", "loanId": "", "amount": 100}
# session = requests.session()
# session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/login", params={"mobilephone": "15666666678", "pwd": "123456"})
# res1 = session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/bidLoan", params=data)
# print(res1.text)

# 登陆后，参数错误:所有参数都不能为空 amount=""
# data = {"memberId": 1115697, "password": "123456", "loanId": 10, "amount":"" }
# session = requests.session()
# session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/login", params={"mobilephone": "15666666678", "pwd": "123456"})
# res1 = session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/bidLoan", params=data)
# print(res1.text)

# 参数错误，memberId必须是大于0的正整数 memberid=-1
# data = {"memberId": -1, "password": "123456", "loanId": 10, "amount": 100}
# session = requests.session()
# session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/login", params={"mobilephone": "15666666678", "pwd": "123456"})
# res1 = session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/bidLoan", params=data)
# print(res1.text)

# 参数错误，memberId必须是大于0的正整数 memberid=0
# data = {"memberId": 0, "password": "123456", "loanId": 10, "amount": 100}
# session = requests.session()
# session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/login", params={"mobilephone": "15666666678", "pwd": "123456"})
# res1 = session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/bidLoan", params=data)
# print(res1.text)

# 请根据数值参数的类型对应输入合法的数字 memberid=1.99
# data = {"memberId": 1.99, "password": "123456", "loanId": 10, "amount": 100}
# session = requests.session()
# session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/login", params={"mobilephone": "15666666678", "pwd": "123456"})
# res1 = session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/bidLoan", params=data)
# print(res1.text)

# 不存在该标的 loanId=-1
# data = {"memberId": 1115697, "password": "123456", "loanId": -1, "amount": 100}
# session = requests.session()
# session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/login", params={"mobilephone": "15666666678", "pwd": "123456"})
# res1 = session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/bidLoan", params=data)
# print(res1.text)

# 不存在该标的 loanId=0
# data = {"memberId": 1115697, "password": "123456", "loanId": 0, "amount": 100}
# session = requests.session()
# session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/login", params={"mobilephone": "15666666678", "pwd": "123456"})
# res1 = session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/bidLoan", params=data)
# print(res1.text)

# loanId 必须否大于 0 的正整数？？ 弄不出来
# data = {"memberId": 1115697, "password": "123456", "loanId": "df234", "amount": 100}
# session = requests.session()
# session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/login", params={"mobilephone": "15666666678", "pwd": "123456"})
# res1 = session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/bidLoan", params=data)
# print(res1.text)

# 参数错误，password 长度必须大于 6 位且小于 18 位 password=123
# data = {"memberId": 1115697, "password": "123", "loanId": "df234", "amount": 100}
# session = requests.session()
# session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/login", params={"mobilephone": "15666666678", "pwd": "123456"})
# res1 = session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/bidLoan", params=data)
# print(res1.text)

# 参数错误，password 长度必须大于 6 位且小于 18 位 password=1234567890123456789
# data = {"memberId": 1115697, "password": "1234567890123456789", "loanId": "df234", "amount": 100}
# session = requests.session()
# session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/login", params={"mobilephone": "15666666678", "pwd": "123456"})
# res1 = session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/bidLoan", params=data)
# print(res1.text)

# 参数错误，password 长度必须大于 6 位且小于 18 位 password=123456789012345678
# data = {"memberId": 1115697, "password": "123456789012345678", "loanId": "df234", "amount": 100}
# session = requests.session()
# session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/login", params={"mobilephone": "15666666678", "pwd": "123456"})
# res1 = session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/bidLoan", params=data)
# print(res1.text)

# 参数错误，投资金额必须能被 100整除的正整数 amount=99
# data = {"memberId": 1115697, "password": "123456", "loanId": "11580", "amount": 99}
# session = requests.session()
# session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/login", params={"mobilephone": "15666666678", "pwd": "123456"})
# res1 = session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/bidLoan", params=data)
# print(res1.text)

# 参数错误，投资金额必须能被 100整除的正整数 amount=-100
# data = {"memberId": 1115697, "password": "123456", "loanId": "11580", "amount": -100}
# session = requests.session()
# session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/login", params={"mobilephone": "15666666678", "pwd": "123456"})
# res1 = session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/bidLoan", params=data)
# print(res1.text)

# 参数错误，投资金额必须能被 100整除的正整数 amount=0
# data = {"memberId": 1115697, "password": "123456", "loanId": "11580", "amount": 0}
# session = requests.session()
# session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/login", params={"mobilephone": "15666666678", "pwd": "123456"})
# res1 = session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/bidLoan", params=data)
# print(res1.text)

# 参数错误，不存在该用户 memberId=110
# data = {"memberId": 110, "password": "123456", "loanId": "11580", "amount": 100}
# session = requests.session()
# session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/login", params={"mobilephone": "15666666678", "pwd": "123456"})
# res1 = session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/bidLoan", params=data)
# print(res1.text)

# 该标不在竞标中状态，无法完成投标 memberId=110
# data = {"memberId": 1115697, "password": "123456", "loanId": "11580", "amount": 100}
# session = requests.session()
# session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/login", params={"mobilephone": "15666666678", "pwd": "123456"})
# res1 = session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/bidLoan", params=data)
# print(res1.text)


# 参数错误，password 长度必须大于 6 位且小于 18 位 memberId=110
# data = {"memberId": 1115697, "password": "123456", "loanId": "11580", "amount": 100}
# session = requests.session()
# session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/login", params={"mobilephone": "15666666678", "pwd": "123456"})
# res1 = session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/bidLoan", params=data)
# print(res1.text)

"""
# 该标已经满标,无法进行投资 loanId=??? 重新设计用例
data = {"memberId": 1115697, "password": "123456", "loanId": "11580", "amount": -100}
session = requests.session()
session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/login", params={"mobilephone": "15666666678", "pwd": "123456"})
res1 = session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/bidLoan", params=data)
print(res1.text)


# 该标可投金额不足 loanId=？？？ 重新设计用例
data = {"memberId": 1115697, "password": "123456", "loanId": "11580", "amount": -100}
session = requests.session()
session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/login", params={"mobilephone": "15666666678", "pwd": "123456"})
res1 = session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/bidLoan", params=data)
print(res1.text)
"""

# 参数错误，请根据数值参数的类型对应输入合法的数字 memberId=abc
# data = {"memberId": "abc", "password": "123456", "loanId": "11580", "amount": -100}
# session = requests.session()
# session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/login", params={"mobilephone": "15666666678", "pwd": "123456"})
# res1 = session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/bidLoan", params=data)
# print(res1.text)

# 参数错误，请根据数值参数的类型对应输入合法的数字 amount=abc
# data = {"memberId": "1115697", "password": "123456", "loanId": "11580", "amount": "abc"}
# # session = requests.session()
# # session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/login", params={"mobilephone": "15666666678", "pwd": "123456"})
# # res1 = session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/bidLoan", params=data)
# # print(res1.text)

"""
# 竞标成功 loanId=？？？
data = {"memberId": "1115697", "password": "123456", "loanId": "11580", "amount": "abc"}
session = requests.session()
session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/login", params={"mobilephone": "15666666678", "pwd": "123456"})
res1 = session.request("get", url="http://test.lemonban.com/futureloan/mvc/api/member/bidLoan", params=data)
print(res1.text)
"""
