from pathlib import Path
import pandas as pd


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
        concat_pd = pd.concat([file_one, file_two], axis=0)
        concat_pd.drop_duplicates(keep=False, inplace=True)
        concat_pd.reset_index(drop=True, inplace=True)
        if concat_pd.empty:
            print('No difference found.')
        else:
            print('There is a difference in the file and here are they: {0}'.format(concat_pd))

    def compare_excel(self):
        pass

    def __close__(self):
        pass
