from xlrd import open_workbook
from xlwt import Workbook()
workingfile = "i:/test12.xlsx"
wb = open_workbook(workingfile)
sheet = wb.sheet_by_index(0)
sheet.ncols
sheet.nrows
sheeet.cell(0,0)
sheet.ncols
print workingfile
