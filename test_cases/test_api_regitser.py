# coding: utf-8
# python13-api-test 
# test_api_regitser 
# shen 
# 2019/1/21 23:00 

import unittest
from common import contants
from ddt import ddt, data

from common.do_excel import DoExcel  # 导入excel
from common.request import Request  # 导入api请求

# 重新使用doexcel_study中的方法调用
cases_register = DoExcel(contants.excel_file, "register").read_excel()
cases_login = DoExcel(contants.excel_file, "login").read_excel()

from common.mysql import MysqlUtil
import json

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
class TestApiMethod(unittest.TestCase):
    '这是测试接口的类'

    #do_excel = DoExcel(contans.case_file)  # 传入excel
    cases_recharge = DoExcel(contants.excel_file, "recharge").read_excel()

    @classmethod  # 为什么用类方法？ 整个类只执行一次！
    def setUpClass(cls):  # 每个测试类里面去运行的操作都放到类方法里面
        cls.request = Request()  # 实例化对象

    def setUp(self):
        self.write_register = DoExcel(contants.excel_file, "register") # 创建一个对象写入
        self.write_login = DoExcel(contants.excel_file, "login")
        my_log.info("开始执行用例")

    def tearDown(self):
        my_log.info("用例执行结束")

    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()  # 关闭session请求

    mysql = MysqlUtil()
    sql = "select max(mobilephone) from future.member"
    max = mysql.fetch_one(sql) [0] # 执行SQL，并且返回最近的一条数据，是元祖，使用下标取第一个值
    print(max[0])

    @data(*cases_register)
    def test_register(self, case):  # 测试注册
        my_log.info("开始执行第{}条用例: {}".format(case.case_id, case.title))
        # my_log.info('url:{}'.format(case.url))
        # my_log.info('data:{}'.format(case.data))
        # my_log.info('method:{}'.format(case.method))
        # my_log.info('expected:{}'.format(case.expected))
        data_dict = json.loads(case.data)
        if data_dict['mobilephone'] == '#@mobilephone':
            data_dict['mobilephone'] == int(self.max)+1
        result = self.request.request(case.method, case.url, data_dict)
        try:
            self.assertEqual(case.expected, result.text)
            TestResult = "Pass"
        except AssertionError as e:
            TestResult = "Failed"
            my_log.error("断言出错了".format(e))
            raise e
        finally:
            self.write_register.write_excel(case.case_id+1, result.text, TestResult)  # 写入测试实际结果
            my_log.info('注册的结果：{}'.format(result.status_code))


