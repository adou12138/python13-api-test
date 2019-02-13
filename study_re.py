# coding: utf-8
# python13-api-test 
# study_re 
# shen 
# 2019/1/26 13:32

import re
"""
正则表达式一般包含：原本字符 元字符
()  代表一个组
元字符
.   匹配任意单个字符
\d  匹配任意单个数字
限定符
+   至少匹配一次
?   最多匹配一次
*   匹配0次或者多次

re模块扩展，有几种模式，分别使用一下
jmeter扩展：loadid 12345 可以用正则快速找到结果 "\#\{(.*?)}"

"""
import json
admin_user = '15873171553'
admin_pwd = '123456'

data = {"admin_user": "15873171553", "admin_pwd": "123456"}
s = '{"mobilephone": "${admin_user}", "pwd": "${admin_pwd}"}'
p = "\$\{admin_user}"  # 需要转义 原本字符的写法
p1 = "\$\{(.*?)}"  # 元字符和限定符，（）代表组 英文输入法下面去写正则表达式

"""
m = re.search(p, s)  # 原本字符搜索结果
print("匹配对象", m)
匹配对象 <_sre.SRE_Match object; span=(17, 30), match='${admin_user}'>
"""
m = re.search(p1, s)  # 元字符搜索结果  # 任意位置开始找，找到一个就返回match
print("任意位置开始找，找到一个就返回match", m)
g = m.group()  # 不传参，返回的是整个匹配的字符串
print(g)
g1 = m.group(1)  # 取第一个组的匹配字符串
print(g1)
value = data[g1]
s = re.sub(p1, value, s, count=1)  # 查找且替换  # sub count默认为0，匹配所有，查找全部
print("使用正则式查找，并且替换：", s)


l = re.findall(p1, s)  # 查找全部，返回一个列表
print("查找全部，返回一个列表", l)
"""
# 字符串替换 方法还是不行，不用！！！
s = s.replace("${admin_user}", value)
print(s)
"""

# # 将字符串转成字典，然后根据KEY去取值，取到值判断是否需要替换
# dict1 = json.loads(s)
# if dict1['mobilephone'] == '${admin_user}':
#     dict1['mobilephone'] = admin_user
#
# if dict1['pwd'] == '${admin_pwd}':
#     dict1['pwd'] = admin_pwd
#
# print(dict1)



# 字符串的查找，替换
if s.find('${admin_user}') > -1:
    s = s.replace('${admin_user}', admin_user)  # 调用replace方法，不会改变字符串，字符串需要重新去赋值

if s.find('${admin_pwd}') > -1:
    s = s.replace('${admin_pwd}', admin_pwd)

print(s)
"""
{"mobilephone": "${admin_user}", "pwd": "${admin_pwd}"}
"""
# 根据KEY动态的去取值


