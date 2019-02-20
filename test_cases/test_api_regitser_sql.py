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

from common.mysql import MysqlUtil_double
import json

from common.context import Context
# 一个接口一个类，一个类一个方法
# 一个类，多个方法，多个接接口
# 一个类，一个方法，全部接口

"""
手机号码注册 电话号码数据库取值，名字随机字符
1.数据库里面查最大的手机号+1
2.case.data里面的手机号码给替换掉
3.然后再去请求

投资必须先有标的，loan，自己创建一个标的
提bug到禅道
"""
# 导入日志文件
from log.test_api_log import MyLog
my_log = MyLog()

logger = logger.get_logger(logger_name='RegisterTest')

@ddt
class RegisterTest(unittest.TestCase):
    '这是测试注册接口的类'
    # 使用doexcel_study中的方法调用
    do_excel = DoExcel(contants.excel_file)  # 传入do_excel_study.xlsx
    cases_register = do_excel.read_excel("register")  # 读取register_sheet

    @classmethod  # 为什么用类方法？ 整个类只执行一次！
    def setUpClass(cls):  # 每个测试类里面去运行的操作都放到类方法里面
        cls.request = Request()  # 实例化对象

    def setUp(self):
        # self.write_register = DoExcel(contants.excel_file, "register") # 创建一个对象写入
        logger.info("开始执行用例")

    def tearDown(self):
        logger.info("用例执行结束")

    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()  # 关闭session请求
        cls.mysql.close()  # 关闭数据库连接

    # 测试一下放在setup里面效果 是不行的
    mysql = MysqlUtil_double(return_dict=True)
    sql = "select max(mobilephone) as max_phone from future.member"
    max = mysql.fetch_one(sql)['max_phone']  # 执行SQL，并且返回最近的一条数据，是元祖，使用下标取第一个值
    # print(max)

    @data(*cases_register)
    def test_register(self, case):  # 测试注册
        logger.info("开始执行第{}条用例: {}".format(case.case_id, case.title))
        logger.debug('url:{}'.format(case.url))
        logger.debug('data:{}'.format(case.data))
        logger.debug('method:{}'.format(case.method))
        logger.debug('expected:{}'.format(case.expected))
        data_dict = json.loads(case.data)
        if data_dict['mobilephone'] == '#@mobilephone':
            # 取最大电话号码+1
            data_dict['mobilephone'] = int(self.max)+1
        # resp = self.request.request(case.method, case.url, data_dict)

        data_dict = json.dumps(data_dict)  # 把字典转换成字符串传入context进行转换
        # print(data_dict, type(data_dict))
        register_data_new = Context.replace_new(data_dict)
        resp = self.request.request(case.method, case.url, register_data_new)

        try:
            self.assertEqual(case.expected, resp.text, 'register error')
            if resp.json()['msg'] == '注册成功':
                sql = 'select * from future.member where mobilephone = {0}'\
                    .format(json.loads(data_dict)['mobilephone'])
                results = self.mysql.fetch_all(sql)
                # 首先判断是否有成功插入数据
                self.assertEqual(1, len(results))
                member = results[0]  # 获取到这一条数据，是一个字典
                self.assertEqual(0, member['LeaveAmount'])  # 判断注册成功余额应该是0
                self.assertEqual(1, member['Type'])  # 判断注册用户类型是1
                if 'regname' in json.loads(register_data_new).keys():
                    self.assertEqual(json.loads(register_data_new)['regname'], member['RegName'])
                else:
                    self.assertEqual('小蜜蜂', member['RegName'])
            # 一致就写入Excel的结果为PASS，并且
            self.do_excel.write_excel('register', case.case_id + 1, resp.text, 'PASS')  # 读取sheet，写入结果
            logger.info("第{0}用例执行结果：PASS".format(case.case_id))
        except AssertionError as e:
            self.do_excel.write_excel('register', case.case_id + 1, resp.text, 'FAIL')
            logger.error("第{0}用例执行结果：FAIL".format(case.case_id))
            logger.error("断言出错了".format(e))
            raise e