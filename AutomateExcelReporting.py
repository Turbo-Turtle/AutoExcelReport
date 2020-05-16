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

# pip3 install xlrd (if needed)
#print(df_first_shift)
