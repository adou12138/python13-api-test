# coding: utf-8
# homework_01.19
# test_api_recharge 
# shen 
# 2019/1/21 22:07 

import unittest
from common import contants
from ddt import ddt, data

from common.do_excel import DoExcel  # 导入excel
from common.request import Request  # 导入api请求

"""
充值，先登录，然后走正常的充值成功流程，接着走异常流程
另一种，调用sessions的方法老师会给代码
"""


# 一个接口一个类，一个类一个方法
# 一个类，多个方法，多个接接口
# 一个类，一个方法，全部接口

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
        self.write_recharge = DoExcel(contants.excel_file, "recharge") # 创建一个对象写入

        my_log.info("开始执行用例")

    def tearDown(self):
        my_log.info("用例执行结束")

    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()  # 关闭session请求

    @data(*cases_recharge)
    def test_register(self, case):  # 测试注册
        my_log.info("开始执行第{}条用例: {}".format(case.case_id, case.title))
        my_log.info('url:{}'.format(case.url))
        my_log.info('data:{}'.format(case.data))
        my_log.info('method:{}'.format(case.method))
        my_log.info('expected:{}'.format(case.expected))
        result = self.request.request(case.method, case.url, case.data)
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

    @unittest.skip("不要运行")  # 可以跳过运行此用例
    @data(*cases_login)
    def test_login(self, case):  # 测试注册
        my_log.info("开始执行第{}条用例: {}".format(case.case_id, case.title))
        my_log.info('url:{}'.format(case.url))
        my_log.info('data:{}'.format(case.data))
        my_log.info('method:{}'.format(case.method))
        my_log.info('expected:{}'.format(case.expected))
        result = self.request.request(case.method, case.url, case.data)
        try:
            self.assertEqual(case.expected, result.text)
            TestResult = "Pass"
        except AssertionError as e:
            TestResult = "Failed"
            my_log.error("断言出错了".format(e))
            raise e
        finally:
            self.write_login.write_excel(case.case_id+1, result.text, TestResult)  # 写入测试实际结果
            my_log.info('登陆的结果：{}'.format(result.status_code))