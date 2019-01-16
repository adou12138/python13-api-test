# 当前项目的名称: python_13 
# 新文件名称：do_excel 
# 当前登录名：LuckyLu
# 创建日期：2019/1/11 14:52
# 文件IDE名称：PyCharm

from openpyxl import Workbook
from openpyxl import load_workbook

# from week_7.class_unittest_test.test_config import ReadConfig
# test_button = ReadConfig('test_case.conf').get_value('CASE', 'button')
'''
params=datas??
'''


def create_excel(excel_name):  # 创建一个excel
    # 新建一个Excel
    wb = Workbook()  # 新建一个
    wb.save(excel_name)  # 必须要保存 否则不能创建成功

class Cases:
    '这个是一个存储数据的类'
    def __init__(self):  # 存储初始化数据
        self.case_id = None
        self.title = None
        self.a = None
        self.b = None
        self.expected = None

class DoExcel:
    '这是一个excel测试数据的类'
    def __init__(self, excel_name, excel_sheet_name, test_button):  # 定义初始化函数
        self.excel_name = excel_name
        self.excel_sheet_name = excel_sheet_name
        self.test_button = test_button

    def read_excel(self):  # 读取数据
        wb = load_workbook(self.excel_name)  # 定位excel
        sheet = wb[self.excel_sheet_name]  # 定为表单
        # res = sheet.cell(row, col).value  # 定位单元格

        if test_button == 'all':
            case = []
            for i in range(2, sheet.max_row+1):
                row_case = Cases()
                row_case.case_id = sheet.cell(row=i, column=1).value
                row_case.title = sheet.cell(row=i, column=2).value
                row_case.a = sheet.cell(row=i, column=3).value
                row_case.b = sheet.cell(row=i, column=4).value
                row_case.expected = sheet.cell(row=i, column=5).value
                case.append(row_case)
                # print(row_case)
            # print(case)
        else:
            case = []
            for i in eval(test_button):
                row_case = Cases()
                row_case.case_id = sheet.cell(row=i+1, column=1).value
                row_case.title = sheet.cell(row=i+1, column=2).value
                row_case.a = sheet.cell(row=i+1, column=3).value
                row_case.b = sheet.cell(row=i+1, column=4).value
                row_case.expected = sheet.cell(row=i+1, column=5).value
                case.append(row_case)
        return case

    def write_excel(self, row, col,value):  # 写入数据
        wb = load_workbook(self.excel_name)  # 定位excel
        sheet = wb[self.excel_sheet_name]  # 定为表单

        sheet.cell(row, col).value = value  # 写入数据
        wb.save(self.excel_name)  # 保存数据


# sheet.cell(row=3,column=4,value=9)#写入值的方法一
# # sheet.cell(row=3,column=5).value='7777'#写入值的方法二
# # wb.save('Python3.xlsx')



#3. 定位单元格--取值
# res=sheet.cell(row=3,column=4).value
# print('获取到的值是：{}'.format(res))
# print('------')
# for i in range(1,sheet.max_column+1):
#     for j in range(1,sheet.max_row+1):
#         res=sheet.cell(row=i,column=j).value
#         print('获取到的值是：{}'.format(res))
#         # print('获取到的值的类型是：{}'.format(type(res)))
# print('------')

#4. 定位单元格 写值 一定要关闭excel才能写!
# sheet.cell(row=3,column=4,value=9)#写入值的方法一
# # sheet.cell(row=3,column=5).value='7777'#写入值的方法二
# # wb.save('Python3.xlsx')
# print('获取到的值是：{}'.format(res))
# print('获取到的值的类型是：{}'.format(type(res)))
#print('------)

#字符串--str
# res=eval(sheet.cell(row=1,column=2).value)
# print('获取到的值是：{}'.format(res))
# print('获取到的值的类型是：{}'.format(type(res)))
# print('------')
#列表--字符串 如果想变成原始的类型 就利用eval函数 进行转换
# res=sheet.cell(row=1,column=2).value
# print('获取到的值是：{}'.format(res))
# print('获取到的值的类型是：{}'.format(type(res)))
# print('------')
#字典--字符串
# res=sheet.cell(row=1,column=4).value
# print('获取到的值是：{}'.format(res))
# print('获取到的值的类型是：{}'.format(type(res)))
# print('------')
#float--floast
# res=sheet.cell(row=2,column=4).value
# print('获取到的值是：{}'.format(res))
# print('获取到的值的类型是：{}'.format(type(res)))
# print('------')
#int--int
# res=sheet.cell(row=3,column=5).value
# print('获取到的值是：{}'.format(res))
# print('获取到的值的类型是：{}'.format(type(res)))
# print('------')

#5. 获取最大行数和最大列数
# print('行',sheet.max_row)
# print('列',sheet.max_column)
# print('获取到的值是：{}'.format(res))
# print('获取到的值的类型是：{}'.format(type(res)))

if __name__ == '__main__':
    # create_excel('luckytest.xlsx')
    cases = DoExcel('luckytest.xlsx', 'add', test_button).read_excel()
    print(cases)
    # write = DoExcel('luckytest.xlsx', 'sub').write_excel(2, 6, 'pass')
    # print(write)