# 当前项目的名称: python_13 
# 新文件名称：test_math_suite 
# 当前登录名：LuckyLu
# 创建日期：2019/1/11 16:29
# 文件IDE名称：PyCharm

"""
配置jenkins？
# import sys
# import os
#
# project = 'python13-api-test'  # 工作项目根目录
# sys.path.append(os.getcwd().split(project)[0] + project)
"""

import unittest
import HTMLTestRunnerNew

import sys
sys.path.append('../')

from test_cases.test_api_method import TestApiMethod  # 导入所有的测试用例

from test_cases.test_api_regitser import RegisterTest  # 导入注册
from test_cases.test_api_login import LogInTest  # 导入登陆
# from test_cases import test_api_regitser  # 模块方式导入注册
# from test_cases import test_api_login  # 模块导入登陆


# from test_cases.test_api_recharge import RechargeTest  # 导入充值
# from test_cases.test_api_withdraw import WithDrawTest  # 导入提现
from test_cases.test_api_add import AddTest  # 导入add
from test_cases.test_api_bidloan import BidLoanTest  # 导入bidloan
from test_cases.test_api_audit import AuditTest  # 导入audit

suite = unittest.TestSuite()  # 创建对象
loader = unittest.TestLoader()

# suite.addTest(loader.loadTestsFromTestCase(TestApiMethod))  # 执行所有的测试用例

suite.addTest(loader.loadTestsFromTestCase(RegisterTest))  # 执行注册
suite.addTest(loader.loadTestsFromTestCase(LogInTest))  # 执行登陆
# suite.addTest(loader.loadTestsFromModule(test_api_regitser))  # 模块方式执行注册
# suite.addTest(loader.loadTestsFromModule(test_api_login))  # 模块方式执行登陆

# suite.addTest(loader.loadTestsFromTestCase(RechargeTest))  # 执行充值
# suite.addTest(loader.loadTestsFromTestCase(WithDrawTest))  # 执行提现
# suite.addTest(loader.loadTestsFromTestCase(AddTest))  # 执行add
# suite.addTest(loader.loadTestsFromTestCase(BidLoanTest))  # 执行bidloan
# suite.addTest(loader.loadTestsFromTestCase(AuditTest))  # 执行bidloan

from common import contants
import time
now = time.strftime('%Y-%m-%d-%H-%M-%S')  # 获取当前系统的时间，生成字符串
path = contants.report_file+now+'.html'

with open(path, 'wb+') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                            verbosity=2,
                                            title='API TEST',
                                            description='THIS IS A API TEST REPORT  ',
                                            tester='lucky')
    runner.run(suite)

# with open(contants.report_file, 'wb') as file:  # 引用common中的report地址
#     runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
#                                             verbosity=2,
#                                             title='API TEST',
#                                             description='THIS IS A API TEST REPORT',
#                                             tester='lucky')
#     runner.run(suite)  # 执行测试集里面的用例  F代表失败 .代表成功 e代表代码错误