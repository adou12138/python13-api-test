# coding: utf-8
# 当前项目的名称: python13-api-test 
# 新文件名称：test 
# 当前登录名：LuckyLu
# 创建日期：2019/1/15 13:40
# 文件IDE名称：PyCharm

# from PTL import Image  # 图片操作

'''get请求'''
import requests
# req1 = requests.get("http://httpbin.org/get", params={'key1': 'value1', 'key2': ['value2', 'value3']})  # 列表作为值传入
# print(req1.url)  # "url": "http://httpbin.org/get?key2=value2&key2=value3&key1=value1"
# print(req1.text)
# print(req1.status_code)
# req1.encoding = 'utf-8'
# print(req1.content)  # 非文本请求，以字节形式请求响应体
print('*'*50)


# req3 = requests.get('https://api.github.com/events')
# print(req3.json())
# print('*'*50)
'''
检查json请求是否成功
req3.raise_for_status()
req3.status_code

'''

'''原始响应内容'''
# req3 = requests.get('https://api.github.com/events', stream=True)
# print(req3.raw)
# # req3.raw.read(10)
#
# with open('test.txt', 'w') as file:
#     for chunk in req3.iter_content(chunk_size=569):  # 会报错
#         file.write(chunk)
# print('*'*50)


'''定制请求头'''
# url = 'https://api.github.com/some/endpoint'
# headers = {'user-agent': 'my-app/0.0.1'}
# req3 = requests.get('https://api.github.com/some/endpoint')
# print(req3.request.headers)
# print = {'User-Agent': 'python-requests/2.20.1', 'Accept': '*/*', 'Connection': 'keep-alive', 'Accept-Encoding': 'gzip, deflate'}
# print = {'Connection': 'keep-alive', 'Accept-Encoding': 'gzip, deflate', 'user-agent': 'my-app/0.0.1', 'Accept': '*/*'}  # 传入headers显示传入的参数
# 添加头部信息
# url = 'https://api.github.com/some/endpoint'
# headers = {'user-agent': 'my-app/0.0.1'}
# req3 = requests.get('https://api.github.com/some/endpoint',headers={'user-agent': 'my-app/0.0.1'})
# print(req3.request.headers)  # 请求头部信息
# print('*'*50)
# print(req3.headers)  # 响应头部信息

'''post请求'''
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.post("http://httpbin.org/post", data=payload)
# print(r.text)

# payload = (('key1', 'value1'), ('key1', 'value2'))  # 用一个key，显示多个value值
# r = requests.post('http://httpbin.org/post', data=payload)
# print(r.text)
'''
"key1": [
    "value1",
    "value2"
]
'''

'''json'''
import json
# url = 'https://api.github.com/some/endpoint'
# payload = {'some': 'data'}
# r = requests.post(url, data=json.dumps(payload))  # json.dumps 字典转换成jason格式
# print(r)

# url = 'https://api.github.com/some/endpoint'
# payload = {'some': 'data'}
# r = requests.post(url, json=payload)  # 直接用json传参
# print(r)


'''文件传输'''
# # {'name': file-tuple}  # 上传文件
# url = 'http://httpbin.org/post'
# files = {'file': open('report.xlsx', 'rb')}  # 文件传输格式
# r = requests.post(url, files=files)
# print(r.text)

# url = 'http://httpbin.org/post'
# files = {'file': ('report.xlsx', open('report.xlsx', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}  # 文件名、文件类型、请求头
# r = requests.post(url, files=files)
# print(r.text)

# url = 'http://httpbin.org/post'
# files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}  # 作为文件来接收的字符串
# r = requests.post(url, files=files)
# print(r.text)

'''响应码'''
# r = requests.get('http://httpbin.org/get')
# print(r.status_code)  # 200
# print(r.status_code == requests.codes.ok)  # 正常就是True

# bad_r = requests.get('http://httpbin.org/status/404')
# bad_r.status_code  # 404
# bad_r.raise_for_status()  # Response.raise_for_status() 来抛出异常：
# # Traceback (most recent call last):
# #   File "requests/models.py", line 832, in raise_for_status
# #     raise http_error
# # requests.exceptions.HTTPError: 404 Client Error

'''响应头'''
# r = requests.get('http://httpbin.org/get')
# print(r.headers)  # 获取响应头
# # 获取响应头Content-Type的详细信息
# print(r.headers['Content-Type'])  # 'application/json'
# print(r.headers.get('content-type'))  # 'application/json'

'''cookies'''
# url = 'http://httpbin.org/cookies'
# r = requests.get(url)
# print(r)
# r.cookies['example_cookie_name']  # 获取指定cookies值：'example_cookie_value'

# 传入制定cookies的值
url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')

r = requests.get(url, cookies=cookies)
print(r.text)  # '{"cookies": {"cookies_are": "working"}}'


# Cookie 的返回对象为 RequestsCookieJar，它的行为和字典类似，但接口更为完整，适合跨域名跨路径使用。你还可以把 Cookie Jar 传到 Requests 中：
jar = requests.cookies.RequestsCookieJar()
jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
url = 'http://httpbin.org/cookies'
r = requests.get(url, cookies=jar)
print(r.text)  # '{"cookies": {"tasty_cookie": "yum"}}'


'''重定向'''

# req2 = requests.post('http://httpbin.org/post', data={'key': 'value'})
# print(req2.text)
# print(req2.url)
# print(req2.status_code)

# req2 = requests.put('http://httpbin.org/put', data={'key': 'value'})
# print(req2.text)
# print(req2.url)
# print(req2.status_code)
# print(req2.cookies)

