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


def replace(s, d):
    p = "\$\{(.*?)}"  # 有组一定要用()
    while re.search(p, s):
        m = re.search(p, s)
        key = m.group(1)
        value = d[key]
        s = re.sub(p, value, s, count=1)
    return s

if __name__ == '__main__':
    # s = '{"mobilephone": "${admin_user}", "pwd": "${admin_pwd}"}'
    # data = {"admin_user": "15873171553", "admin_pwd": "123456"}
    #
    # register_mobile_phone = {"mobilephone": "${register_mobilephone}", "pwd": "${register_pwd}"}
    # register_data = {"mobilephone": "15666666678", "pwd": "123456"}

    login_mobile_phone = '{"mobilephone": "${login_mobile_phone}", "pwd": "${login_mobile_pwd}"}'
    login_data = {"login_mobile_phone": "15666666678", "login_mobile_pwd": "123456"}

    s = replace(login_mobile_phone, login_data)
    print(s)