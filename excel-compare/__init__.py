from excel_compare import CompareFiles

if __name__ == '__main__':
    file_one = '../test files/similar_excel_files/one.xlsx'
    file_two = '../test files/similar_excel_files/two.xlsx'
    compare_files = CompareFiles(file_one, file_two)
    compare_files.compare_excel()
