import pandas as pd
import time

class DataClear:
    hydata1 = pd.read_csv('..\\..\\processed_csv\\original_data\\hydata_swjl_15.csv', sep=',', low_memory=False, header=0)
    hydata2 = pd.read_csv('..\\..\\processed_csv\\original_data\\hydata_swjl_16.csv', sep=',', low_memory=False, header=0)
    hydata = hydata1.append(hydata2, ignore_index=True)
    hydata['BIRTHDAY'] = hydata['BIRTHDAY'].astype(int)
    hydata = hydata[hydata['BIRTHDAY'] >= 19160000]
    hydata = hydata[hydata['BIRTHDAY'] <= 20100000]
    hydata['m'] = hydata['OFFLINETIME'].astype(float)
    hydata = hydata[hydata['m'] <= 20170000000000]
    hydata = hydata.drop(['m'], axis=1)
    hydata[['ONLINETIME']] = hydata[['ONLINETIME']].astype(str)
    hydata[['OFFLINETIME']] = hydata[['OFFLINETIME']].astype(str)
    timestamp1 = hydata['ONLINETIME'].apply(lambda x: time.mktime(time.strptime(x, '%Y%m%d%H%M%S')))
    timestamp2 = hydata['OFFLINETIME'].apply(lambda x: time.mktime(time.strptime(x, '%Y%m%d%H%M%S')))
    hydata['timestamp'] = timestamp2 - timestamp1
    hydata = hydata[hydata['timestamp'] > 0]
    hydata.to_csv('..\\..\\processed_csv\\processed_one\\hydata_8.csv', index=0, sep=',')