# coding: utf-8
# python13-api-test 
# test_payment 
# shen 
# 2019/2/18 23:00 

"""
支付测试类：
1. 正确的用户信息，支付成功
2. 正确的用户信息，支付失败
3. 超时，超时再成功
4. 超时，超时再失败
"""

import unittest
from mockdemo import payment
from unittest import mock

class PaymentTest(unittest.TestCase):
    '这个是测试支付的类'
    def setUp(self):
        self.payment = payment.Payment()

    def test_success(self):
        self.payment.requestQutoSystem = mock.Mock(return_value=200)
        resp = self.payment.doPay(user_id=1, card_num='1234567', amount=100)
        self.assertEqual('success', resp)

    def test_fail(self):
        self.payment.requestQutoSystem = mock.Mock(return_value=500)
        resp = self.payment.doPay(user_id=2, card_num='1234567', amount=10.01)
        self.assertEqual('fail', resp)

    def test_retry_success(self):
        self.payment.requestQutoSystem = mock.Mock(side_effect=[TimeoutError, 200])
        resp = self.payment.doPay(user_id=2, card_num='1234567', amount=10.01)
        print(resp)
        self.assertEqual('success', resp)
        # self.payment.requestQutoSystem.assert_called()
        self.payment.requestQutoSystem.assert_called_with(user_id=3, card_num='1234567')

    def test_retry_fail(self):
        self.payment.requestQutoSystem = mock.Mock(side_effect=[TimeoutError, 500])
        resp = self.payment.doPay(user_id=2, card_num='1234567', amount=100)
        print(resp)
        self.assertEqual('fail', resp)
        print('requestQutoSystem被调用两次：', self.payment.requestQutoSystem.call_count)



