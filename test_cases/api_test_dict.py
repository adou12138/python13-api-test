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
cases = DoExcel('../datas/luckytest.xlsx', 'login').read_excel()

@ddt
class TestApiMethod(unittest.TestCase):
    '这是测试接口的类'
    def setup(self):
        self.write = DoExcel('../datas/luckytest.xlsx', 'login')  # 创建一个对象写入
        print("开始执行用例")

    def tearDown(self):
        print("用例执行结束")

    # def test_register(self):  # 测试注册
    #     pass

    @data(*cases)
    def test_login(self, case):  # 测试登陆
        print("开始执行第{}条用例".format(case['case_id'], case['title']))
        print('url:', case['url'])
        print('data:', case['data'])
        print('method:', case['method'])
        print('expected:', case['expected'])
        result = ApiMethod().login(case['url'], case['data'], case['method'])
        print('result:', result)
        try:
            self.assertEqual(case['expected'], result)
            TestResult = "Pass"
        except AssertionError as e:
            TestResult = "Failed"
            print("断言出错了".format(e))
            raise e
        finally:
            self.write.write_excel(case['case_id']+1, 7, result)  # 写入测试实际结果
            self.write.write_excel(case['case_id']+1, 8, TestResult)  # 写入测试实际结果
            print('登陆的结果：{}'.format(result))

    # def test_recharge(self):  # 测试充值
    #     pass


if __name__ == '__main__':  # 会自动的在当前文件里面加载test_文件开头的用例
    unittest.main()