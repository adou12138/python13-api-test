# coding: utf-8
# python13-api-test 
# test_api_regitser 
# shen 
# 2019/1/21 23:00 

import unittest
from common import contants
from ddt import ddt, data

from common.do_excel_study import DoExcel  # 导入excel
from common.request import Request  # 导入api请求

from common.test_api_config import ReadConfig
config = ReadConfig()
# 正则配置
# audit_information = eval(config.get_value("Audit", "audit"))  # ? 还没有设置

from common.context import Context
import json

# 一个接口一个类，一个类一个方法
# 一个类，多个方法，多个接接口
# 一个类，一个方法，全部接口

# 导入日志文件
from log.test_api_log import MyLog
my_log = MyLog()

from log import logger
logger = logger.get_logger(logger_name='AuditTest')

from common.mysql import MysqlUtil

@ddt
class AuditTest(unittest.TestCase):
    '这是测试审核接口的类'
    # 使用doexcel_study中的方法调用
    do_excel = DoExcel(contants.excel_file)  # 传入do_excel_study.xlsx
    cases_audit = do_excel.read_excel("audit")  # 读取audit_sheet

    @classmethod  # 为什么用类方法？ 整个类只执行一次！
    def setUpClass(cls):  # 每个测试类里面去运行的操作都放到类方法里面
        cls.request = Request()  # 实例化对象
        cls.mysql = MysqlUtil()

    def setUp(self):
        # self.write_register = DoExcel(contants.excel_file, "audit") # 创建一个对象写入
        logger.info("开始执行用例")

    def tearDown(self):
        logger.info("用例执行结束")

    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()  # 关闭session请求
        cls.mysql.close()  # 关闭数据库连接

    @data(*cases_audit)
    def test_audit(self, case):  # 测试注册
        logger.info("开始执行第{}条用例: {}".format(case.case_id, case.title))
        logger.debug('url:{}'.format(case.url))
        logger.debug('data:{}'.format(case.data))
        logger.debug('method:{}'.format(case.method))
        logger.debug('expected:{}'.format(case.expected))

        audit_data_new = Context.replace_new(case.data)
        resp = self.request.request(case.method, case.url, audit_data_new)

        # resp = self.request.request(case.method, case.url, case.data)
        try:
            # self.assertEqual(json.loads(case.expected)['msg'], json.loads(resp.text)['msg'])
            self.assertEqual(json.loads(case.expected)['code'], resp.json()['code'], "member_list error")
            self.do_excel.write_excel('audit', case.case_id + 1, resp.text, 'PASS')  # 读取sheet，写入结果
            logger.info("第{0}用例执行结果：PASS".format(case.case_id))

            # 判断是否加标成功，如果成功就按照借款人ID去数据库查询最新的加标的记录
            if resp.json()['msg'] == '加标成功':
                loan_member_id = getattr(Context, 'loan_member_id')
                sql = "select id from future.loan where memberid='{0}' " \
                      "order by createTime desc limit 1".format(loan_member_id)
                loan_id = self.mysql.fetch_one(sql)[0]
                setattr(Context, 'loan_id', str(loan_id))  # 和excel中的名字保持一致, 记得转成字符串str，后续要通过正则替换

        except AssertionError as e:
            self.do_excel.write_excel('audit', case.case_id + 1, resp.text, 'FAIL')
            logger.error("第{0}用例执行结果：FAIL".format(case.case_id))
            logger.error("断言出错了".format(e))
            raise e