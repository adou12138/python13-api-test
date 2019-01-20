# 当前项目的名称: python_13 
# 新文件名称：test_math_suite 
# 当前登录名：LuckyLu
# 创建日期：2019/1/11 16:29
# 文件IDE名称：PyCharm

import unittest
import HTMLTestRunnerNew

from test_cases.test_api_method import TestApiMethod
from common import contants

suite = unittest.TestSuite()

loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestApiMethod))

with open(contants.report_file, 'wb') as file:  # 引用common中的report地址
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                            verbosity=2,
                                            title='API TEST',
                                            description='THIS IS A API TEST',
                                            tester='lucky')
    runner.run(suite)  # 执行测试集里面的用例  F代表失败 .代表成功 e代表代码错误