# coding: utf-8
# python13-api-test 
# context 
# shen 
# 2019/1/26 16:57 

import re
# s 是目标字符串
# d 是替换的内容
# 找到目标字符串里面的标识符KEY，去d字典里面拿到替换的值
# 替换到s里面去，然后在返回

from common.test_api_config import ReadConfig
config = ReadConfig()

class Context:  # 上下文，数据的准备和记录
    admin_user = config.get_value('Data', 'admin_user')
    admin_pwd = config.get_value('Data', 'admin_pwd')

    loan_member_id = config.get_value('Data', 'loan_member_id')  # loan_id 是创建好才有的，所有不需要定义成类属性
    loan_member = config.get_value('Data', 'loan_member')
    loan_member_pwd = config.get_value('Data', 'loan_member_pwd')

    normal_user = config.get_value('Data', 'normal_user')
    normal_pwd = config.get_value('Data', 'normal_pwd')
    normal_member_id = config.get_value('Data', 'normal_member_id')

    recharge_login_mobile_phone = config.get_value('Data', 'recharge_login_mobile_phone')
    recharge_login_mobile_pwd = config.get_value('Data', 'recharge_login_mobile_pwd')
    recharge_mobile_phone = config.get_value('Data', 'recharge_mobile_phone')
    recharge_amount = config.get_value('Data', 'recharge_amount')

    register_member_pwd = config.get_value('Data', 'register_member_pwd')
    register_member_regname = config.get_value('Data', 'register_member_regname')

    audit_loan_id = config.get_value('Data', 'audit_loan_id')

    generateRepayments_loan_id = config.get_value('Data', 'generateRepayments_loan_id')
    generateRepayments_loan_id_repayments = config.get_value('Data', 'generateRepayments_loan_id_repayments')

    def replace(s, d):
        p = "\$\{(.*?)}"  # 有组一定要用()
        while re.search(p, s):
            m = re.search(p, s)
            key = m.group(1)
            value = d[key]
            s = re.sub(p, value, s, count=1)
        return s

    def replace_new(s):
        p = "\$\{(.*?)}"  # 有组一定要用()
        while re.search(p, s):
            m = re.search(p, s)
            key = m.group(1)
            if hasattr(Context, key):
                value = getattr(Context, key)  # 利用反射动态的获取属性
                s = re.sub(p, value, s, count=1)
            else:
                print("没有这个属性值")
                return None  # 或者抛出一个异常，告知没有这个属性
        return s

if __name__ == '__main__':
    # s = '{"mobilephone": "${admin_user}", "pwd": "${admin_pwd}"}'
    # data = {"admin_user": "15873171553", "admin_pwd": "123456"}
    #
    # register_mobile_phone = {"mobilephone": "${register_mobilephone}", "pwd": "${register_pwd}"}
    # register_data = {"mobilephone": "15666666678", "pwd": "123456"}

    # login_mobile_phone = '{"mobilephone": "${login_mobile_phone}", "pwd": "${login_mobile_pwd}"}'
    # login_data = {"login_mobile_phone": "15666666678", "login_mobile_pwd": "123456"}
    # s = replace(login_mobile_phone, login_data)
    # print(s)

    # add_add = '''{"memberId": "${add_memberId}", "title": "${add_title}", "amount": "${add_amount}",
    #            "loanRate": "${add_loanRate}", "loanTerm": "${add_loanTerm}",
    #            "loanDateType": "${add_loanDateType}", "repaymemtWay": "${add_repaymemtWay}",
    #            "biddingDays": "${add_biddingDays}"}'''
    # add = {"add_memberId": "1116833", "add_title": "lucyktest2", "add_amount": "10000", "add_loanRate": "10.0",
    #        "add_loanTerm": "6",
    #        "add_loanDateType": "0", "add_repaymemtWay": "4", "add_biddingDays": "1"}
    # s = replace(add_add, add)
    # print(s)
    s = '{"mobilephone": "${admin_user}", "pwd": "${admin_pwd}"}'
    s = Context.replace_new(s)
    print(s)

    s2 = '{"mobilephone": "${recharge_login_mobile_phone}", "pwd": "${recharge_login_mobile_pwd}", "mobilephone": "${recharge_mobile_phone}", "amount": "${recharge_amount}"}'
    s2 = Context.replace_new(s2)
    print(s2)