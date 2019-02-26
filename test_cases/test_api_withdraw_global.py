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
withdraw_information = eval(config.get_value("WithDraw", "withdraw"))

from common.context import Context
import json

# 一个接口一个类，一个类一个方法
# 一个类，多个方法，多个接接口
# 一个类，一个方法，全部接口

"""
"""
# 导入日志文件
from log.test_api_log import MyLog
my_log = MyLog()

logger = logger.get_logger(logger_name='WithDrawTest')

from common.mysql import MysqlUtil_double

global origin_withdraw
origin_withdraw = None

@ddt
class WithDrawTest(unittest.TestCase):
    '这是测试提现接口的类'
    # 使用doexcel_study中的方法调用
    do_excel = DoExcel(contants.excel_file)  # 传入do_excel_study.xlsx
    cases_withdraw = do_excel.read_excel("withdraw")  # 读取withdraw_sheet

    @classmethod  # 为什么用类方法？ 整个类只执行一次！
    def setUpClass(cls):  # 每个测试类里面去运行的操作都放到类方法里面
        cls.request = Request()  # 实例化对象
        # cls.origin_withdraw = None
        # cls.updated_withdraw = None

    def setUp(self):
        # self.write_withdraw = DoExcel(contants.excel_file, "withdraw") # 创建一个对象写入
        logger.info("开始执行用例")

    def tearDown(self):
        logger.info("用例执行结束")

    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()  # 关闭session请求
        cls.mysql.close()  # 关闭数据库连接

    mysql = MysqlUtil_double(return_dict=True)

    @data(*cases_withdraw)
    def test_withdraw(self, case):  # 测试注册
        logger.info("开始执行第{}条用例: {}".format(case.case_id, case.title))
        logger.debug('url:{}'.format(case.url))
        logger.debug('data:{}'.format(case.data))
        logger.debug('method:{}'.format(case.method))
        logger.debug('expected:{}'.format(case.expected))

        withdraw_data_new = Context.replace_new(case.data)
        resp = self.request.request(case.method, case.url, withdraw_data_new)

        try:
            self.assertEqual(json.loads(case.expected)['msg'], json.loads(resp.text)['msg'])
            if resp.json()['msg'] == '登录成功':
                sql = 'select * from future.member where mobilephone = {0}'\
                    .format(json.loads(withdraw_data_new)['mobilephone'])
                results = self.mysql.fetch_all(sql)
                # # 首先判断是否有成功插入数据
                # self.assertEqual(1, len(results))
                member = results[0]  # 获取到这一条数据，是一个字典
                global origin_withdraw
                origin_withdraw = member['LeaveAmount']

            if resp.json()['msg'] == '取现成功':
                # global origin_withdraw
                # origin_withdraw = getattr(Context, 'origin_withdraw')
                sql2 = 'select * from future.member where mobilephone = {0}' \
                    .format(json.loads(withdraw_data_new)['mobilephone'])
                results2 = self.mysql.fetch_all(sql2)
                member2 = results2[0]  # 获取到这一条数据，是一个字典
                updated_withdraw = member2['LeaveAmount']  # 提现成功后获取最新的leaveamount值
                abs = origin_withdraw - updated_withdraw
                # print('abs', abs, type(abs))
                import decimal
                set_amount = decimal.Decimal(json.loads(withdraw_data_new)['amount'])  # 设置的金额转化成十进制数字
                self.assertEqual(set_amount, abs)  # 与设置的提现金额进行比对

            self.do_excel.write_excel('withdraw', case.case_id + 1, resp.text, 'PASS')  # 读取sheet，写入结果
            logger.info("第{0}用例执行结果：PASS".format(case.case_id))
        except AssertionError as e:
            self.do_excel.write_excel('withdraw', case.case_id + 1, resp.text, 'FAIL')
            logger.error("第{0}用例执行结果：FAIL".format(case.case_id))
            logger.error("断言出错了".format(e))
            raise e