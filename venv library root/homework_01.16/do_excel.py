# 当前项目的名称: python_13 
# 新文件名称：do_excel 
# 当前登录名：LuckyLu
# 创建日期：2019/1/11 14:52
# 文件IDE名称：PyCharm

from openpyxl import Workbook
from openpyxl import load_workbook



def create_excel(excel_name):  # 创建一个excel
    # 新建一个Excel
    wb = Workbook()  # 新建一个
    wb.save(excel_name)  # 必须要保存 否则不能创建成功

class Cases:
    '这个是一个存储数据的类'
    def __init__(self):  # 存储初始化数据
        self.case_id = None
        self.title = None
        self.url = None
        self.data = None
        self.method = None
        self.expected = None

class DoExcel:
    '这是一个excel测试数据的类'
    def __init__(self, excel_name, excel_sheet_name):  #, test_button):  # 定义初始化函数
        self.excel_name = excel_name
        self.excel_sheet_name = excel_sheet_name
        # self.test_button = test_button

    def read_excel(self):  # 读取数据
        wb = load_workbook(self.excel_name)  # 定位excel
        sheet = wb[self.excel_sheet_name]  # 定为表单
        # res = sheet.cell(row, col).value  # 定位单元格

        # case = []
        # for i in range(2, sheet.max_row + 1):
        #     row_case = Cases()
        #     row_case.case_id = sheet.cell(row=i, column=1).value
        #     row_case.title = sheet.cell(row=i, column=2).value
        #     row_case.url = sheet.cell(row=i, column=3).value
        #     row_case.data = sheet.cell(row=i, column=4).value
        #     row_case.method = sheet.cell(row=i, column=5).value
        #     row_case.expected = sheet.cell(row=i, column=6).value
        #     case.append(row_case)
        # return case

        case = []  # 所有的数据都存在这个大列表里面 适用于方法一和方法二
        # 方法二：每一行数据存在一个字典里面
        for i in range(2, sheet.max_row + 1):  # 行的范围从第二行开始
            row_data = {}  # 每一行数据存在这个子列表里面
            row_data['case_id'] = sheet.cell(row=i, column=1).value  # 存的是case_id
            row_data['title'] = sheet.cell(row=i, column=2).value  # 存的是title
            row_data['url'] = sheet.cell(row=i, column=3).value  # 存的是url
            row_data['data'] = sheet.cell(row=i, column=4).value  # 存的是data
            row_data['method'] = sheet.cell(row=i, column=5).value  # 存的是method
            row_data['expected'] = sheet.cell(row=i, column=6).value  # 存的是expected
            case.append(row_data)  # 读取完毕之后 把每一行的值存到这个test_data大列表里面去
        return case

        # if test_button == 'all':
        #     case = []
        #     for i in range(2, sheet.max_row+1):
        #         row_case = Cases()
        #         row_case.case_id = sheet.cell(row=i, column=1).value
        #         row_case.title = sheet.cell(row=i, column=2).value
        #         row_case.a = sheet.cell(row=i, column=3).value
        #         row_case.b = sheet.cell(row=i, column=4).value
        #         row_case.expected = sheet.cell(row=i, column=5).value
        #         case.append(row_case)
        #         # print(row_case)
        #     # print(case)
        # else:
        #     case = []
        #     for i in eval(test_button):
        #         row_case = Cases()
        #         row_case.case_id = sheet.cell(row=i+1, column=1).value
        #         row_case.title = sheet.cell(row=i+1, column=2).value
        #         row_case.a = sheet.cell(row=i+1, column=3).value
        #         row_case.b = sheet.cell(row=i+1, column=4).value
        #         row_case.expected = sheet.cell(row=i+1, column=5).value
        #         case.append(row_case)
        # return case

    def write_excel(self, row, col, value):  # 写入数据
        wb = load_workbook(self.excel_name)  # 定位excel
        sheet = wb[self.excel_sheet_name]  # 定为表单

        sheet.cell(row, col).value = value  # 写入数据
        wb.save(self.excel_name)  # 保存数据


if __name__ == '__main__':
    # create_excel('luckytest.xlsx')
    cases = DoExcel('../datas/luckytest.xlsx', 'login').read_excel()
    print(cases)
    print(type(cases))
    # write = DoExcel('../datas/luckytest.xlsx', 'login').write_excel(2, 8, 'pass')
    # print(write)

