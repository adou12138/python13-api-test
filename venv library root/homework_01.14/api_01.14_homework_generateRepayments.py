# coding: utf-8  # 模板添加
# 当前项目的名称: python13-api-test
# 新文件名称：api_11.14_homework 
# 当前登录名：LuckyLu
# 创建日期：2019/1/15 11:03
# 文件IDE名称：PyCharm

# requirement
'''
接口地址：/loan/generateRepayments 请求方式：GET/POST

参数	变量名	类型	说明	是否必填
项目id	id	int		是

结果说明
参数	变量名	类型	说明
结果	status	string	接口执行状态，1 表示成功 0 表示异常
返回码	code	string	10001：生成回款计划成功
20402：服务器异常
20403：参数错误
20404：不存在该项目，生成回款计划失败
20405：该项目不在核保审批或终审状态，无法生成回款计划
20406：请根据参数类型对应输入，数值类型
只能输入数字
数据	data	object
信息	msg	string

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
data = {"id": "12056"}

# resp = requests.get('http://test.lemonban.com/futureloan/mvc/api/loan/generateRepayments', params=data)
# print(resp.status_code)  # 响应码
# print(resp.text)  # 响应信息


# data = {"mobilephone": "15777777777", "amount": 10000}
# # resp2 = requests.session('post', 'http://test.lemonban.com/futureloan/mvc/api/member/recharge', data={"mobilephone": "15666666666", "pwd": "123456"})
# # print(resp2.text)
#
session = requests.session()
session.request('post', 'http://test.lemonban.com/futureloan/mvc/api/member/login', data={"mobilephone": "15555555555", "pwd": "123456"})
resp2 = session.request('post', 'http://test.lemonban.com/futureloan/mvc/api/loan/generateRepayments', data=data)
print(resp2.text)