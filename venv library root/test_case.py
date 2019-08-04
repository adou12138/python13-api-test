# coding: utf-8
# python13-api-test 
# test_case 
# shen 
# 2019/1/15 21:09

"""
cmd 命令行执行，为何test case执行不行，没有显示调用结果，但是执行test report调用test_suite是ok的，是因为参数的关系么？


bug 1：
add 模块 memberid='0' 抛出：
{"status":0,"code":"20102","data":null,
"msg":"nested exception is org.apache.ibatis.exceptions.TooManyResultsException: Expected one result (or null) to be returned by selectOne(), but found: 4243"}
bug 2：
recharge & withdraw使用不同的账号进行操作，第一条用例测试失败，登录 != 充值成功
bug 3:
add 模块 loanTerm=999 抛出：
{"status":0,"code":"20102","data":null,
"msg":"\n### Error updating database.  Cause: com.mysql.jdbc.MysqlDataTruncation: Data truncation: Out of range value for column 'LoanTerm' at row 1\n### The error may involve com.lemon.futureloan.dao.LoanMapper.add-Inline\n### The error occurred while setting parameters\n### SQL: insert into loan   ( memberId      ,title      ,amount      ,loanRate       ,loanTerm      ,loanDateType      ,repaymemtWay      ,biddingDays      ,status   )  values   ( ?      ,?      ,?      ,?      ,?      ,?      ,?      ,biddingDays      ,?   )\n### Cause: com.mysql.jdbc.MysqlDataTruncation: Data truncation: Out of range value for column 'LoanTerm' at row 1\n; SQL []; Data truncation: Out of range value for column 'LoanTerm' at row 1; nested exception is com.mysql.jdbc.MysqlDataTruncation: Data truncation: Out of range value for column 'LoanTerm' at row 1"}
bug 4:
add 模块 loanDateType=-1 抛出：
<html><head><title>Apache Tomcat/6.0.53 - Error report</title><style><!--H1 {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;font-size:22px;} H2 {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;font-size:16px;} H3 {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;font-size:14px;} BODY {font-family:Tahoma,Arial,sans-serif;color:black;background-color:white;} B {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;} P {font-family:Tahoma,Arial,sans-serif;background:white;color:black;font-size:12px;}A {color : black;}A.name {color : black;}HR {color : #525D76;}--></style> </head><body><h1>HTTP Status 501 - Method GOT is not implemented by this servlet for this URI </h1><HR size="1" noshade="noshade"><p><b>type</b> Status report</p><p><b>message</b> <u>Method GOT is not implemented by this servlet for this URI </u></p><p><b>description</b> <u>The server does not support the functionality needed to fulfill this request.</u></p><HR size="1" noshade="noshade"><h3>Apache Tomcat/6.0.53</h3></body></html>
bug 5:
add 模块 repaymemtWay=-1 抛出：
还款方式 repaymemtWay值应该属于[4,5,10,11]
不应该加标成功  {"status":1,"code":"10001","data":null,"msg":"加标成功"}
bug 6:
add 模块 biddingDays=-1 抛出：
还款方式 repaymemtWay值应该属于rangeint(1,10)
不应该加标成功  {"status":1,"code":"10001","data":null,"msg":"加标成功"}
bug 7:
add 模块 biddingDays=0 抛出：
还款方式 repaymemtWay值应该属于rangeint(1,10)
不应该加标成功  {"status":1,"code":"10001","data":null,"msg":"加标成功"}
bug8:
audit 模块 status=10，状态错误
显示："当前接口暂未开放该状态值更新"，应该是 10. 还款完成 项目所有的还款都已完成
bug9:
generateRepayments 模块 状态错误
执行后显示：{"status":1,"code":"20403","data":null,"msg":"不存在该项目，生成回款计划失败"}
需求文档显示code：20404
"""

