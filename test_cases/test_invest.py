# coding: utf-8
# python13-api-test 
# test_invest 
# shen 
# 2019/1/28 23:13 

import unittest
from common import contants
from ddt import ddt, data

from common.do_excel_study import DoExcel  # 导入excel
from common.request import Request  # 导入api请求

from common.mysql import MysqlUtil
from common.context import Context

import json

# 导入日志文件
from log.test_api_log import MyLog
my_log = MyLog()

import logger
logger = logger.get_logger(logger_name='TestInvest')

@ddt
class TestInvest(unittest.TestCase):
    '这是测试投资流程接口的类'
    do_excel = DoExcel(contants.excel_file)  # 传入do_excel_study.xlsx
    cases_invest = do_excel.read_excel("invest")  # 读取invest_sheet

    @classmethod  # 为什么用类方法？ 整个类只执行一次！
    def setUpClass(cls):  # 每个测试类里面去运行的操作都放到类方法里面
        print("\m这是一个类方法")
        cls.request = Request()  # 实例化对象
        cls.mysql = MysqlUtil()

    def setUp(self):  # 每个测试方法里面去运行的操作都放到类方法里面
        logger.debug("这是一个setUp")
        logger.info("开始执行用例")

    def tearDown(self):
        logger.info("用例执行结束")

    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()  # 关闭session请求
        cls.mysql.close()  # 关闭数据库连接

    @data(*cases_invest)
    def test_invest(self, case):  # 测试注册
        logger.info("开始执行第{}条用例: {}".format(case.case_id, case.title))
        logger.debug('url:{}'.format(case.url))
        logger.debug('data:{}'.format(case.data))
        logger.debug('method:{}'.format(case.method))
        logger.debug('expected:{}'.format(case.expected))

        # 查找参数化的测试数据，动态替换
        data_new = Context.replace_new(case.data)  # Str测试数据
        # 使用封装好的request 来完成请求
        resp = self.request.request(case.method, case.url, data_new)
        try:
            # self.assertEqual(str(case.expected), resp.json()['code'], "invest error")
            self.assertEqual(json.loads(case.expected)['code'], resp.json()['code'], "invest error")
            # self.assertEqual(case.expected, json.loads(resp.text)['code'], "invest error")
            # 一致就写入Excel的结果为PASS，并且
            self.do_excel.write_excel('invest', case.case_id+1, resp.text, "Pass")  # 写入测试实际结果
            logger.info('第{}条用例执行结果：PASS'.format(case.case_id))

            # 判断是否加标成功，如果成功就按照借款人ID去数据库查询最新的加标的记录
            if resp.json()['msg'] == '加标成功':
                loan_member_id = getattr(Context, 'loan_member_id')
                sql = "select id from future.loan where memberid='{0}' " \
                      "order by createTime desc limit 1".format(loan_member_id)
                loan_id = self.mysql.fetch_one(sql)[0]
                setattr(Context, 'loan_id', str(loan_id))  # 和excel中的名字保持一致, 记得转成字符串str，后续要通过正则替换

        except AssertionError as e:
            self.do_excel.write_excel('invest', case.case_id+1, resp.text, "Failed")  # 写入测试实际结果
            logger.error('第{}条用例执行结果：FAIL'.format(case.case_id))
            logger.error("断言出错了".format(e))
            raise e

if __name__ == '__main__':
    pass