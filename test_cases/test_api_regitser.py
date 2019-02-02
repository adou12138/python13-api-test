# coding: utf-8
# python13-api-test 
# test_api_regitser 
# shen 
# 2019/1/21 23:00 

import unittest
from common import contants
from ddt import ddt, data

from common.do_excel_study import DoExcel  # 导入excel
from common.request import Request  # 导入api请求

from common.test_api_config import ReadConfig
config = ReadConfig()

from common.mysql import MysqlUtil
import json

from common.context import Context
# 一个接口一个类，一个类一个方法
# 一个类，多个方法，多个接接口
# 一个类，一个方法，全部接口

"""
手机号码注册 电话号码数据库取值，名字随机字符
1.数据库里面查最大的手机号+1
2.case.data里面的手机号码给替换掉
3.然后再去请求

投资必须先有标的，loan，自己创建一个标的
提bug到禅道
"""
from log.test_api_log import MyLog
my_log = MyLog()

@ddt
class RegisterTest(unittest.TestCase):
    '这是测试注册接口的类'
    # 使用doexcel_study中的方法调用
    do_excel = DoExcel(contants.excel_file)  # 传入do_excel_study.xlsx
    cases_register = do_excel.read_excel("register")  # 读取register_sheet

    @classmethod  # 为什么用类方法？ 整个类只执行一次！
    def setUpClass(cls):  # 每个测试类里面去运行的操作都放到类方法里面
        cls.request = Request()  # 实例化对象

    def setUp(self):
        # self.write_register = DoExcel(contants.excel_file, "register") # 创建一个对象写入
        print("开始执行用例")

    def tearDown(self):
        print("用例执行结束")

    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()  # 关闭session请求
        cls.mysql.close()  # 关闭数据库连接

    mysql = MysqlUtil()
    sql = "select max(mobilephone) from future.member"
    max = mysql.fetch_one(sql)[0]  # 执行SQL，并且返回最近的一条数据，是元祖，使用下标取第一个值
    # print(max)

    # @unittest.skip("忽略")
    @data(*cases_register)
    def test_register(self, case):  # 测试注册
        print("开始执行第{}条用例: {}".format(case.case_id, case.title))
        print('url:{}'.format(case.url))
        print('data:{}'.format(case.data))
        print('method:{}'.format(case.method))
        print('expected:{}'.format(case.expected))
        data_dict = json.loads(case.data)
        if data_dict['mobilephone'] == '#@mobilephone':
            # 取最大电话号码+1
            data_dict['mobilephone'] = int(self.max)+1
        # resp = self.request.request(case.method, case.url, data_dict)

        data_dict = json.dumps(data_dict)  # 把字典转换成字符串传入context进行转换
        # print(data_dict, type(data_dict))
        register_data_new = Context.replace_new(data_dict)
        resp = self.request.request(case.method, case.url, register_data_new)

        try:
            self.assertEqual(case.expected, resp.text)
            self.do_excel.write_excel('register', case.case_id + 1, resp.text, 'PASS')  # 读取sheet，写入结果
            print("第{0}用例执行结果：PASS".format(case.case_id))
        except AssertionError as e:
            self.do_excel.write_excel('register', case.case_id + 1, resp.text, 'FAIL')
            print("第{0}用例执行结果：FAIL".format(case.case_id))
            print("断言出错了".format(e))
            raise e



