# coding: utf-8  # 模板添加
# 当前项目的名称: python13-api-test
# 新文件名称：api_11.14_homework 
# 当前登录名：LuckyLu
# 创建日期：2019/1/15 11:03
# 文件IDE名称：PyCharm

# requirement
'''
接口地址：/loan/audit 请求方式：GET/POST

参数	变量名	类型	说明	是否必填
项目 ID	id	int	标id	是
状态	status	int	1:审核中
2:二审(初审中)
3:三审(复审中)
4:竞标中
5:核保审批
6:平台终审
7:还款中
10:还款完成


***8.9.11状态不需要关注***
8:审核不通过
9:流标
11：申请流标	是

结果说明
参数	变量名	类型	说明
结果	status	string	接口执行状态，1 表示成功 0 表示异常
返回码	code	string	10001：成功
20202：服务器异常
20203：参数错误：所有参数不能为空 20204： 参数错误：错误的标id 值
20205：参数错误：非法 status 参数，状态值
1-11
20206：不存在该项目"
20207：修改失败，当前标已经否该状态
20210：不允许直接更新项目到还款中状态， 请执行生成回款计划
20212：请根据参数类型对应输入，数值类型

# 20208：审核不通过、流标、还款完成的标不允许修改状态
#20209：当前接口暂未开放该状态值更新

只能输入数字
数据	data	object


'''

import requests

'''
创建标的 借款用户
data = {"mobilephone": "15777777777", "pwd": "123456"}
<RequestsCookieJar[<Cookie JSESSIONID=60B5CACF93F2F7428C8280925DF29038 for test.lemonban.com/futureloan>]>
data = {"memberId": 1114425, "title": "lucyktest1", "amount": 10000, "loanRate": 10.0, "loanTerm": 6,
        "loanDateType": 0, "repaymemtWay": 4, "biddingDays": 1}
        
创建的标的 
data = {Id=11587, status=1}

11573
11574
11575
11576

mobilephone=15777777777
11579 loanDateType 0
11580 loanDateType 2
11581 loanDateType 4
'''

# get请求 未登陆直接审核  响应信息null
data = {"id": 11587,  "status": 1}
# resp = requests.get('http://test.lemonban.com/futureloan/mvc/api/loan/audit', params=data)
# print(resp.status_code)  # 响应码
# print(resp.text)  # 响应信息


# 修改失败，当前标已经是该状态 status=1
# data = {"id": 11587,  "status": 1}
# session = requests.session()
# session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/member/login', params={"mobilephone": "15777777777", "pwd": "123456"})
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/audit', params=data)
# print(req1.text)


# 参数错误：所有参数不能为空 status=""
# data = {"id": 11587,  "status": ""}
# session = requests.session()
# session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/member/login', params={"mobilephone": "15777777777", "pwd": "123456"})
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/audit', params=data)
# print(req1.text)

# 参数错误：所有参数不能为空 id=""
# data = {"id": "",  "status": 1}
# session = requests.session()
# session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/member/login', params={"mobilephone": "15777777777", "pwd": "123456"})
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/audit', params=data)
# print(req1.text)

# 参数错误：非法 status 参数，状态值1-11 status=-1
# data = {"id": 11587,  "status": -1}
# session = requests.session()
# session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/member/login', params={"mobilephone": "15777777777", "pwd": "123456"})
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/audit', params=data)
# print(req1.text)


# 参数错误：非法 status 参数，状态值1-11 status=0
# data = {"id": 11587,  "status": 0}
# session = requests.session()
# session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/member/login', params={"mobilephone": "15777777777", "pwd": "123456"})
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/audit', params=data)
# print(req1.text)


# 参数错误：错误的标id值 id=-1
# data = {"id": -1,  "status": 1}
# session = requests.session()
# session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/member/login', params={"mobilephone": "15777777777", "pwd": "123456"})
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/audit', params=data)
# print(req1.text)

# 不存在该项目 id=99999
# data = {"id": 99999,  "status": 1}
# session = requests.session()
# session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/member/login', params={"mobilephone": "15777777777", "pwd": "123456"})
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/audit', params=data)
# print(req1.text)

