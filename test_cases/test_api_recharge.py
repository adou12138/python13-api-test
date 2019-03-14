# coding: utf-8
# homework_01.23.19
# test_api_recharge 
# shen 
# 2019/1/21 22:07 

import unittest

from common import contants, logger
from common.do_excel_study import DoExcel  # 导入excel
from common.request import Request  # 导入api请求
from common.test_api_config import ReadConfig
from libext.ddtNew import ddt, data

# config = ReadConfig()
# # 正则配置
# recharge_information = eval(config.get_value("Recharge", "recharge"))

from common.context import Context
import json

"""
充值，先登录，然后走正常的充值成功流程，接着走异常流程
另一种，调用sessions的方法老师会给代码
"""

# 导入日志文件
from log.test_api_log import MyLog
my_log = MyLog()

logger = logger.get_logger(logger_name='RechargeTest')
from common.mysql import MysqlUtil_double

@ddt
class RechargeTest(unittest.TestCase):
    '这是测试充值接口的类'
    # 使用doexcel_study中的方法调用
    do_excel = DoExcel(contants.excel_file)  # 传入do_excel_study.xlsx
    cases_recharge = do_excel.read_excel("recharge")  # 读取register_sheet

    @classmethod  # 为什么用类方法？ 整个类只执行一次！
    def setUpClass(cls):  # 每个测试类里面去运行的操作都放到类方法里面
        cls.request = Request()  # 实例化对象

    def setUp(self):
        # self.write_recharge = DoExcel(contants.excel_file, "recharge") # 创建一个对象写入
        logger.info("开始执行用例")

    def tearDown(self):
        logger.info("用例执行结束")

    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()  # 关闭session请求
        cls.mysql.close()  # 关闭数据库连接

    mysql = MysqlUtil_double(return_dict=True)

    @data(*cases_recharge)
    def test_recharge(self, case):  # 测试注册
        logger.info("开始执行第{}条用例: {}".format(case.case_id, case.title))
        logger.debug('url:{}'.format(case.url))
        logger.debug('data:{}'.format(case.data))
        logger.debug('method:{}'.format(case.method))
        logger.debug('expected:{}'.format(case.expected))

        # recharge_data_new = Context.replace(case.data, recharge_information)
        recharge_data_new = Context.replace_new(case.data)  # 调用类的方法替换参数
        resp = self.request.request(case.method, case.url, recharge_data_new)

        try:
            self.assertEqual(json.loads(case.expected)['msg'], json.loads(resp.text)['msg'])
            if json.loads(resp.text)['msg'] == '登录成功':
                sql = "'select * from future.member where mobilephone = '{0}'".format(json.loads(recharge_data_new)['mobilephone'])
                results = self.mysql.fetch_all(sql)
                member = results[0]  # 获取到这一条数据，是一个字典
                # 首先判断是否有成功插入数据
                # self.assertEqual(1, len(results))
                # old_recharge = member['LeaveAmount']
                # print(old_recharge)
                with open(contants.recharge_test_file, 'w') as r:  # 登陆成功后，写入member初始leaveamount的值
                    r.write(str(member['LeaveAmount']))
            if resp.json()['msg'] == '充值成功':
                sql2 = 'select * from future.member where mobilephone = {0}' \
                    .format(json.loads(recharge_data_new)['mobilephone'])
                results2 = self.mysql.fetch_all(sql2)
                member2 = results2[0]
                updated_recharge = member2['LeaveAmount']  # 充值成功后获取最新的leaveamount值
                with open(contants.recharge_test_file, 'r') as r:
                    origin_recharge = r.read()
                import decimal
                origin_recharge_decimal = decimal.Decimal(origin_recharge)
                add = (updated_recharge - origin_recharge_decimal)
                setup_amount = json.loads(recharge_data_new)['amount']  # 取出设置的金额转成十进制数字
                setup_amount_decimal = decimal.Decimal(setup_amount)
                self.assertEqual(setup_amount_decimal, add)  # 与设置的提现金额进行比对
            self.do_excel.write_excel('recharge', case.case_id + 1, resp.text, 'PASS')  # 读取sheet，写入结果
            logger.info("第{0}用例执行结果：PASS".format(case.case_id))
        except AssertionError as e:
            self.do_excel.write_excel('recharge', case.case_id + 1, resp.text, 'FAIL')
            logger.error("第{0}用例执行结果：FAIL".format(case.case_id))
            logger.error("断言出错了".format(e))
            raise e