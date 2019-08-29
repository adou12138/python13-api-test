# coding: utf-8
# python13-api-test 
# jenkins 
# shen 
# 2019/2/16 12:21

"""
自动代码更新：代码直接放到git上面，设置成每次更新就执行一次

忘记账户密码，jenkins在安装目录中可以直接修改jenkins.xml配置文件：httpPort=8080 修改端口号
config.xml 删除  <authorizationStrategy class="hudson.security.ProjectMatrixAuthorizationStrategy">
    <permission>hudson.model.Hudson.Administer:lucky</permission>
  </authorizationStrategy>

General-参数化构建（使用grovvny语言），尝试下

查看远程git代码，设置拉去时间执行方式
全局工具配置：git
Name：git
Path to Git executable：D:\Program Files\Git\bin\git.exe

job构建信息：workspace job真正执行的信息

构建触发器-GitHub hook trigger for GITScm polling 触发器执行，提交代码后执行

构建环境-对workspace操作的内容

设置本地代码拉取和服务器代码拉取是不一样的
服务器代码拉取(如果代码已经在github上面拉下来，就可以用windows批处理直接执行了)，直接使用执行windows批处理命令，不需要在安装python插件执行
python run_test.py
D:\Python34\python.exe run_test.py 如果安装了多个python，就输入绝对路径添加进去
本地代码，需要安装python插件，还要配置环境变量
@echo off
D:
cd D:\python13-api-test\reports
python test_api_method_suite.py

使用HTML报告和发送邮件，需要安装第三方插件
Publish Over SSH
SSH plugin
Subversion Plug-in
msbuild
HTML Publisher plugin 测试报告设置
Email Extension Plugin email配置
Git

Post-build Actions配置
HTML directory to archive：reports  workspace的相对路径
Index page[s]：reports.html （reports同文件里面report名称）
Report title：Python13-API-Test_Report
最后生成：Jenkins\Jobs\Python13-API\htmlreports\Python13-API-Test_Report

Editable Email Notification
1. 先设置全局属性-邮箱地址
Extended E-mail Notification
SMTP server: smtp.126.com
Default user E-mail suffix: 空
勾选advance选项，出现高级设置
Use SMTP Authentication：勾选
User Name：和系统邮箱保持一致,发件人
Password：使用邮箱smtp服务开启后的密码（qq邮箱需要打开SMTP和IMAP服务）
Use SSL：勾选（126不需要勾选！！！）
SMTP port: 25
Charset: UTF-8

发件人邮件地址和默认的系统邮箱地址一致
发件人邮箱需要设置smtp服务器，如果没有会出现415认证错误
发件人邮件地址和收件人邮件地址不一样
2. Project From 默认设置为空（系统发件人）
3. Content Type-Both HTML and Plain Text
4. Attachments 上传HTML附件 reports/reports.html
5. Project Recipient List
收件人邮件地址用英文状态的逗号隔开

邮件附件中的html文件需要下载看才显示正常，不然会缺少样式

tomcat里面放了两个war包 要是改了端口号 那我另外的war能正常执行吗? server.xml可以配置服务
如果没有配置git/SVN,可以先把代码拷贝到workspace里面

jenkins工作空间的路径直接在workspace里面看
查看相关日志文件查看报错信息E:\Program Files (x86)\Jenkins\logs\tasks

设计定时执行： H代表任意合理的数 H/10 * * * * 每隔10分钟

Jenkins的国内升级镜像源
系统管理-管理插件-高级
将升级站点更改为：
https://mirrors.tuna.tsinghua.edu.cn/jenkins/updates/current/update-center.json

更改语言，安装插件之后
系统设置-locale-language

pip install -i https://pypi.douban.com/simple pymysql
python test_run.py

http报告丢失css样式：
https://testerhome.com/topics/9476
在系统管理-脚本命令行执行下面的语句：
System.setProperty("hudson.model.DirectoryBrowserSupport.CSP", "")


定时执行：
-每15分钟构建一次：H代表形参
    - H/15 ****
-每隔5分钟构建一次：
    - H/5 ****
-在每个小时的前半个小时内的每15分钟：
    - H(0-29)/15 ****
-每3个小时构建一次：
    - H H/3 ***
-每天中午12点定时构建一次：
    - H 12 ***
-每天的3点，8点，12点，一天构建3次：(多个时间点中间用逗号隔开)
    - 0 3，8，12 ***
-每天早上7点到晚上7点每2小时构建一次：
    - H 7-19/2 ***
-周一到周五，从上午9：45开始，每天下午3：45结束，每两小时构建一次：
    - 45 9-16/2 ** 1-5
-周一到周五，上午9点到下午4点，每两小时构建一次：
    - H H(9-16)/2 ** 1-5
"""



