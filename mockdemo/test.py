# -*- coding: UTF-8 -*-
# 当前项目的名称: python13-api-test 
# 新文件名称：test 
# 当前登录名：LuckyLu
# 创建日期：2019/2/19 14:13
# 文件IDE名称：PyCharm 

from unittest import mock
import  os

class Remove(object):

    def rmdir(self,path='c:/Windows'):
        r=os.rmdir(path)
        if r==None :
            return u'删除成功'
        else:
            return u'Sorry，删除失败'

    def exists_get_rmdir(self):
        return self.rmdir()

class Remove(object):

    def rmdir(self,path='c:/log'):
        r=os.rmdir(path)
        if r==None :
            return 'success'
        else:
            return 'fail'

    def exists_get_rmdir(self):
        return self.rmdir()


class MockTest(unittest.TestCase):
    def setUp(self):
        self.r=Remove()


    def tearDown(self):
        pass

    def test_success_rmdir(self):
        '''
        删除目录成功
        :return:
        '''
        success_path=mock.Mock(return_value='success')
        self.r.rmdir=success_path
        self.assertEqual(self.r.exists_get_rmdir(),'success')

    def test_fail_rmdir(self):
        '''
        删除目录失败
        :return:
        '''
        fail_path=mock.Mock(return_value='fail')
        self.r.rmdir=fail_path
        self.assertEqual(self.r.exists_get_rmdir(),'fail')

if __name__=='__main__':
    unittest.main(verbosity=2)