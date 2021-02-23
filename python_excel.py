import xlrd
import xlwt
from xlutils.copy import copy

class python_excel:
    def __init__(self):
        self.xlsx = xlrd.open_workbook("/Users/dengdeshun/Downloads/批量查询_企业_企查查(49133171).xls")

    def pyexcel(self):
        table = self.xlsx.sheet_by_index(0)
        for i in range(10):
            for j in range(10):
                print(table.cell_value(i,j))

    def create_excel(self):
        new_wb = xlwt.Workbook() #新建工作簿
        ws = new_wb.add_sheet("第一张表") #新建工作表
        for i in range(9):
            for j in range(9):
                if i >= j:
                    cube = f"{j+1}×{i+1}={(i+1)*(j+1)}"
                    ws.write(i, j, cube) #数据写入
        new_wb.save('pyexcel.xlsx') #工作簿保存


if __name__ == '__main__':
    solution = python_excel()
    # solution.pyexcel()
    solution.create_excel()
