from excel_compare import CompareFiles
import click


@click.command()
@click.option('--file_one', '-f1')
@click.option('--file_two', '-f2')
@click.option('--file_type', '-type')
def compare(file_one, file_two, file_type):
    compare_file = CompareFiles(file_one, file_two)
    if file_type == 'csv':
        compare_file.compare_csv()
    elif file_type == 'xlsx':
        compare_file.compare_excel()
    else:
        print('{0} is not supported.'.format(file_type))


if __name__ == '__main__':
    compare()
