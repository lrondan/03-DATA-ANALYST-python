import json
import pandas as pd

with open('amd/amd.json', 'r')as json_file:
    json_object = json.load(json_file)
    json_object('city', 'country', 'industry')
    df = pd.DataFrame(columns=json_object)
    print(df)