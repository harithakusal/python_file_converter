import pandas as pd
import os

all_files = [x for x in os.listdir() if x.endswith(".csv")]

for every_file in all_files:
    file_name = str(every_file)
    file_name = file_name.replace('.csv', '')
    current_file = pd.read_csv(every_file)
    current_file.to_json(file_name + '.json')

