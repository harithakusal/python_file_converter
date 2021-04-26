import csv
import re
import pandas as pd
import os
import json

#
# # get all json files in directory
# all_files = [x for x in os.listdir() if x.endswith(".json")]
#
# for every_file in all_files:
#     # edit file name
#     file_name = str(every_file)
#     file_name = file_name.replace('.json', '')
#
#     # read json
#     current_file = pd.read_json(every_file)
#
#
#     # output normal text
#     current_file.to_csv(file_name + '.txt', index=None, header=True)


# get all txt files in directory
all_files = [x for x in os.listdir() if x.endswith(".txt")]

for every_file in all_files:
    # edit file name
    file_name = str(every_file)
    file_name = file_name.replace('.txt', '')

    # read txt
    current_file = open(every_file, "r")
    current_file = current_file.read()

    # beautify csv
    current_file = re.sub(r'(\s)', r'', current_file)  # remove spaces
    # current_file = current_file.rstrip('\n')  # remove newline character
    current_file = re.sub('},', '\n', current_file)  # break line after "},"
    current_file = re.sub("['\"{}@[]", "", current_file)  # remove ,"{}[]@ characters
    # print(current_file)

    # output csv
    # current_file.to_csv(file_name + '.csv', index=None, header=True)
    with open(file_name + '.csv', 'w') as output_csv:
        csv.writer(output_csv)
