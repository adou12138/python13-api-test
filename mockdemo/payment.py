# coding: utf-8
# python13-api-test 
# payment 
# shen 
# 2019/2/18 22:43 

import requests

class Payment:
    '这个是一个支付类'

    def requestQutoSystem(self, card_num, amount):
        """
        请求第三方外部接口，并返回响应码
        :param card_num:
        :param amount:
        :return: 返回状态码，200 代表支付成功， 500 代表支付异常失败
        """
        url = "http://third.payment.pay"  # 第三方支付接口请求地址
        data = {"card_num": card_num, "amount": amount}  # 请求参数
        response = requests.post(url, data=data)
        return response.status_code  # 返回状态码

    def doPay(self, user_id, card_num, amount):
        """
        支付
        :param user_id: 用户ID
        :param card_num: 卡号
        :param amount: 支付金额
        :return:
        """
        try:
            # 调用第三方支付接口请求进行真实扣款
            resp = self.requestQutoSystem(card_num, amount)
        except TimeoutError:
            # 如果超时就重新调用一次
            resp = self.requestQutoSystem(card_num, amount)

        if resp == 200:  # 返回第三方支付成功，则进行系统里面的扣款并记录支付记录
            print("{0}支付{1}成功!!!进行扣款并记录支付记录".format(user_id, amount))
            return 'success'

        elif resp == 500:  # 返回第三方支付失败，则不进行扣款
            print("{0}支付{1}失败!!不进行扣款".format(user_id, amount))
            return 'fail'

if __name__ == '__main__':
    import json
    from unittest import mock
    a = '{"status":1,"code":"10001","data":null,"msg":"登录成功"}'
    b = 1
    if b:
        json.loads(a)['code'] = mock.Mock(return_value=20102)
        print(json.loads(a)['code'])
    else:
        print(b)