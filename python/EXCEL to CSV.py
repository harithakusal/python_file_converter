import pandas as pd
import os

all_files = [x for x in os.listdir() if x.endswith(".xlsx")]

for every_file in all_files:
    file_name = str(every_file)
    file_name = file_name.replace('.xlsx', '')
    current_file = pd.read_excel(every_file)
    current_file.to_csv(file_name + '.csv', index=None, header=True)

