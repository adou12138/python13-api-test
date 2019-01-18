# coding: utf-8
# 当前项目的名称: python13-api-test 
# 新文件名称：api_test 
# 当前登录名：LuckyLu
# 创建日期：2019/1/17 15:45
# 文件IDE名称：PyCharm

import unittest
from common.do_excel import DoExcel  # 导入excel
from test_cases.api_method import ApiMethod  # 导入api接口

from ddt import ddt, data
cases_register = DoExcel('../datas/luckytest.xlsx', 'register').read_excel()
cases_login = DoExcel('../datas/luckytest.xlsx', 'login').read_excel()

from log.test_api_log import MyLog
my_log = MyLog()

@ddt
class TestApiMethod(unittest.TestCase):
    '这是测试接口的类'
    def setUp(self):
        self.write_register = DoExcel('../datas/luckytest.xlsx', 'register')  # 创建一个对象写入
        self.write_login = DoExcel('../datas/luckytest.xlsx', 'login')  # 创建一个对象写入
        my_log.info("开始执行用例")

    def tearDown(self):
        my_log.info("用例执行结束")

    @data(*cases)
    def test_register(self, case):  # 测试注册

        my_log.info("开始执行第{}条用例".format(case.case_id, case.title))
        my_log.info('url:', case.url)
        my_log.info('data:', case.data)
        my_log.info('method:', case.method)
        my_log.info('expected:', case.expected)
        result = ApiMethod().register(case.url, case.data, case.method)
        try:
            self.assertEqual(case.expected, result)
            TestResult = "Pass"
        except AssertionError as e:
            TestResult = "Failed"
            my_log.error("断言出错了".format(e))
            raise e
        finally:
            self.write_register.write_excel(case.case_id+1, 7, result)  # 写入测试实际结果
            self.write_register.write_excel(case.case_id+1, 8, TestResult)  # 写入测试实际结果
            my_log.info('注册的结果：{}'.format(result))


    @data(*cases)
    def test_login(self, case):  # 测试登陆

        my_log.info("开始执行第{}条用例".format(case.case_id, case.title))
        my_log.info('url:', case.url)
        my_log.info('data:', case.data)
        my_log.info('method:', case.method)
        my_log.info('expected:', case.expected)
        result = ApiMethod().login(case.url, case.data, case.method)
        try:
            self.assertEqual(case.expected, result)
            TestResult = "Pass"
        except AssertionError as e:
            TestResult = "Failed"
            my_log.error("断言出错了".format(e))
            raise e
        finally:
            self.write_login.write_excel(case.case_id+1, 7, result)  # 写入测试实际结果
            self.write_login.write_excel(case.case_id+1, 8, TestResult)  # 写入测试实际结果
            my_log.info('登陆的结果：{}'.format(result))

    # def test_recharge(self):  # 测试充值
    #     pass


if __name__=='__main__':  # 会自动的在当前文件里面加载test_文件开头的用例
    unittest.main()