# Parse CSV Files
# A very useful package called pandas. This package can parse CSV and excel files, and extract data from it easily.

# First, install the package
pip install pandas
# Then you can use it in your modules like this:
import pandas 
data=pandas.read_csv('file.csv)

# Pandas treats the first column as a label for each row by default.You can pass the  index_col parameter to specify the column index if it’s not the first column.
# If there are no row labels in your document, you should use the parameter index_col=False.
# To write to CSV file, you can use to_csv() method.
data.to_csv('file.csv)

# Parse Excel Files
# You can use read_excel() method from pandas module to parse excel files.
data = pd.read_excel('file.xls', sheetname='Sheet1')
# If you have multiple sheets, you can load it like this:
data = pd.ExcelFile('file.xls')
# You can write to excel files like this:
data.to_excel('file.xls', sheet='Sheet1')