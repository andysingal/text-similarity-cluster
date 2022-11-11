# Load CSV's & Create Dataframes
import pandas as pd
import openpyxl

input_data = pd.read_csv("input.csv")
output_data = pd.read_csv("output.csv")

input_data.columns = ["ID","keyword"]
output_data.columns = ["ID","keyword"]

input_data.describe()

# Drop Duplicates from Output CSV, ID column
output_data.drop_duplicates(inplace=True)

input_data.drop(columns="ID",inplace=True)
output_data.drop(columns="ID",inplace=True)

input_data

output_data

# Create Mappings JSON
# create dict to store keywords and indices they match in original document
from collections import defaultdict
mappings_json = defaultdict(list)
mappings_json

# create list of keys from output csv, which will be used to find indices in original csv
output_keys = list(output_data['keyword'])

# some keywords have 0 results on their own such as numbers like "2205200030001371"
# add to dict only if found indices are not 0
# increment indices by 2 to compensate for removal of "genie"
for key in output_keys:
    indices = input_data.index[input_data['keyword'] == key].to_list()
    indices = list(map(lambda x : x+2, indices))
    if len(indices):
        mappings_json[key] = indices

print(dict(mappings_json))

# Update CSV to highlight rows with same values
# output_csv = openpyxl.load_workbook("output.csv")
# print(output_csv)