# coding: utf-8
# 当前项目的名称: python13-api-test 
# 新文件名称：json 
# 当前登录名：LuckyLu
# 创建日期：2019/1/24 14:35
# 文件IDE名称：PyCharm

import json
from common.contants import json_test_file

class OperationJson:

    def __init__(self, file_name=None):
        if file_name:
            self.file_name = file_name
        else:
            self.file_name = json_test_file
        self.data = self.read_data()

    def read_data(self):
        with open(self.file_name) as fp:
            data = json.load(fp)
            return data

    # fp = open(json_test_file)
    # # 获取json文件数据
    # data = json.load(fp)
    # # 打印json1的value
    # print(data["json1"])

    #根据关键字获取数据
    def get_data(self, key):
        return self.data[key]

if __name__ == '__main__':
    opJson = OperationJson()
    print(opJson.read_data())
    print(opJson.get_data('json1'))
