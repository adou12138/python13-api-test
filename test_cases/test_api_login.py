# coding: utf-8
# python13-api-test 
# test_api_regitser 
# shen 
# 2019/1/21 23:00+

import unittest

from common import contants, logger
from common.do_excel_study import DoExcel  # 导入excel
from common.request import Request  # 导入api请求
from common.test_api_config import ReadConfig
from libext.ddtNew import ddt, data

config = ReadConfig()
# 正则配置
login_information = eval(config.get_value("Login", "login"))

from common.context import Context
import json

# 一个接口一个类，一个类一个方法
# 一个类，多个方法，多个接接口
# 一个类，一个方法，全部接口

# 导入日志文件
from log.test_api_log import MyLog
my_log = MyLog()

logger = logger.get_logger(logger_name='LoginTest')
# 如果logger_name='case'，就是一个单例模式，添加控制台的文本输出样式

@ddt
class LogInTest(unittest.TestCase):
    '这是测试登陆接口的类'
    # 使用doexcel_study中的方法调用
    do_excel = DoExcel(contants.excel_file)  # 传入do_excel_study.xlsx
    cases_login = do_excel.read_excel("login")  # 读取login_sheet

    @classmethod  # 为什么用类方法？ 整个类只执行一次！
    def setUpClass(cls):  # 每个测试类里面去运行的操作都放到类方法里面
        cls.request = Request()  # 实例化对象

    def setUp(self):
        # self.write_register = DoExcel(contants.excel_file, "login") # 创建一个对象写入
        logger.info("开始执行用例")

    def tearDown(self):
        logger.info("用例执行结束")

    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()  # 关闭session请求
        # cls.mysql.close()  # 关闭数据库连接

    @data(*cases_login)
    def test_login(self, case):  # 测试注册
        logger.info("开始执行第{}条用例: {}".format(case.case_id, case.title))
        logger.debug('url:{}'.format(case.url))
        logger.debug('data:{}'.format(case.data))
        logger.debug('method:{}'.format(case.method))
        logger.debug('expected:{}'.format(case.expected))

        login_data_new = Context.replace(case.data, login_information)
        resp = self.request.request(case.method, case.url, login_data_new)

        try:
            self.assertEqual(json.loads(case.expected)['msg'], json.loads(resp.text)['msg'])
            self.do_excel.write_excel('login', case.case_id + 1, resp.text, 'PASS')  # 读取sheet，写入结果
            logger.info("第{0}用例执行结果：PASS".format(case.case_id))
        except AssertionError as e:
            self.do_excel.write_excel('login', case.case_id + 1, resp.text, 'FAIL')
            logger.error("第{0}用例执行结果：FAIL".format(case.case_id))
            logger.error("断言出错了".format(e))
            raise e



