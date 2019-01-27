# coding: utf-8
# 当前项目的名称: python13-api-test 
# 新文件名称：api_test 
# 当前登录名：LuckyLu
# 创建日期：2019/1/17 15:45
# 文件IDE名称：PyCharm

import unittest
from common import contants
from ddt import ddt, data

from common.do_excel import DoExcel  # 导入excel
from common.request import Request  # 导入api请求

import json
from common.mysql import MysqlUtil  # 导入数据库类
import warnings  # 导入warning库 忽略 ResourceWarning: unclosed file <_io.TextIOWrapper

# 一个接口一个类，一个类一个方法
# 一个类，多个方法，多个接接口
# 一个类，一个方法，全部接口

from common.test_api_config import ReadConfig  # 导入配置类
config = ReadConfig()
# 正则配置
login_information = eval(config.get_value("Login", "login"))
recharge_information = eval(config.get_value("Recharge", "recharge"))
withdraw_information = eval(config.get_value("WithDraw", "withdraw"))

"""
config配置参数
"""
recharge_member_phone = config.get_int("RechargeMember", "recharge_member1_phone")
recharge_member_id = config.get_int("RechargeMember", "recharge_member1_id")
recharge_member_pwd = config.get_int("RechargeMember", "recharge_member_pwd")  # login登录配置

withdraw_member_phone = config.get_int("WithDrawMember", "withdraw_member1_phone")
withdraw_member_id = config.get_int("WithDrawMember", "withdraw_member1_id")
audit_member_phone = config.get_int("AuditMember", "audit_member_phone")
audit_member_id = config.get_int("AuditMember", "audit_member_id")




from common.context import replace
"""
手机号码注册 电话号码数据库取值，名字随机字符
1.数据库里面查最大的手机号+1
2.case.data里面的手机号码给替换掉
3.然后再去请求
"""
from log.test_api_log import MyLog  # 导入日志类
my_log = MyLog()

Max = None

