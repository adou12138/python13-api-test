# coding: utf-8  # 模板添加
# 当前项目的名称: python13-api-test
# 新文件名称：api_11.14_homework 
# 当前登录名：LuckyLu
# 创建日期：2019/1/15 11:03
# 文件IDE名称：PyCharm

# requirement
'''
接口地址：/loan/getLoanList 请求方式：GET/POST
  参数：无

结果说明
参数	变量名	类型	说明
结果	status	string	接口执行状态，1 表示成功 0 表示异常
返回码	Code:msg	string	10001：获取标列表成功
20302：服务器异常
20303：获取标列表失败
数据	data	object

'''

import requests

'''
管理员账户
datas = {"mobilephone": "15555555555", "pwd": "123456"}
<RequestsCookieJar[<Cookie JSESSIONID="" for test.lemonban.com/futureloan>]>
'''

# resp = requests.get('http://test.lemonban.com/futureloan/mvc/api/loan/getLoanList', params="")
# print(resp.status_code)  # 响应码
# print(resp.text)  # 响应信息

# data = {"mobilephone": "15777777777", "amount": 10000}
# resp2 = requests.session('post', 'http://test.lemonban.com/futureloan/mvc/api/member/login', data={"mobilephone": "15666666666", "pwd": "123456"})
# print(resp2.text)
#
session = requests.session()
session.request('post', 'http://test.lemonban.com/futureloan/mvc/api/member/login', data={"mobilephone": "15555555555", "pwd": "123456"})
resp2 = session.request('post', 'http://test.lemonban.com/futureloan/mvc/api/loan/getLoanList', data="")
print(resp2.text)