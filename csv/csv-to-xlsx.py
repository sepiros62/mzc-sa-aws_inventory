import os
import csv
import sys

from openpyxl import Workbook

reload(sys)
sys.setdefaultencoding('utf8')

if __name__ == '__main__':
    workbook = Workbook()
    worksheet = workbook.active
    with open('ec2-template.csv', 'r') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                for idx, val in enumerate(col.split(',')):
                    cell = worksheet.cell(row=r+1, column=c+1)
                    cell.value = val
    workbook.save('ec2-template.xlsx')
