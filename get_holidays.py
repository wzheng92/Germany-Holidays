import urllib.request
import json
import pandas as pd

YEAR = 2019
YEAR = [2005, 2006, 2007, 2018]
YEAR = [y for y in range(2001, 2020)]
LAND = 'NI'

if isinstance(YEAR,int):
    url = "https://feiertage-api.de/api/?jahr=%d&nur_land=%s" % (YEAR, LAND)
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    df = pd.DataFrame(columns=['Date', 'Name'])
    for key in data.keys():
        df = df.append({'Date': data[key]['datum'], 'Name': key}, ignore_index=True)
    print(df)
    df.to_csv('output\\holidays_in_%d.csv' % YEAR, sep=';', index=None)
    

if isinstance(YEAR, list):
    df_gesamt = pd.DataFrame(columns=['Date', 'Name'])
    for year in YEAR:
        url = "https://feiertage-api.de/api/?jahr=%d&nur_land=%s" % (year, LAND)
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())  
        df = pd.DataFrame(columns=['Date', 'Name'])
        for key in data.keys():
            df = df.append({'Date': data[key]['datum'], 'Name': key}, ignore_index=True)
            df.to_csv('output\\holidays_in_%d.csv' % year, sep=';', index=None)
        df_gesamt = df_gesamt.append(df)
        print(df_gesamt)
    
