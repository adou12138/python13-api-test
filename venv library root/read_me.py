# python13-api-test
# read_me 
# shen 
# 2019/1/14 22:02 

# 在当前项目中导出配置文件
# pip freeze>requirements.txt

# 1) 先复制到新项目中
# 2) cmd命名中进入新项目的路径,执行命令 pip install -r requirements.txt

# 接口项目测试安排
# stage1
# 1.14 requests模块讲解与应用
# 1.16 需求分析与用例设置 数据库管理与数据驱动
# 1.18 数据获取和解析，json和dict
# 1.19 结合单元测试和ddt

# stage2
# 1.21 优化创造环境数据
# 1.23 多种断言和正则的使用
# 1.25 关联用例处理
# 1.26 数据库校验

# stage3
# 1.28 日志处理与报告生成
# 1.30 jenkins持续集成
# 2.13 第一阶段复习总结

# 项目接口地址：
# http://47.107.168.87:8080/futureloan/mvc/api/member/login

# 项目需求分析
# https://pan.baidu.com/s/1dTLgME-KWN5lrVd7BVVV6g

# 登录的请求是部署在服务器上的一个服务？api？

"""
20190121
1. pymysql的详解与应用
2. 参数化注册手机号

20190123
1. 如何进一步来优化环境数据？
配置化---配置文件的设计

20190126
用例依赖如何解决？
1. re模块的使用，使用正则查找并替换参数化数据

20190128
》》》 如果解决多个module，或者不同测试类之间的数据传递？
》》》 同一个类或者module里面，不同方法之间的数据传递？ A a B a -> self/global 同一个生命周期里面
1. 如何利用python反射来解决不同测试方法之间数据的传递？




"""

