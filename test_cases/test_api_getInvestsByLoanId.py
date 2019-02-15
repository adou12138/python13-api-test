# coding: utf-8
# homework_01.23.19
# test_api_recharge 
# shen 
# 2019/1/21 22:07 

import unittest
from common import contants
from ddt import ddt, data

from common.do_excel_study import DoExcel  # 导入excel
from common.request import Request  # 导入api请求

from common.test_api_config import ReadConfig
config = ReadConfig()

from common.context import Context
import json

"""
充值，先登录，然后走正常的充值成功流程，接着走异常流程
另一种，调用sessions的方法老师会给代码
"""

# 一个接口一个类，一个类一个方法
# 一个类，多个方法，多个接接口
# 一个类，一个方法，全部接口

# 导入日志文件
from log.test_api_log import MyLog
my_log = MyLog()

import logger
logger = logger.get_logger(logger_name='GetInvestsByLoanIdTest')

@ddt
class GetInvestsByLoanIdTest(unittest.TestCase):
    '这是测试获取标的所有投资接口的类'
    # 使用doexcel_study中的方法调用
    do_excel = DoExcel(contants.excel_file)  # 传入do_excel_study.xlsx
    cases_getInvestsByLoanId = do_excel.read_excel("getInvestsByLoanId")  # 读取getInvestsByLoanId

    @classmethod  # 为什么用类方法？ 整个类只执行一次！
    def setUpClass(cls):  # 每个测试类里面去运行的操作都放到类方法里面
        cls.request = Request()  # 实例化对象

    def setUp(self):
        # self.write_recharge = DoExcel(contants.excel_file, "getInvestsByLoanId") # 创建一个对象写入
        logger.info("开始执行用例")

    def tearDown(self):
        logger.info("用例执行结束")

    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()  # 关闭session请求

    @data(*cases_getInvestsByLoanId)
    def test_getInvestsByLoanId(self, case):  # 测试注册
        logger.info("开始执行第{}条用例: {}".format(case.case_id, case.title))
        logger.debug('url:{}'.format(case.url))
        logger.debug('data:{}'.format(case.data))
        logger.debug('method:{}'.format(case.method))
        logger.debug('expected:{}'.format(case.expected))

        getInvestsByLoanId_data_new = Context.replace_new(case.data)  # 调用类的方法替换参数
        resp = self.request.request(case.method, case.url, getInvestsByLoanId_data_new)

        try:
            self.assertEqual(json.loads(case.expected)['msg'], json.loads(resp.text)['msg'])
            self.do_excel.write_excel('getInvestsByLoanId', case.case_id + 1, resp.text, 'PASS')  # 读取sheet，写入结果
            logger.info("第{0}用例执行结果：PASS".format(case.case_id))
        except AssertionError as e:
            self.do_excel.write_excel('getInvestsByLoanId', case.case_id + 1, resp.text, 'FAIL')
            logger.error("第{0}用例执行结果：FAIL".format(case.case_id))
            logger.error("断言出错了".format(e))
            raise e