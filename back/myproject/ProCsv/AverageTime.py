import pandas as pd
from datetime import datetime

class AveTime:
    hydata = pd.read_csv('..\\..\\processed_csv\\processed_one\\hydata_8.csv', sep=',', low_memory=False, header=0)
    hydata = hydata.drop(['PERSONID', 'SITEID', 'XB', 'CUSTOMERNAME', 'OFFLINETIME', 'AREAID', 'BIRTHDAY'], axis=1)
    hydata[['ONLINETIME']] = hydata[['ONLINETIME']].astype(str)
    hydata['ONLINETIME'] = [datetime.strptime(x, '%Y%m%d%H%M%S') for x in hydata['ONLINETIME']]
    hydata['ONLINETIME'] = [datetime.strftime(x, '%H') for x in hydata['ONLINETIME']]
    hydata['ONLINETIME'] = hydata['ONLINETIME'].astype(int)
    M = hydata['ONLINETIME'].value_counts()

    dict_m = {'ID': M.index, 'ONLINETIME_8': M.values}
    df_m = pd.DataFrame(dict_m)
    df_m.sort_values('ID', inplace=True)
    # df_m.set_index('ID', inplace=True)
    df_m['ONLINETIME_8'] = df_m['ONLINETIME_8']/90
    df_m['ONLINETIME_8'] = df_m['ONLINETIME_8'].astype(int)
    # Ha = pd.DataFrame()
    # Ha = Ha.append(df_m['ONLINETIME'], ignore_index=True)
    #print(df_m)
    df_m.to_csv('..\\..\\processed_csv\\processed_one\\AvgTime8.csv', index=0, sep=',')