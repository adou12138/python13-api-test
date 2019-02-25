# coding: utf-8
# python13-api-test 
# test_api_regitser 
# shen 
# 2019/1/21 23:00 

import unittest

from common import contants, logger
from common.do_excel_study import DoExcel  # 导入excel
from common.request import Request  # 导入api请求
from common.test_api_config import ReadConfig
from libext.ddtNew import ddt, data

config = ReadConfig()
# 正则配置
add_information = eval(config.get_value("Add", "add"))

from common.context import Context
import json

# 一个接口一个类，一个类一个方法
# 一个类，多个方法，多个接接口
# 一个类，一个方法，全部接口

# 导入日志文件
from log.test_api_log import MyLog
my_log = MyLog()

logger = logger.get_logger(logger_name='AddTest')

from common.mysql import MysqlUtil_double

@ddt
class AddTest(unittest.TestCase):
    '这是测试管理员新增项目接口的类'
    # 使用doexcel_study中的方法调用
    do_excel = DoExcel(contants.excel_file)  # 传入do_excel_study.xlsx
    cases_add = do_excel.read_excel("add")  # 读取add_sheet

    @classmethod  # 为什么用类方法？ 整个类只执行一次！
    def setUpClass(cls):  # 每个测试类里面去运行的操作都放到类方法里面
        cls.request = Request()  # 实例化对象

    def setUp(self):
        # self.write_register = DoExcel(contants.excel_file, "add") # 创建一个对象写入
        logger.info("开始执行用例")

    def tearDown(self):
        logger.info("用例执行结束")

    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()  # 关闭session请求
        cls.mysql.close()  # 关闭数据库连接

    mysql = MysqlUtil_double(return_dict=True)

    @data(*cases_add)
    def test_add(self, case):  # 测试注册
        logger.info("开始执行第{}条用例: {}".format(case.case_id, case.title))
        logger.debug('url:{}'.format(case.url))
        logger.debug('data:{}'.format(case.data))
        logger.debug('method:{}'.format(case.method))
        logger.debug('expected:{}'.format(case.expected))

        add_data_new = Context.replace(case.data, add_information)
        resp = self.request.request(case.method, case.url, add_data_new)

        try:
            self.assertEqual(json.loads(case.expected)['msg'], json.loads(resp.text)['msg'])

            if resp.json()['msg'] == '加标成功':
                sql = "select * from future.loan where memberid='{0}' " \
                      "order by createTime desc limit 1".format(json.loads(add_data_new)['memberId'])
                results = self.mysql.fetch_all(sql)
                # 首先判断是否有成功插入数据
                self.assertEqual(1, len(results))
                add_loan = results[0]  # 获取到这一条数据，是一个字典
                # print(add_loan)
                self.assertEqual(1, add_loan['Status'])  # 判断加标成功状态是1
                self.assertEqual(json.loads(add_data_new)['title'], add_loan['Title'])  # 判断加标标题
                self.assertEqual(int(json.loads(add_data_new)['amount']), add_loan['Amount'])  # 判断加标金额
                # self.assertEqual(int(json.loads(add_data_new)['loanRate']), add_loan['LoanRate'])  # 判断加标LoanRate
                self.assertEqual(int(json.loads(add_data_new)['loanTerm']), add_loan['LoanTerm'])  # 判断加标LoanTerm
                self.assertEqual(int(json.loads(add_data_new)['loanDateType']), add_loan['LoanDateType'])  # 判断加标LoanDataType
                self.assertEqual(int(json.loads(add_data_new)['repaymemtWay']), add_loan['RepaymemtWay'])  # 判断加标RepaymentWay
                # self.assertEqual(json.loads(add_data_new)['biddingDays'], add_loan['BiddingDays'])  # 判断加标BiddingDays
            self.do_excel.write_excel('add', case.case_id + 1, resp.text, 'PASS')  # 读取sheet，写入结果
            logger.info("第{0}用例执行结果：PASS".format(case.case_id))
        except AssertionError as e:
            self.do_excel.write_excel('add', case.case_id + 1, resp.text, 'FAIL')
            logger.error("第{0}用例执行结果：FAIL".format(case.case_id))
            logger.error("断言出错了".format(e))
            raise e