# coding: utf-8
# python13-api-test 
# mysql 
# shen 
# 2019/1/21 22:38 

import pymysql

class MysqlUtil:
    '这个是一个操作数据的类'
    def __init__(self):  # 初始化数据库参数
        # 1. 建立连接
        host = "test.lemonban.com"
        user = "test"
        password = "test"
        self.mysql = pymysql.connect(host=host, user=user, password=password, port=3306)

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

# 建立一次数据库连接，建立多次查询，整体一次性关闭
class MysqlUtil_double:
    '这个是一个操作数据的类'

    def __init__(self):  # 初始化数据库参数
        # 1. 建立连接
        host = "test.lemonban.com"
        user = "test"
        password = "test"
        self.mysql = pymysql.connect(host=host, user=user, password=password, port=3306)
        # 2. 新建一个查询页面
        self.cursor = self.mysql.cursor()

    def fetch_one(self,sql):
        # 4. 执行SQL
        self.cursor.execute(sql)
        # 5. 查看结果
        result = self.cursor.fetchone()
        return result

    def close(self):
        # 6. 关闭查询
        self.cursor.close()
        # 7. 数据库连接关闭
        self.mysql.close()

if __name__ == '__main__':
    mysql = MysqlUtil()
    # 3. 编写SQL
    sql = "select max(mobilephone) from future.member"
    result = mysql.fetch_one(sql)
    print(result[0])
    mysql.close()
