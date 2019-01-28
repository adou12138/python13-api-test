# coding: utf-8
# python13-api-test 
# test_invest 
# shen 
# 2019/1/28 23:13 

import unittest
from common import contants
from ddt import ddt, data

from common.do_excel import DoExcel  # 导入excel
from common.request import Request  # 导入api请求

# 重新使用doexcel_study中的方法调用
cases_register = DoExcel(contants.excel_file, "register").read_excel()
cases_login = DoExcel(contants.excel_file, "login").read_excel()

from common.mysql import MysqlUtil
import json

from common.context import Context



"""

"""
from log.test_api_log import MyLog
my_log = MyLog()


@ddt
class TestInvest(unittest.TestCase):
    '这是测试接口的类'

    #do_excel = DoExcel(contans.case_file)  # 传入excel
    cases_invest = DoExcel(contants.excel_file, "invest").read_excel()

    @classmethod  # 为什么用类方法？ 整个类只执行一次！
    def setUpClass(cls):  # 每个测试类里面去运行的操作都放到类方法里面
        print("\m这是一个类方法")
        cls.request = Request()  # 实例化对象
        cls.mysql = MysqlUtil

    def setUp(self):  # 每个测试方法里面去运行的操作都放到类方法里面
        print("这是一个setUp")
        self.write_register = DoExcel(contants.excel_file, "register") # 创建一个对象写入
        self.write_login = DoExcel(contants.excel_file, "login")
        my_log.info("开始执行用例")

    def tearDown(self):
        my_log.info("用例执行结束")

    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()  # 关闭session请求
        cls.mysql.close()  # 关闭数据库连接

    @data(*cases_invest)
    def test_invest(self, case):  # 测试注册
        # my_log.info("开始执行第{}条用例: {}".format(case.case_id, case.title))
        # # my_log.info('url:{}'.format(case.url))
        # # my_log.info('data:{}'.format(case.data))
        # # my_log.info('method:{}'.format(case.method))
        # # my_log.info('expected:{}'.format(case.expected))
        # data_dict = json.loads(case.data)
        # if data_dict['mobilephone'] == '#@mobilephone':
        #     data_dict['mobilephone'] == int(self.max)+1
        # result = self.request.request(case.method, case.url, data_dict)
        # try:
        #     self.assertEqual(case.expected, result.text)
        #     TestResult = "Pass"
        # except AssertionError as e:
        #     TestResult = "Failed"
        #     my_log.error("断言出错了".format(e))
        #     raise e
        # finally:
        #     self.write_register.write_excel(case.case_id+1, result.text, TestResult)  # 写入测试实际结果
        #     my_log.info('注册的结果：{}'.format(result.status_code))


        print("开始执行第{}条用例: {}".format(case.case_id, case.title))
        # 查找参数化的测试数据，动态替换
        data_new = Context.replace_new(case.data)  # Str测试数据
        # 使用封装好的request 来完成请求
        resp = self.request.request(case.method, case.url, data_new)
        try:
            self.assertEqual(case.expected, resp.json()['code'], "invest error")
            # 一致就写入Excel的结果为PASS，并且
            self.do_excel.write_excel('invest', case.case_id+1, resp.text, "Pass")  # 写入测试实际结果
            print('第{}条用例执行结果：PASS'.format(case.id))
            # 判断是否加标成功，如果成功就按照借款人ID去数据库查询最新的加标的记录
            if resp.json()['msg'] == '加标成功':
                loan_member_id = getattr(Context, 'loan_member_id')
                sql = "select id from future.loan where memberid='{0}' " \
                      "order by createTime desc limic 1".format(loan_member_id)
                loan_id = self.mysql.fetch_one(sql)[0]
                # 记得转成字符串，后续要通过正则替换
                setattr(Context, 'loan_id', str(loan_id))  # 和excel中的名字保持一致

        except AssertionError as e:
            self.do_excel.write_excel('invest', case.case_id+1, resp.text, "Failed")  # 写入测试实际结果
            print('第{}条用例执行结果：FAIL'.format(case.id))
            print("断言出错了".format(e))
            raise e

if __name__ == '__main__':
    pass
