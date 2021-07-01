# Parse CSV Files
# A very useful package called 

# First, install the package pandas to parse CSV, Excel files, and extract data
# pip install pandas

# Then you can use it in your modules
import pandas as pd

df = pd.DataFrame(data={"id": ['a', 'b', 'c'],
                        "value": [1, 2, 3]})

def multiply_value(df, multiplier):
    df = df.copy()
    df["value"] = df["value"] * multiplier

multiplier_list = [1, 2, "3"]

for mult in multiplier_list:
    multiply_value(df, mult)

'''
DEBUGGING PYTHON SCRIPTS IN VS CODE

Error: DLL load failed while importing _multiarray_umath: Le module spécifié est introuvable.
Fix:  update your environment variable "PATH" adding \Library\bin
Note: Follow this step only if you have already installed numpy and still facing issue.
C:\Users\<username>\AppData\Roaming\Python\Python<version>\Library\bin
C:\Users\<username>\AppData\Local\Continuum\Anaconda<version>\Library\bin\

'''


See decorators
