# coding: utf-8
# python13-api-test 
# mysql 
# shen 
# 2019/1/21 22:38 

import pymysql
from common.test_api_config import ReadConfig

class MysqlUtil:
    '这个是一个操作数据的类'
    def __init__(self):  # 初始化数据库参数
        # 1. 建立连接
        # host = "test.lemonban.com"
        # user = "test"
        # password = "test"
        # port = 3306

        config = ReadConfig()
        host = eval(config.get_value("DataBase", "host"))
        user = eval(config.get_value("DataBase", "user"))
        password = eval(config.get_value("DataBase", "password"))
        port = config.get_int("DataBase", "port")

        self.mysql = pymysql.connect(host=host, user=user, password=password, port=port)

    def fetch_one(self, sql):
        # 2. 新建一个查询页面
        cursor = self.mysql.cursor()
        # 4. 执行SQL
        cursor.execute(sql)
        # 5. 查看结果
        result = cursor.fetchone()
        # 6. 关闭查询
        cursor.close()
        return result

    def close(self):
        # 7. 数据库连接关闭
        self.mysql.close()

# 建立一次数据库连接，建立多次查询，整体一次性关闭 上课使用的是这个
class MysqlUtil_double:
    '这个是一个操作数据的类'

    def __init__(self, return_dict=False):  # 初始化数据库参数

        # host = "test.lemonban.com"
        # user = "test"
        # password = "test"
        # self.mysql = pymysql.connect(host=host, user=user, password=password, port=3306)

        config = ReadConfig()
        host = eval(config.get_value("DataBase", "host"))
        user = eval(config.get_value("DataBase", "user"))
        password = eval(config.get_value("DataBase", "password"))
        port = config.get_int("DataBase", "port")

        # 1. 建立连接
        self.mysql = pymysql.connect(host=host, user=user, password=password, port=port)
        # 2. 新建一个查询页面
        if return_dict:
            self.cursor = self.mysql.cursor(pymysql.cursors.DictCursor)  # 指定每行数据以字典形式返回
        else:
            self.cursor = self.mysql.cursor()  # 指定每行数据以元祖的形式返回

    def fetch_one(self,sql):
        # 4. 执行SQL
        self.cursor.execute(sql)
        # 5. 查看结果
        result = self.cursor.fetchone()  # 返回元祖()
        return result  # 返回结果

    def fetch_all(self,sql):
        # 4. 执行SQL
        self.cursor.execute(sql)
        # 5. 查看结果
        results = self.cursor.fetchall()  # 返回列表()
        return results

    def close(self):
        # 6. 关闭查询
        self.cursor.close()
        # 7. 数据库连接关闭
        self.mysql.close()

if __name__ == '__main__':
    # mysql = MysqlUtil()
    # # 3. 编写SQL
    # sql = "select max(mobilephone) from future.member"
    # result = mysql.fetch_one(sql)
    # print(result[0])  # 使用下标去获取值
    # mysql.close()

    mysql = MysqlUtil_double(return_dict=True)
    sql = "select * from future.member limit 10"
    results = mysql.fetch_all(sql)  # 返回列表里面放字典
    for result in results:
        # print(result)
        print(result['Id'])
    mysql.close()