"""
# 还款完成 项目所有的还款都已完成，状态值1-11 status=10  ！！！状态错误，显示："当前接口暂未开放该状态值更新"
data = {"id": 11587,  "status": 10}
session = requests.session()
session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/member/login', params={"mobilephone": "15777777777", "pwd": "123456"})
req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/audit', params=data)
print(req1.text)
"""


# 请根据数值参数的类型对应输入合法的数字，状态值1-11 id=1
# data = {"id": "abc",  "status": 1}
# session = requests.session()
# session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/member/login', params={"mobilephone": "15777777777", "pwd": "123456"})
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/audit', params=data)
# print(req1.text)

# 请根据数值参数的类型对应输入合法的数字，状态值1-11 id=(*&^
# data = {"id": "(*&^",  "status": -1}
# session = requests.session()
# session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/member/login', params={"mobilephone": "15777777777", "pwd": "123456"})
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/audit', params=data)
# print(req1.text)

# 请根据数值参数的类型对应输入合法的数字，状态值1-11 status=abc
# data = {"id": 11587,  "status": "abc"}
# session = requests.session()
# session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/member/login', params={"mobilephone": "15777777777", "pwd": "123456"})
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/audit', params=data)
# print(req1.text)

# 请根据数值参数的类型对应输入合法的数字，状态值1-11 status=(*(*^
# data = {"id": 11587,  "status": "(*(*^"}
# session = requests.session()
# session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/member/login', params={"mobilephone": "15777777777", "pwd": "123456"})
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/audit', params=data)
# print(req1.text)

# 更新状态成功：审核通过，当前标为二审(初审中)状态，状态值1-11 status=2
# data = {"id": 11580,  "status": 2}
# session = requests.session()
# session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/member/login', params={"mobilephone": "15777777777", "pwd": "123456"})
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/audit', params=data)
# print(req1.text)

# 更新状态成功：审核通过，当前标为二审(初审中)状态，状态值1-11 status=3
# data = {"id": 11580,  "status": 3}
# session = requests.session()
# session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/member/login', params={"mobilephone": "15777777777", "pwd": "123456"})
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/audit', params=data)
# print(req1.text)

# 更新状态成功：审核通过，当前标为三审(复审中)状态，状态值1-11 status=4
# data = {"id": 11580,  "status": 4}
# session = requests.session()
# session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/member/login', params={"mobilephone": "15777777777", "pwd": "123456"})
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/audit', params=data)
# print(req1.text)

# 更新状态成功：审核通过，当前标为二审(初审中)状态，状态值1-11 status=5
# data = {"id": 11580,  "status": 5}
# session = requests.session()
# session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/member/login', params={"mobilephone": "15777777777", "pwd": "123456"})
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/audit', params=data)
# print(req1.text)

# 更新状态成功：审核通过，当前标为二审(初审中)状态，状态值1-11 status=6
# data = {"id": 11580,  "status": 6}
# session = requests.session()
# session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/member/login', params={"mobilephone": "15777777777", "pwd": "123456"})
# req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/audit', params=data)
# print(req1.text)

"""
# 更新状态成功：审核通过，当前标为二审(初审中)状态，状态值1-11 status=7 ???
{"status":0,"code":"20210","data":null,"msg":"不允许直接更新项目到还款中状态，请执行生成回款计划"}
data = {"id": 11580,  "status": 7}
session = requests.session()
session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/member/login', params={"mobilephone": "15777777777", "pwd": "123456"})
req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/audit', params=data)
print(req1.text)

"""
# 更新状态成功：审核通过，当前标为二审(初审中)状态，状态值1-11 status=1
data = {"id": 11580,  "status": 1}
session = requests.session()
session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/member/login', params={"mobilephone": "15777777777", "pwd": "123456"})
req1 = session.request('get', url='http://test.lemonban.com/futureloan/mvc/api/loan/audit', params=data)
print(req1.text)


"""

"""
