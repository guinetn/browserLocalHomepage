"""
pip install tabulate

tabulate() transform many different things into easy to read plain-text tables, such as a list of lists, dictionary of iterables, and others.
"""

table = [['First Name', 'Last Name', 'Age'], ['John', 'Smith', 39], ['Mary', 'Jane', 25], ['Jennifer', 'Doe', 28]]

print(table)


from tabulate import tabulate
print(tabulate(table))

print(tabulate(table, headers='firstrow'))
print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))


# dictionary of iterables:

info = {'First Name': ['John', 'Mary', 'Jennifer'], 'Last Name': ['Smith', 'Jane', 'Doe'], 'Age': [39, 25
print(tabulate(info, headers='keys', tablefmt='fancy_grid'))
