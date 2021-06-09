from excel_compare import CompareFiles

if __name__ == '__main__':
    file_one = '../test files/similar_csv_files/one.csv'
    file_two = '../test files/similar_csv_files/two.csv'
    compare_files = CompareFiles(file_one, file_two)
    compare_files.compare_csv()
