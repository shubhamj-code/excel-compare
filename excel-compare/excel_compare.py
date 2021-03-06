from pathlib import Path
import pandas as pd
import openpyxl


class CompareFiles(object):
    def __init__(self, file_one_path: str, file_two_path: str):
        self.file_one_path: str = file_one_path
        self.file_two_path: str = file_two_path
        self.__validate__()

    def __validate__(self):
        """
        Validates whether the file exists or not
        """

        file_one = Path(self.file_one_path)
        file_two = Path(self.file_two_path)
        if not file_one.is_file() or not file_two.is_file():
            print('No file found, exiting.')
            exit(-1)

    def compare_csv(self):
        file_one = pd.read_csv(self.file_one_path)
        file_two = pd.read_csv(self.file_two_path)
        concat_pd = self.__concat_drop_dataframes__(file_one, file_two)
        if concat_pd.empty:
            print('No difference found.')
        else:
            print('There is a difference in the file and here are they: {0}'.format(concat_pd))

    def __concat_drop_dataframes__(self, dataframe_one: pd.DataFrame, dataframe_two: pd.DataFrame):
        concat_pd = pd.concat([dataframe_one, dataframe_two], axis=0)
        concat_pd.drop_duplicates(keep=False, inplace=True)
        concat_pd.reset_index(drop=True, inplace=True)
        return concat_pd

    def compare_excel(self):
        workbook_one = openpyxl.load_workbook(self.file_one_path, read_only=True)
        workbook_two = openpyxl.load_workbook(self.file_two_path, read_only=True)

        if workbook_one.get_sheet_names() != workbook_two.get_sheet_names():
            print('Sheet names are different.')

        sheet_names = workbook_one.get_sheet_names()

        found_difference = False

        for sheet_name in sheet_names:
            sheet_one: openpyxl.workbook.workbook.ReadOnlyWorksheet = workbook_one[sheet_name]
            sheet_two = workbook_two[sheet_name]
            df_one = pd.DataFrame(sheet_one.values)
            df_two = pd.DataFrame(sheet_two.values)
            concat_pd = self.__concat_drop_dataframes__(df_one, df_two)
            if not concat_pd.empty:
                print('Difference found in sheet {0}\n'.format(sheet_name))
                print('Differences are : {0}\n'.format(concat_pd))
                found_difference = True

        if not found_difference:
            print('No difference found.')

        workbook_one.close()
        workbook_two.close()
