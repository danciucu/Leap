import os
import openpyxl
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import quote_sheetname
from openpyxl.styles import PatternFill
from openpyxl.formatting.rule import FormulaRule

import globalvars

class field_notes():
    def __init__(self) -> None:
        pass

    def import_notes(self, dictionary):
        # define workbook path
        wb_dir = globalvars.root_path + '/' + dictionary['Structure ID'] + '/Field Notes'
        return