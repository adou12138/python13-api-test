# coding: utf-8
# python13-api-test 
# case_info 
# shen 
# 2019/1/23 22:19 

"""
# '投资人'={'mobilephone':15666666678, 'id':1115697}
# '借款人'={'mobilephone':15777777777, 'id':1114425}
# '审核人'
11579 loanDateType 0
11580 loanDateType 2
11581 loanDateType 4

# 借款人自己给自己申请的标的投资

register=mysql_config
login={"mobilephone": "15666666666", "pwd": "123456"}
recharge={"mobilephone": "15666666678", "pwd": "123456"} '投资人'
withdraw={"mobilephone": "15666666668", "amount": 123} '借款人'
add={"memberId": 1114425, "title": "lucyktest1", "amount": 10000, "loanRate": 10.0, "loanTerm": 6,
        "loanDateType": 0, "repaymemtWay": 4, "biddingDays": 1}
audit= {"id": 11587,  "status": 1} data = {"id": 11580,  "status": 1}

bidLoan=

"""


