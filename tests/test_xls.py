import os
import xlrd
from conftest import RESOURCES_DIR

# TODO оформить в тест, добавить ассерты и использовать универсальный путь

"""Количество листов 1
Имена листов ['Sheet1']
Количество колонок  8
Количество строк    10"""


def test_xls():
    xls_file_path = os.path.join(RESOURCES_DIR, 'file_example_XLS_10.xls')
    book = xlrd.open_workbook(xls_file_path)
    assert book.nsheets == 1, f'Wrong book number of sheets: expected {1}, got {book.nsheets}'
    assert book.sheet_names() == ['Sheet1'], f"Wrong sheet names: expected {['Sheet1']}, got {book.nsheets}"

    sheet = book.sheet_by_index(0)
    rowx = 3
    colx = 2
    cell_value = sheet.cell_value(rowx=rowx, colx=colx)
    exp_col_number = 8
    exp_row_number = 10
    all_sheet_rows_list = []

    for rx in range(sheet.nrows):
        all_sheet_rows_list.append(sheet.row(rx))

    assert sheet.ncols == exp_col_number, f'Wrong columns number: expected {exp_col_number}, got {sheet.ncols}'
    assert sheet.nrows == exp_row_number, f'Wrong rows number: expected {exp_row_number}, got {sheet.nrows}'
    assert cell_value == 'Gent', f'Wrong value in cell {rowx= } {colx= }: expected {"Gent"}, got {cell_value}'
    assert len(all_sheet_rows_list) == exp_row_number, (f'Wrong rows number: '
                                                        f'expected {exp_row_number}, got {len(all_sheet_rows_list)}')
