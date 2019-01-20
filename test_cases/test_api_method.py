# coding: utf-8
# 当前项目的名称: python13-api-test 
# 新文件名称：api_test 
# 当前登录名：LuckyLu
# 创建日期：2019/1/17 15:45
# 文件IDE名称：PyCharm

import unittest
from common import contants
from ddt import ddt, data

from common.do_excel import DoExcel  # 导入excel
from common.request import Request  # 导入api请求

# 一个接口一个类，一个类一个方法
# 一个类，多个方法，多个接接口
# 一个类，一个方法，全部接口

from log.test_api_log import MyLog
my_log = MyLog()

@ddt
class TestApiMethod(unittest.TestCase):
    '这是测试接口的类'
    do_excel = DoExcel(contants.excel_file)  # 传入excel
    cases_register = do_excel.read_excel("register")
    cases_login = do_excel.read_excel("login")
    request = Request()
    def setUp(self):
        # self.write_register = do_excel.write_excel("register")  # 创建一个对象写入
        # self.write_register = do_excel.write_excel("login")  # 创建一个对象写入
        my_log.info("开始执行用例")

    def tearDown(self):
        my_log.info("用例执行结束")

    @data(*cases_register)
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
            self.do_excel.write_excel(case.case_id+1, result.text, TestResult)  # 写入测试实际结果

            my_log.info('注册的结果：{}'.format(result))

    # @data(*cases_login)
    # def test_login(self, case):  # 测试登陆
    #     my_log.info("开始执行第{}条用例: {}".format(case.case_id, case.title))
    #     my_log.info('url:{}'.format(case.url))
    #     my_log.info('data:{}'.format(case.data))
    #     my_log.info('method:{}'.format(case.method))
    #     my_log.info('expected:{}'.format(case.expected))
    #     result = self.request.request(case.method, case.url, case.data)
    #     try:
    #         self.assertEqual(case.expected, result.text)
    #         TestResult = "Pass"
    #     except AssertionError as e:
    #         TestResult = "Failed"
    #         my_log.error("断言出错了".format(e))
    #         raise e
    #     finally:
    #         self.do_excel.write_excel(case.case_id+1, result.text)  # 写入测试实际结果
    #         self.do_excel.write_excel(case.case_id+1, TestResult)  # 写入测试实际结果
    #         my_log.info('登陆的结果：{}'.format(result))

    # def test_recharge(self):  # 测试充值
    #     pass

if __name__ == '__main__':  # 会自动的在当前文件里面加载test_文件开头的用例
    unittest.main()