# coding: utf-8
# 当前项目的名称: python13-api-test 
# 新文件名称：setup 
# 当前登录名：LuckyLu
# 创建日期：2019/1/24 10:04
# 文件IDE名称：PyCharm

"""
1，设计配置文件，完成配置文件类的封装，将接口请求URL和数据库信息放到配置文件中进行管理。
2，思考如何实现投资接口？

1》如何实现投资人测试数据的参数化？（类比注册手机号码的实现？）

2》参数化后的投资人，管理员，借款人这些基础数据放到哪里管理？

3》如何在自动化用例中特换这些参数化数据？

4》如何实现投资接口中对于标的ID的依赖？ （温馨提示可以使用global全局变量）

为何recharge执行手机号码为空直接跳过了，显示出错信息：

  File "D:\BaiduNetdiskDownload\python13-api-test\test_cases\test_api_method.py", line 142, in test_recharge
    recharge_dict = json.loads(case.data)
    raise ValueError(errmsg("Expecting value", s, err.value)) from None
ValueError: Expecting value: line 1 column 34 (char 33)


"""




