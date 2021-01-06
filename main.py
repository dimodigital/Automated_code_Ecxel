import xlsxwriter

workbook = xlsxwriter.Workbook('0.xlsx')
worksheet = workbook.add_worksheet()
# number assign as quantity
number = 18000
j = 0
for i in range(10000, number+1):
    my_list = ("01H34%.5d" %i)
    j = (i - 10000)
    worksheet.write(j, 0, j)
    worksheet.write(j, 1, "LED")
    worksheet.write(j, 2, "7W")
    worksheet.write(j, 3, "6500k")
    worksheet.write(j, 4, "B22")
    worksheet.write(j, 5, 1901)
    worksheet.write(j, 6, my_list)
    print(my_list)

workbook.close()