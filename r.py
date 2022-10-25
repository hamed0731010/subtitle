import xlsxwriter
workbook   = xlsxwriter.Workbook('filename.xlsx')
worksheet1 = workbook.add_worksheet()
worksheet1.write('A1', 123)

workbook.close()