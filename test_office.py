from openpyxl import Workbook
from datetime import datetime


def main():
    wb = Workbook()
    ws = wb.active

    ws.append([1, 2, 3])

    ws['A2'] = datetime.now()
    wb.save('test_office.xlsx')

if __name__ == '__main__':
    main()
