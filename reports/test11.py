# coding: utf-8
# 当前项目的名称: python13-api-test 
# 新文件名称：test11 
# 当前登录名：LuckyLu
# 创建日期：2019/2/11 11:01
# 文件IDE名称：PyCharm

import os
# print('hello word')

import json
from common import contants
# ajson = {'amount':'10'}
# with open(contants.json_test_file, 'w+') as f:
#     f.write(json.dumps(ajson['amount']))
#


# a = '5'
# with open(contants.recharge_test_file, 'w') as r:  # 登陆成功后，写入member初始leaveamount的值
#     r.write(a)

# 冒泡排序
l = [1,2,4,5,7,3,9,8,6]
def maopao(l):
    count = len(l)
    for i in range(0,count):
        for j in range(i+1,count):
            if l[i] > l[j]:
                l[i],l[j] = l[j],l[i]
                # print(l)
    return l


aa = maopao(l)
print(aa)

# 从一个数组中找出前4个最大的数，用最优解
print(sorted([2,2,1,8,5,7,6])[:4])

# 写一段程序，删除字符串a中包含的字符串b，举例 输入a = "asdw",b = "sd" 返回 字符串 “aw”，并且测试这个程序。
def delete(a,b):
    if b in a:
        c = a.replace(b,'')
    else:
        c= 'b is not in a'
    return c

p = delete('asd1w','s2d')
print(p)
print('*'*50)


# 写一个方法，把字符串转为数字，比如 str="1234"，变成 int 1234。并且测试这个程序。
# a =2
# result = isinstance(a, int)
# print(result)

def change(a):
    if isinstance(a, str):
        c = (int(a))
    else:
        c = 'is not a str'
    return c

s = change('1')
print(s)