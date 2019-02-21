# -*- coding: UTF-8 -*-
# 当前项目的名称: python13-api-test 
# 新文件名称：review 
# 当前登录名：LuckyLu
# 创建日期：2019/2/21 13:41
# 文件IDE名称：PyCharm
"""
自动化测试框架梳理
一、框架的意义 可读性，可维护性，可扩展性
1. 数据与代码分离 （数据驱动）
2. 结构分层（数据层，用例层，逻辑层）

好处：
二、1. 手工测试用例与自动用例完美结合，避免重复工作
2. 配置灵活，根据需要快速切换测试环境
3. 常用功能封装，逻辑清晰，易于维护
4. 统一执行入口，管理测试用例集
5. 持续集成，定时构建，快速反馈

11.21 怎么设计数据框架的
json:字符串用loads，文件用load
接口项目请求：response cookies
request cookies
其他项目：response tokenID
request headers tokeni
逻辑层都在common里面，都是常量的封装

三、使用到技术/框架
1. 语言 Python
2. 测试框架 unittest ---pytest
3. 接口调用 request ---
4. 数据驱动 ddt
5. 数据管理 openpyxl
6. 数据库交互 pymysql ---根据数据库选择对应的第三方模块来完成
7. 数据格式的转换 json
8. 日志处理 logging --- 清晰的执行过程，快速定位问题
9. 持续集成 jenkins

python 弱语法，不需要编译，面向对象
unittest 用xml直接换成xml类？ 56.10
unittest：testcases testsuite testloaders mock？
urlib 也可以完成http请求
openpyxl可以完成读写
pymysql 因为用的数据库是mysql
数据格式转化：json/eval
区别：json针对json格式字符串，eval针对python数据的
eval 不能识别非python数据
json是跨语言的
持续集成的好处：可视化 快速构建 部署 定时 自动执行
避免人工操作出错
快速部署

简历的编写&投递
一、如何编写进阿里
1. 技能长项写在建立最重要的位置
2. 项目是王道

二、如何投递简历
1. 投递时间 8
2. 投递网站 拉钩 51 猎聘
3. 简历设置在职不可见，其他均可见

三、面试准备
1. 框架一定要熟悉，简历上罗列的知识点一定要熟记于心
2. 面试题、笔试题、app有定时更新
3. 找丹丹老师拉入vip工作群


"""


