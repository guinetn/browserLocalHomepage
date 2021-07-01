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




f = open("data.csv", 'r')
dataset = f.read()
rows = dataset.split('\n')

with open(filename) as f:
	reader = csv.reader(f)
	next(reader)		# Ignore the header row.    
	# Store the latitudes and longitudes in the appropriate lists.
	for row in reader:
    	lats.append(float(row[1]))
    	lons.append(float(row[2]))



    	


# https://docs.python.org/3.3/library/csv.html

import csv

# Open the earthquake data file.
filename = 'datasets/earthquake_data.csv'

# Create empty lists for the latitudes and longitudes.
lats, lons = [], []

# Read through the entire file, skip the first line,
#  and pull out just the lats and lons.
with open(filename) as f:
    # Create a csv reader object.
    reader = csv.reader(f)

    # Ignore the header row.
    next(reader)

    # Store the latitudes and longitudes in the appropriate lists.
    for row in reader:
        lats.append(float(row[1]))
        lons.append(float(row[2]))

# Display the first 5 lats and lons.
print('lats', lats[0:5])
print('lons', lons[0:5])