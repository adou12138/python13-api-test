# coding: utf-8  # 模板添加
# 当前项目的名称: python13-api-test
# 新文件名称：api_11.14_homework 
# 当前登录名：LuckyLu
# 创建日期：2019/1/15 11:03
# 文件IDE名称：PyCharm

# requirement
'''
接口地址：/invest/getInvestsByMemberId 请求方式：GET/POST

参数	变量名	类型	说明	是否必填
用户 ID	memberId	int		是


结果说明
参数	变量名	类型	说明
结果	status	string	接口执行状态，1 表示成功 0 表示异常
返回码	code	string	10001：成功
30102：服务器异常
30103：参数错误：参数不能为空
30104：参数错误，参数必须是数字
数据	data	object	投资记录数组
信息	msg	string

'''

import requests

'''
管理员账户
datas = {"mobilephone": "15555555555", "pwd": "123456", "memberId": "1115697"}
<RequestsCookieJar[<Cookie JSESSIONID="" for test.lemonban.com/futureloan>]>
'''

# get请求 未登陆直接执行回款记录  响应信息null
data = {"memberId": "1115697"}
# data = {"memberId": ""}
# data = {"memberId": "adas"}


# resp = requests.get('http://test.lemonban.com/futureloan/mvc/api/invest/getInvestsByMemberId', params=data)
# print(resp.status_code)  # 响应码
# print(resp.text)  # 响应信息

session = requests.session()
session.request('post', 'http://test.lemonban.com/futureloan/mvc/api/member/login', data={"mobilephone": "15555555555", "pwd": "123456"})
resp2 = session.request('post', 'http://test.lemonban.com/futureloan/mvc/api/invest/getInvestsByMemberId', data=data)
print(resp2.text)