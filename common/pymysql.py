# coding: utf-8
# 当前项目的名称: python13-api-test 
# 新文件名称：pymysql 
# 当前登录名：LuckyLu
# 创建日期：2019/1/21 16:40
# 文件IDE名称：PyCharm

import pymysql

class MSSQL:

    def __init__(self, host, user, password, db, port):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.port = port

    def __GetConnect(self):
        if not self.db:
            raise (NameError, "没有设置数据库信息")
        self.db = pymysql.db(host=self.host, user=self.user, password=self.password, database=self.db, port=self.port, charset="utf8")
        cur = self.db.cursor()
        if not cur:
            raise (NameError, "连接数据库失败")
        else:
            return cur

    def ExecQuery(self, sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()
        # 查询完毕后必须关闭连接
        self.db.close()
        return resList

    def ExecNonQuery(self, sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        self.db.commit()
        self.db.close()

ms = MSSQL(host="test.lemonban.com", user="test", password="test", db="testdb", port=3306)
reslist = ms.ExecQuery("select * from member")
print(reslist)
# for i in reslist:
#     print i

# newsql = "update webuser set name='%s' where id=1" % u'测试'
# print(newsql)
# ms.ExecNonQuery(newsql.encode('utf-8'))