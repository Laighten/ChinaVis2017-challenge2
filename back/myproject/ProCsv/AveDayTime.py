import pandas as pd
from datetime import datetime

class AveDayTime:
    hydata = pd.read_csv('..\\..\\processed_csv\\processed_one\\hydata_4.csv', sep=',', low_memory=False, header=0)
    hydata = hydata.drop(['PERSONID', 'SITEID', 'XB', 'CUSTOMERNAME', 'OFFLINETIME', 'AREAID', 'BIRTHDAY'], axis=1)
    hydata[['ONLINETIME']] = hydata[['ONLINETIME']].astype(str)
    hydata['ONLINETIME'] = [datetime.strptime(x, '%Y%m%d%H%M%S') for x in hydata['ONLINETIME']]
    hydata['ONLINETIME'] = [datetime.strftime(x, '%Y%m%d') for x in hydata['ONLINETIME']]
    M = hydata['ONLINETIME'].value_counts()
    dict_m = {'Date': M.index, 'ONLINETIME_4': M.values}
    df_m = pd.DataFrame(dict_m)
    df_m.to_csv('..\\..\\processed_csv\\processed_one\\AvgDayTime4.csv', index=0, sep=',')