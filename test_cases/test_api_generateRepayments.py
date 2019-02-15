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
# # 正则配置
# recharge_information = eval(config.get_value("Recharge", "recharge"))

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

from log import logger
logger = logger.get_logger(logger_name='GenerateRepaymentsTest')
from common.mysql import MysqlUtil

@ddt
class GenerateRepaymentsTest(unittest.TestCase):
    '这是测试回款流程的类'
    # 使用doexcel_study中的方法调用
    do_excel = DoExcel(contants.excel_file)  # 传入do_excel_study.xlsx
    cases_generateRepayments = do_excel.read_excel("generateRepayments")  # 读取generateRepayments

    @classmethod  # 为什么用类方法？ 整个类只执行一次！
    def setUpClass(cls):  # 每个测试类里面去运行的操作都放到类方法里面
        cls.request = Request()  # 实例化对象
        cls.mysql = MysqlUtil()

    def setUp(self):
        # self.write_recharge = DoExcel(contants.excel_file, "generateRepayments") # 创建一个对象写入
        logger.info("开始执行用例")

    def tearDown(self):
        logger.info("用例执行结束")

    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()  # 关闭session请求
        cls.mysql.close()  # 关闭数据库连接

    @data(*cases_generateRepayments)
    def test_generateRepayments(self, case):  # 测试注册
        logger.info("开始执行第{}条用例: {}".format(case.case_id, case.title))
        logger.debug('url:{}'.format(case.url))
        logger.debug('data:{}'.format(case.data))
        logger.debug('method:{}'.format(case.method))
        logger.debug('expected:{}'.format(case.expected))

        generateRepayments_data_new = Context.replace_new(case.data)  # 调用类的方法替换参数
        resp = self.request.request(case.method, case.url, generateRepayments_data_new)

        try:
            self.assertEqual(json.loads(case.expected)['code'], resp.json()['code'], "member_list error")
            # self.assertEqual(str(case.expected), resp.json()['code'], "generateRepayments error")
            self.do_excel.write_excel('generateRepayments', case.case_id + 1, resp.text, 'PASS')  # 读取sheet，写入结果
            logger.info("第{0}用例执行结果：PASS".format(case.case_id))

            # 判断是否加标成功，如果成功就按照借款人ID去数据库查询最新的加标的记录
            if resp.json()['msg'] == '加标成功':
                loan_member_id = getattr(Context, 'loan_member_id')
                sql = "select id from future.loan where memberid='{0}' " \
                      "order by createTime desc limit 1".format(loan_member_id)
                loan_id = self.mysql.fetch_one(sql)[0]
                setattr(Context, 'loan_id', str(loan_id))  # 和excel中的名字保持一致, 记得转成字符串str，后续要通过正则替换

        except AssertionError as e:
            self.do_excel.write_excel('generateRepayments', case.case_id + 1, resp.text, 'FAIL')
            logger.error("第{0}用例执行结果：FAIL".format(case.case_id))
            logger.error("断言出错了".format(e))
            raise e