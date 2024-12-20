from os import listdir
from os.path import isfile, join
from openpyxl import load_workbook
import xlwings as xw

import globalvars

class get_data():
    def __init__(self, count, fieldnotes_dict):

        # import global variables
        globalvars.init()

        # set the main path for the Field Notes folder
        main_path = f'{globalvars.main_path}/{globalvars.bridgeID[count]}/Field Notes'
        # get the excel file name
        files = self.get_all_folder_files(main_path)
        # set file path of the field notes
        file_path = f'{main_path}/{files}'

        # load workbook
        field_notes = xw.Book(file_path, read_only=True)
        # get field notes data from the main sheet
        main_sheet = field_notes.sheets['Info, NBI, Work']
        # set 2 empty variables
        row = 0
        column = 0
        # loop over the entire keys of the dictionary
        for keys in fieldnotes_dict:
            # skip the Elements key
            if keys == 'Elements':
                continue
            # update the Work Items:
            if keys == 'Work Items':
                # loop over all Work Items information
                for keys_wi, i in enumerate(fieldnotes_dict[keys]):
                    # set the initial position to the first description
                    row, column = [57, 1 + i]
                    while True:
                        value = main_sheet.cells(row, column).value
                        if value == '' or value == None:
                            break
                        
                        fieldnotes_dict[keys][keys_wi].append(value)
                        row += 1
                continue
            # get the rows and columns for the desired cell
            row, column = fieldnotes_dict[keys][0]
            # update the dictionary with the Excel cell value
            fieldnotes_dict[keys][1] = main_sheet.cells(row, column).value

        # get all elements
        elements = [num for num in field_notes.sheet_names if num.isnumeric()]
        self.get_element_codition(field_notes, fieldnotes_dict, elements)
        print(fieldnotes_dict)


    def get_all_folder_files(self, main_path):
        # get all files
        files = [f for f in listdir(main_path) if isfile(join(main_path, f)) and 'Field Notes' in f][0]
        return files
    

    def get_element_codition(self, field_notes, dict_database, elements):

        row, column = 5, 4
        
        for element in elements:
            element_sheet = field_notes.sheets[element]
            # Initialize the main dictionary for this element if it doesn't exist
            element_dict = dict_database.setdefault(element, {})
            element_dict['Total Quantity'] = element_sheet.cells(row, column).value
            element_dict['CS2'] = element_sheet.cells(row, column + 3).value
            element_dict['CS3'] = element_sheet.cells(row, column + 4).value
            element_dict['CS4'] = element_sheet.cells(row, column + 5).value
            element_dict['Element Notes'] = element_sheet.cells(row + 12, column + 19).value

            # Initialize an empty list for defect types
            element_dict.setdefault('Defect Type', [])

            for i in range(9):
                if element_sheet.cells(row + 1 + i, column).value == 0:
                    continue

                # Extract defect details
                defect_code = element_sheet.cells(row + 1 + i, column - 2).value
                defect_name = element_sheet.cells(row + 1 + i, column - 1).value
                defect_quantity = element_sheet.cells(row + 1 + i, column).value
                defect_cs2 = element_sheet.cells(row + 1 + i, column + 3).value
                defect_cs3 = element_sheet.cells(row + 1 + i, column + 4).value
                defect_cs4 = element_sheet.cells(row + 1 + i, column + 5).value

                # Add defect information as a dictionary in the 'Defect Type' list
                defect_dict = {
                    'Defect Code': defect_code,
                    'Defect Name': defect_name,
                    'Total Quantity': defect_quantity,
                    'CS2': defect_cs2,
                    'CS3': defect_cs3,
                    'CS4': defect_cs4,
                    'Defect Notes': 'See parent element for details.'
                }
                
                element_dict['Defect Type'].append(defect_dict)

            if element_sheet.cells(row, column + 12).value == 0 or element_sheet.cells(row, column + 12).value == '0':
                continue

            child_element_id = element_sheet.cells(row - 3, column + 9).value
            child_element_dict = element_dict.setdefault('Child Element', {}).setdefault(child_element_id, {})
            # Assign values to child element similarly to the parent element
            child_element_dict['Total Quantity'] = element_sheet.cells(row, column + 12).value
            child_element_dict['CS2'] = element_sheet.cells(row, column + 15).value
            child_element_dict['CS3'] = element_sheet.cells(row, column + 16).value
            child_element_dict['CS4'] = element_sheet.cells(row, column + 17).value
            child_element_dict['Child Notes'] = 'See parent element for details.'
            child_element_dict.setdefault('Child Defect Type', []).append(defect_dict)  # Add defects similarly to parent


            for i in range(5):
                if element_sheet.cells(row + 1 + i, column).value == 0:
                    continue

                # Extract defect details
                child_defect_code = element_sheet.cells(row + 1 + i, column + 10).value
                child_defect_name = element_sheet.cells(row + 1 + i, column + 11).value
                child_defect_quantity = element_sheet.cells(row + 1 + i, column + 12).value
                child_defect_cs2 = element_sheet.cells(row + 1 + i, column + 15).value
                child_defect_cs3 = element_sheet.cells(row + 1 + i, column + 16).value
                child_defect_cs4 = element_sheet.cells(row + 1 + i, column + 17).value

                # Add defect information as a dictionary in the 'Defect Type' list
                child_defect_dict = {
                    'Defect Code': defect_code,
                    'Defect Name': defect_name,
                    'Total Quantity': defect_quantity,
                    'CS2': defect_cs2,
                    'CS3': defect_cs3,
                    'CS4': defect_cs4,
                    'Child Defect Notes': 'See parent element for details.'
                }

                element_dict['Child Defect Type'].append(child_defect_dict)