from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'A CLI based Python application to compare excel files'
LONG_DESCRIPTION = 'A CLI based Python application to compare files like csv, xlsx'

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="excel-compare",
    version=VERSION,
    author="Shubham Jain",
    author_email="shubhamj.code@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pandas', 'xlrd', 'openpyxl', 'click'],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'

    keywords=['excel', 'compare', 'excel-compare'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