# 书签 ctrl+f11
"""
try_json.py()["code"] 转成字典取值
testcase分开写接口类，重新设计下


测试有session信息的接口，先按照正常的逻辑走登陆再充值等，然后再走异常流程
识别图片：你先把图片搞出来，用opcv或者halcon字符串识别就可以识别出来字符

A用户能不能给B用户充值？ 应该是不能的
未登录，能不能使用充值？

怎么封装get、post请求
用wb的时候，把resp.txt换成resp.content http响应二进制内容
所有的地址信息：
http://47.107.168.87:8080/futureloan/mvc/api/member/login
自己根据接口文档去更新接口名以及参数即可

数据库的信息二：
接口地址：http://test.lemonban.com/futureloan/mvc/api/member/login
ip:test.lemonban.com
端口：3306
用户名：test
密码：test

数据库的信息一：
接口地址：http://47.107.168.87:8080/futureloan/mvc/api/member/login
ip:47.107.168.87
端口：3306
用户名：python
密码：python666

前台：http://120.78.128.25:8765/
13825161923 lemon123
后台：120.78.128.25:8786/Admin/Index/login.html
lemon7 77q4
接口地址：http://120.78.128.25:8080/futureloan/mvc/api/member/register

webservice:
http://120.24.235.105:9010/finance-user_info-war-1.0//ws/financeUserInfoFacade.ws?wsdl
http:
http://47.107.168.87:8080/futureloan/mvc/api/member/login?mobilephone=&pwd=123456

借款人-->借款
项目(标)
投资人-->投资
投资-->投资记录
资金流水记录
每月付息 到期还本
举例：
加入金额 1000
年化利率 10%
借款期限 3月
还款方式 每月付息
计算收益：总利息？每月的利息是多少？一共多少条回款计划？
1000/12*3

平台核心业务流程：
项目收集-风控审核-运营审核-用户投标-满标放款-到期回款
项目收集：借款人向平台发起借款申请，提交各类资料
风控审核：风控根据借款人的资质，进行审核（线下）
运营审核：审核通过后，项目将在网站和app展示（线上）
用户投标：平台用户充值，通过网站、app进行投资
满标放款：项目满标后，平台打款到借款人账户，更新投资人数据（流标情况）
到期回款：到期正常还款，借款人打款到平台账户，平台更新回款账户  
---使用recharge还款？按照load_id的借款金额还款，打入金额后，平台会自动更新到还款账户？

业务流程：三条主线
借款用户：上标满标、提现还款
投资用户：注册、充值、投资、回款、提现
项目（标的）：审核中、二审、三审、竞标中核保审批（募集资金）、终审还款中、审核不通过流标、还款完成

主要的数据表设计 安装Navicat
数据库地址：120.78.128.25：3306  user：futurevistor pwd：123456
用户：id、用户名、密码、手机号、用户类型、可用余额、注册时间
标：id、用户id、标题、金额、年化收益（年化 18.0%，存储为 18.0）、借款期限（如 6 个月为 6，30 天为 30）（天/月）、
借款日期类型（0- 按月 2- 按天 4-按周）（1/2）、竞标天数（1-10 天）、创建时间、竞标开始时间、状态
--（repaymemtWay）还款方式：4 一次性 5 按月等额本息 10 按月等额本息线下 11 按月付息到期还本（需求文档）

投资记录：id、用户id、标id、状态（有效/无效）、投资金额、创建时间
回款计划：id、投资id、创建时间、回款期次、待还本金、待还利息、还款日期、实际还款日期、状态
流水记录：id、收款用户id、付款用户id、创建时间、交易金额、付款后金额、收入后金额、状态
sql：外键？关联关系？mysql oracle 关系型数据库

8.9.11状态不需要关注
1. 审核中 新建项目，上传资料并保存
2. 二审（初审中） 初审，运营经理
3. 三审（复审中） 初审通过后，运营总监复审
4. 竞标中 发标审核通过，项目发布至平台，用户开始投标
5. 核保审批 担保核查审批，是否接受风险
6. 平台终审 确定项目正常沐子成功，审核通过则生成回款计划，财务出纳放款
7. 还款中 项目募资满、并成功放款、生成回款计划成功
10. 还款完成 项目所有的还款都已完成

8. 审核不通过 各阶段审核不通过状态，募资失败
9. 流标 项目已流标，本次募资无效
11. 申请流标 竞标期限截止而未募满的项目，或其他特殊原因，申请流标状态
"""
""""
SELECT * FROM future.loan where Id='15908';
select * from future.loan where memberid='1117370' order by createTime desc limit 1;
#select * from future.loan where memberid='1117370';
SELECT * FROM future.member WHERE MobilePhone='15999999999';
"""
"""
1.common-test_api_config.py这个文件的异常抛出帮我看下，哪里有问题
    def get_value(self, section, option):
        try:
            return self.config.get(section, option)
        except SyntaxError as e:
            raise OperationalError("Option %s is not found in "
                                   "configuration, error: %s" %
                                   (section, e))

2.测试接口的服务器异常，mock没用，只能通过改服务器的状态么
3.执行test_suite,注册和登录模块，最后只写入了登录模块，report报告都是执行ok的，找不到原因，老师帮忙看下有的数据还是没有写进去
4.在执行withdraw的时候，testcase2，正常登陆，出现警告信息：
C:\Python34\lib\site-packages\pymysql\cursors.py:329: Warning: (1292, "Truncated incorrect DOUBLE value: '${mobilephone}'")
  self._do_get_result()

"""











