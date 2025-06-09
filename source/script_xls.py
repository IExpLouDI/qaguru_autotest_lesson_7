from xlrd import open_workbook
from utils.paths import DIR_WITH_RESOURCES
import os


class FileInfoXls:
    def __init__(self, _object):
        self.book = _object
        self.sheet = self.book.sheet_by_index(0)


    def get_page_count(self):
        return self.book.nsheets


    def get_page_names(self):
        return self.book.sheet_names()


    def get_row_value(self):
        return self.sheet.cell_value(rowx=9, colx=1)


    def get_column_count(self):
        return self.sheet.ncols


    def get_row_count(self):
        return self.sheet.nrows

    def get_file_info(self):
        return {
                "page_count": self.get_page_count(),
                "sheet_list": self.get_page_names(),
                "column_count": self.get_column_count(),
                "row_count": self.get_row_count(),
                "value_9_1": self.get_row_value()
            }


if __name__ == "main":
    book = open_workbook(os.path.join(DIR_WITH_RESOURCES,"file_example_XLS_10.xls"))
    print(book.nsheets) # печать количества страниц

    print(book.sheet_names()) # печать названия страницы

    sheet = book.sheet_by_index(0) # вызвать лист по индексу

    print(f'Количество столбцов {sheet.ncols}') # печать с листа количество столбцов

    print(f'Количество строк {sheet.nrows}') # печать с листа количество строк

    print(f'Ячейка 9:1 = {sheet.cell_value(rowx=9, colx=1)}') # печать содержимого ячейки
    sheet.row(0)
    for rx in range(sheet.nrows): # печать содержимого всех ячеек
        print(sheet.row(rx))
