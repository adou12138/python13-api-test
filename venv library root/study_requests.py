# python13-api-test 
# study_requests 
# shen 
# 2019/1/14 22:03 



'''
cn.python-requests.org/zh_CN/latest
http 协议两大部分(入参/出参)
Request：
请求方法:
GET     查--获取资源
POST    改--修改资源
PUT     增加
DELETE  删除
OPTION--黑客嗅探使用
HEADER--没有返回体，会返回头部信息
请求URL： 协议：//服务器IP地址：端口号/接口路径
请求参数：传参方式：URL/表单
header 请求头：Content-type （测试的时候，加上user agent可以快速区分测试数据还是正式数据）
cookie

response
状态码
1XX--信息类（Information），表示收到web浏览器请求，正在进一步的处理中
2XX--成功类（Successful），表示用户请求被正确接收，理解和处理，例如：200 ok
3XX--重定向类（Redirection），表示请求没有成功，客户必须采取进一步的动作
4XX--客户端错误（Client Error），表示客户端提交的请求有错误 例如：404 NOT Found
5XX--服务器错误（Server Error），表示服务器不能完成对请求的处理 例如：500

响应信息 响应bady 返回信息内容 status code
cookie
header

'''
'''
request：函数：method url 位置传参，其他使用关键字传参！
method：请求方法
url：请求地址
params：get url 请求方式-参数 Dictionary
datas：post 请求方式 Dictionary
json：JSON
headers：
cookies：
files：实现上传和下载的接口功能
auth：认证的信息
timeout：指定等待时间 (connect timeout, read timeout) <timeouts>` tuple.
type timeout: float or tuple
allow_redirects：允许重定向
proxies：使用代理
verify：请求https的接口，不做校验，定义为false去除校验
stream：返回文件是源文件内容，设置为True-流对象
cert：证书（路径传入） 和verify（传出）成对出现


'''

import requests

# 构造请求
# resp = requests.get('http://cn.python-requests.org/zh_CN/latest/')
# resp.encoding = 'utf-8'  # 解决乱码
# print('响应码', resp.status_code)
# print('响应信息', resp.text)
# with open('index.html', 'w+', encoding='utf-8') as file:
#     file.write(resp.text)

# 登录接口 传参 url
# datas = {'mobilephone': '15810447656', 'pwd': '123456'}
# resp = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/login', params=datas)
# # resp = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/login', datas=datas) 会请求不到参数
# print('请求url', resp.request.url)
# print('请求参数', resp.request.body)
# print('响应码', resp.status_code)
# print('响应信息', resp.text)





# 登录接口 post---表单传参---datas
data = {'mobilephone': '15810447656', 'pwd': '123456'}
resp = requests.post('http://test.lemonban.com/futureloan/mvc/api/member/login', data=data)
print('请求url', resp.request.url)
print('请求参数', resp.request.body)
print('请求headers', resp.request.headers)
print('请求cookies', resp.request._cookies)
# 前面加下划线AttributeError: 'PreparedRequest' object has no attribute 'cookies'
print('响应码', resp.status_code)
print('响应信息', type(resp.text))
print('响应信息字典', resp.json())  # 有啥用？
print('响应信息字典',resp.json()['status'])
print('响应信息', resp.text)
print('响应cookies', resp.cookies)
print('响应headers', resp.headers)

# 完成注册登录，查看request的用法
# 看前程带接口 数据字典
# 120.78.128.25数据库的地址写这个
# 47.107.168.87:8080

# http://cn.python-requests.org/zh_CN/latest/user/quickstart.html  #url
# https://www.cnblogs.com/ios9/p/9527939.html sql2017