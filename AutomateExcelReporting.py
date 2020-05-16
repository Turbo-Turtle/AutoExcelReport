import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Denote the path to excel workbooks:
excel_file_1 = 'Day-Shift.xlsx'
excel_file_2 = 'Night-Shift.xlsx'

# Import data into python-
# Create Data-Frames for each excel sheet:
df_first_shift = pd.read_excel(excel_file_1, sheet_name='Sheet1')
df_second_shift = pd.read_excel(excel_file_1, sheet_name='Sheet2')
df_third_shift = pd.read_excel(excel_file_2)  # Reads first sheet by default

#======================================

# pip3 install xlrd, openpyxl (if needed)
# Check:
# print(df_first_shift)
# print(df_first_shift['Product'])


# concat function joins all of the values where the column heading is the same
# make a list of all the frames that we want to concatenate into a single dataframe:
df_all = pd.concat([df_first_shift, df_second_shift, df_third_shift])

# Check:
# print(df_all)

#======================================

# Calculations:

# Calculate which shift was the most productive:
pivot = df_all.groupby(['Shift']).mean()
shift_productivity = pivot.loc[:,
                               'Production Run Time (Min)':'Products Produced (Units)']


# Check:
# print(shift_productivity)


#======================================

# Graphing:

shift_productivity.plot(kind='bar')

# Check:
# plt.show()


#======================================

# Output to excel:

# Creates an excel file in the same directory as this .py file:
df_all.to_excel('output.xlsx')
