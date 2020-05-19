import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Denote the path to excel workbooks:
excel_file_1 = '4564564655.xls'
excel_file_2 = '4564564656.xls'

# Import data into python-
# Create Data-Frames for each excel sheet:
df_first_set = pd.read_excel(excel_file_1, sheet_name='Side_View')
df_second_set = pd.read_excel(excel_file_1, sheet_name='Side_View')
# df_third_shift = pd.read_excel(excel_file_2)  # Reads first sheet by default

#======================================

# pip3 install xlrd, openpyxl (if needed)
# Check:
# print(df_first_shift)
# print(df_first_shift['Product'])


# concat function joins all of the values where the column heading is the same
# make a list of all the frames that we want to concatenate into a single dataframe:
df_all = pd.concat([df_first_set, df_second_set])

# Check:
# print(df_all)

#======================================

# Calculations:

# Calculate which shift was the most productive:
pivot = df_all.groupby(['Dimension']).mean()
Capability = pivot.loc[:,
                       'Avg. dev.':'St.Dev.']


# Check:
# print(Capability)


#======================================

# Graphing:

Capability.plot(kind='bar')

# Check:
# plt.show()


#======================================

# Output to excel:

# Creates an excel file in the same directory as this .py file:
df_all.to_excel('Capability.xlsx')
