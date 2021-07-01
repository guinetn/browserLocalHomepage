
    # read Excel file into a DataFrame
    df = pd.read_excel(r'./Importing files/World_city.xlsx')
    # print values
    df

    # multiple sheets: read Excel sheets in pandas
    xl = pd.ExcelFile(r'./Importing files/World_city.xlsx')

    # print sheet name
    xl.sheet_names

    # read Europe sheet
    df = pd.read_excel(r'./Importing files/World_city.xlsx',sheet_name='Europe')
    df