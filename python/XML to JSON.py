import pandas as pd
import os
import json
import xmltodict

all_files = [x for x in os.listdir() if x.endswith(".xml")]

# opening the xml file
for every_file in all_files:
    with open(every_file, "r") as xmlfileObj:

        file_name = str(every_file)
        file_name = file_name.replace('.xml', '')

        data_dict = xmltodict.parse(xmlfileObj.read())
        xmlfileObj.close()
         
        jsonObj= json.dumps(data_dict, sort_keys=True, indent=3)
        
        with open(file_name, "w") as jsonfileObj:
            jsonfileObj.write(jsonObj)
            jsonfileObj.close()