@ddt
class TestApiMethod(unittest.TestCase):
    '这是测试接口的类'
    cases_register = DoExcel(contants.excel_file, "register").read_excel()
    cases_login = DoExcel(contants.excel_file, "login").read_excel()
    cases_recharge = DoExcel(contants.excel_file, "recharge").read_excel()
    cases_withdraw = DoExcel(contants.excel_file, "withdraw").read_excel()
    cases_add = DoExcel(contants.excel_file, "add").read_excel()
    cases_audit = DoExcel(contants.excel_file, "audit").read_excel()
    cases_bidLoan = DoExcel(contants.excel_file, "bidLoan").read_excel()



    @classmethod  # 每个测试类里面去运行的操作都放到类方法里面
    def setUpClass(cls):  # 为什么用类方法？ 整个类只执行一次！
        cls.request = Request()

    def setUp(self):
        # warnings.simplefilter("ignore", ResourceWarning)
        self.write_register = DoExcel(contants.excel_file, "register") # 创建一个对象写入
        self.write_login = DoExcel(contants.excel_file, "login")
        self.write_recharge = DoExcel(contants.excel_file, "recharge")
        self.write_withdraw = DoExcel(contants.excel_file, "withdraw")
        self.write_add = DoExcel(contants.excel_file, "add")
        self.write_audit = DoExcel(contants.excel_file, "audit")
        self.write_bidLoan = DoExcel(contants.excel_file, "bidLoan")

        my_log.info("开始执行用例")

    def tearDown(self):
        my_log.info("用例执行结束")
        pass

    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()  # 关闭session会话
        # cls.cursor.close()
        cls.mysql.close()

    mysql = MysqlUtil()
    sql = "select max(mobilephone) from future.member"
    max = mysql.fetch_one(sql)[0]  # 执行SQL，并且返回最近的一条数据，是元祖，使用下标取第一个值
    global Max
    Max = int(max)+1

    @unittest.skip("忽略测试，不要运行")
    @data(*cases_register)
    def test_register(self, case):  # 测试注册
        my_log.info("开始执行第{}条用例: {}".format(case.case_id, case.title))
        my_log.info('url:{}'.format(case.url))
        my_log.info('data:{}'.format(case.data))
        my_log.info('method:{}'.format(case.method))
        my_log.info('expected:{}'.format(case.expected))
        dict_data = json.loads(case.data)
        if dict_data['mobilephone'] == '#@mobilephone':

            dict_data['mobilephone'] = int(self.max)+1
            # print(dict_data)
            # print(type(dict_data))

        result = self.request.request(case.method, case.url, dict_data)
        try:
            self.assertEqual(case.expected, result.text)
            TestResult = "Pass"
        except AssertionError as e:
            TestResult = "Failed"
            my_log.error("断言出错了".format(e))
            raise e
        finally:
            self.write_register.write_excel(case.case_id+1, result.text, TestResult)  # 写入测试实际结果
            my_log.info('注册的结果：{}'.format(json.loads(result.text)['msg']))

    @unittest.skip("忽略测试，不要运行")
    @data(*cases_login)
    def test_login(self, case):  # 测试登陆
        my_log.info("开始执行第{}条用例: {}".format(case.case_id, case.title))
        my_log.info('url:{}'.format(case.url))
        my_log.info('data:{}'.format(case.data))
        my_log.info('method:{}'.format(case.method))
        my_log.info('expected:{}'.format(case.expected))

        login_data_new = replace(case.data, login_information)
        result = self.request.request(case.method, case.url, login_data_new)

        """
        # 读取配置替换参数
        # login_dict = json.loads(case.data)
        # if login_dict["mobilephone"] == "${login_mobile_phone}":
        #     login_dict["mobilephone"] = recharge_member_phone
        # if login_dict["pwd"] == "${login_mobile_pwd}":
        #     login_dict["pwd"] = recharge_member_pwd
        # result = self.request.request(case.method, case.url, login_dict)
        """

        try:
            # self.assertEqual(case.expected, result.text)
            self.assertEqual(json.loads(case.expected)['msg'], json.loads(result.text)['msg'])
            TestResult = "Pass"
        except AssertionError as e:
            TestResult = "Failed"
            my_log.error("断言出错了".format(e))
            raise e
        finally:
            self.write_login.write_excel(case.case_id+1, result.text, TestResult)  # 写入测试实际结果
            my_log.info('登陆的结果：{}'.format(json.loads(result.text)['msg']))

    @unittest.skip("忽略测试，不要运行")
    @data(*cases_recharge)
    def test_recharge(self, case):  # 测试充值
        # my_log.info("开始执行第{}条用例: {}".format(case.case_id, case.title))
        # my_log.info('url:{}'.format(case.url))
        # my_log.info('data:{}'.format(case.data))
        # my_log.info('method:{}'.format(case.method))
        # my_log.info('expected:{}'.format(case.expected))

        recharge_data_new = replace(case.data, recharge_information)
        result = self.request.request(case.method, case.url, recharge_data_new)

        """
        recharge_dict = json.loads(case.data)
        if recharge_dict["mobilephone"] == "$$mobilephone$$":
            recharge_dict["mobilephone"] = recharge_member_phone
        result = self.request.request(case.method, case.url, recharge_dict)
        """
        try:
            self.assertEqual(json.loads(case.expected)["msg"], json.loads(result.text)["msg"])
            TestResult = "Pass"
        except AssertionError as e:
            TestResult = "Failed"
            my_log.error("断言出错了".format(e))
            raise e
        finally:
            self.write_recharge.write_excel(case.case_id+1, result.text, TestResult)  # 写入测试实际结果
            my_log.info('充值的结果：{}'.format(json.loads(result.text)["msg"]))  # 第一条用例登陆失败，写入的对比结果不对

    # @unittest.skip("忽略测试，不要运行")
    @data(*cases_withdraw)
    def test_withdraw(self, case):  # 测试取现
        my_log.info("开始执行第{}条用例: {}".format(case.case_id, case.title))
        my_log.info('url:{}'.format(case.url))
        my_log.info('data:{}'.format(case.data))
        my_log.info('method:{}'.format(case.method))
        my_log.info('expected:{}'.format(case.expected))

        withdraw_data_new = replace(case.data, withdraw_information)
        result = self.request.request(case.method, case.url, withdraw_data_new)

        """
        withdraw_dict = json.loads(case.data)
        if withdraw_dict['mobilephone'] == '**mobilephone**':
            withdraw_dict['mobilephone'] = withdraw_member_phone
        result = self.request.request(case.method, case.url, withdraw_dict)
        """
        try:
            self.assertEqual(json.loads(case.expected)['msg'], json.loads(result.text)['msg'])
            TestResult = "Pass"
        except AssertionError as e:
            TestResult = "Failed"
            my_log.error("断言出错了".format(e))
            raise e
        finally:
            self.write_withdraw.write_excel(case.case_id+1, result.text, TestResult)  # 写入测试实际结果
            my_log.info('提现的结果：{}'.format(json.loads(result.text)['msg']))  # 第一条用例登陆失败，写入的对比结果不对

    @unittest.skip("忽略测试，不要运行")
    @data(*cases_add)
    def test_add(self, case):  # 测试创建标的
        my_log.info("开始执行第{}条用例: {}".format(case.case_id, case.title))
        my_log.info('url:{}'.format(case.url))
        my_log.info('data:{}'.format(case.data))
        my_log.info('method:{}'.format(case.method))
        my_log.info('expected:{}'.format(case.expected))

        # 还有问题 登录后在获取变量执行就会跳过
        # add_dict = json.loads(case.data)
        # if add_dict["memberId"] == "**123456**":
        #     add_dict["memberId"] = withdraw_member_id
        # result = self.request.request(case.method, case.url, add_dict)

        result = self.request.request(case.method, case.url, case.data)
        try:
            self.assertEqual(json.loads(case.expected)['msg'], json.loads(result.text)['msg'])
            TestResult = "Pass"
        except AssertionError as e:
            TestResult = "Failed"
            my_log.error("断言出错了".format(e))
            raise e
        finally:
            self.write_add.write_excel(case.case_id+1, result.text, TestResult)  # 写入测试实际结果
            my_log.info('新建项目的结果：{}'.format(json.loads(result.text)['msg']))

    @unittest.skip("忽略测试，不要运行")
    @data(*cases_audit)
    def test_audit(self, case):  # 测试创建标的
        my_log.info("开始执行第{}条用例: {}".format(case.case_id, case.title))
        my_log.info('url:{}'.format(case.url))
        my_log.info('data:{}'.format(case.data))
        my_log.info('method:{}'.format(case.method))
        my_log.info('expected:{}'.format(case.expected))
        result = self.request.request(case.method, case.url, case.data)
        try:
            self.assertEqual(json.loads(case.expected)['msg'], json.loads(result.text)['msg'])
            TestResult = "Pass"

            if json.loads(case.data)['status'] == 4:  # 如果状态为竞标（4），显示标的
                global id
                id = json.loads(case.data)['id']
                # print('id的值:{}'.format(id))

        except AssertionError as e:
            TestResult = "Failed"
            my_log.error("断言出错了".format(e))
            raise e
        finally:
            self.write_audit.write_excel(case.case_id+1, result.text, TestResult)  # 写入测试实际结果
            my_log.info('审核的结果：{}'.format(json.loads(result.text)['msg']))

    @unittest.skip("忽略测试，不要运行")
    @data(*cases_bidLoan)
    def test_bidLoan(self, case):  # 测试创建标的
        # my_log.info("开始执行第{}条用例: {}".format(case.case_id, case.title))
        # my_log.info('url:{}'.format(case.url))
        # my_log.info('data:{}'.format(case.data))
        # my_log.info('method:{}'.format(case.method))
        # my_log.info('expected:{}'.format(case.expected))

        # 还有问题 登录后在获取变量执行就会跳过
        bidLoan_dict = json.loads(case.data)
        if bidLoan_dict["mobilephone"] == "@123@":
            bidLoan_dict["mobilephone"] = recharge_member_phone
        # if bidLoan_dict["memberId"] == "123":
        #     bidLoan_dict["memberId"] = recharge_member_id
        result = self.request.request(case.method, case.url, bidLoan_dict)

        # result = self.request.request(case.method, case.url, case.data)
        try:
            self.assertEqual(json.loads(case.expected)["msg"], json.loads(result.text)["msg"])
            TestResult = "Pass"
        except AssertionError as e:
            TestResult = "Failed"
            my_log.error("断言出错了".format(e))
            raise e
        finally:
            self.write_bidLoan.write_excel(case.case_id+1, result.text, TestResult)  # 写入测试实际结果
            my_log.info('竞标的结果：{}'.format(json.loads(result.text)["msg"]))


if __name__ == '__main__':  # 会自动的在当前文件里面加载test_文件开头的用例
    unittest.main()