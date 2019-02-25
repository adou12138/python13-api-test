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
ajson = {'amount':'10'}
with open(contants.json_test_file, 'w+') as f:
    f.write(json.dumps(ajson['amount']))
