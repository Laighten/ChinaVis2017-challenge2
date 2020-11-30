import pandas as pd
from datetime import datetime

class ClickTime:
    JuvRed = pd.read_csv('..\\..\\processed_csv\\processed_two\\DirectJuvTime.csv', sep=',', low_memory=False, header=0)
    JuvBlue = pd.read_csv('..\\..\\processed_csv\\processed_two\\IndirectJuvTime.csv', sep=',', low_memory=False, header=0)

    da1 = JuvRed.drop(['TITLE', 'lng', 'lat', 'Juv'], axis=1)
    da2 = JuvBlue.drop(['TITLE', 'lng', 'lat', 'JuvIn'], axis=1)
    da = da1.append(da2, ignore_index=True)
    da = da.drop_duplicates()
    # da = pd.read_csv('..\\..\\processed_csv\\processed_two\\Juv.csv', sep=',', low_memory=False, header=0)
    # da = da.drop(['TITLE','lng','lat','Juv','JuvIn'], axis=1)

    daOver18 = da
    csv = pd.read_csv('..\\..\\processed_csv\\processed_two\\hydata_count.csv', sep=',', low_memory=False, header=0)
    csv['ONLINETIME'] = csv[['ONLINETIME']].astype(str)
    csv['ONLINETIME'] = [datetime.strptime(x, '%Y%m%d%H%M%S') for x in csv['ONLINETIME']]
    csv = csv.drop(['XB', 'CUSTOMERNAME', 'OFFLINETIME', 'AREAID'], axis=1)
    #print(csv2)
    csv['ONLINETIME'] = [datetime.strftime(x, '%H') for x in csv['ONLINETIME']]
    csv['ONLINETIME'] = csv['ONLINETIME'].astype(int)
    csv['BIRTHDAY'] = csv['BIRTHDAY'].astype(int)

    csv2 = pd.read_csv('..\\..\\processed_csv\\processed_two\\IndirectJuvDetail.csv', sep=',', low_memory=False, header=0)
    csv2['ONLINETIME'] = (csv2['ONLINETIME']/10000).astype(int)
    csv2['ONLINETIME'] = csv2['ONLINETIME'].astype(str)
    csv2['ONLINETIME'] = [datetime.strptime(x, '%Y%m%d%H') for x in csv2['ONLINETIME']]
    csv2 = csv2.drop(['XB', 'CUSTOMERNAME', 'OFFLINETIME', 'AREAID', 'timestamp'], axis=1)
    csv2['ONLINETIME'] = [datetime.strftime(x, '%H') for x in csv2['ONLINETIME']]
    csv2['ONLINETIME'] = csv2['ONLINETIME'].astype(int)
    csv1 = csv[csv['BIRTHDAY'] >= 19981100]
    csv2 = csv2.append(csv1, ignore_index=True)

    csv3 = csv[csv['BIRTHDAY'] <= 19981000]

    for i in range(0, 24):
        dal = csv2[csv2['ONLINETIME'] == i]
        M = dal['SITEID'].value_counts()
        dict_m = {'SITEID': M.index, i: M.values}
        df_m = pd.DataFrame(dict_m)
        da = pd.merge(da, df_m, how='left', left_on=['SITEID'], right_on=['SITEID'])
        da.fillna(0, inplace=True)
        da[i] = da[i].astype(int)
    for i in range(0, 24):
        daM = csv3[csv3['ONLINETIME'] == i]
        M = daM['SITEID'].value_counts()
        dict_m = {'SITEID': M.index, i: M.values}
        df_m = pd.DataFrame(dict_m)
        daOver18 = pd.merge(daOver18, df_m, how='left', left_on=['SITEID'], right_on=['SITEID'])
        daOver18.fillna(0, inplace=True)
        daOver18[i] = daOver18[i].astype(int)
    da.to_csv('..\\..\\processed_csv\\processed_two\\ClickTime18.csv', index=0, sep=',')
    daOver18.to_csv('..\\..\\processed_csv\\processed_two\\ClickTimeOver18.csv', index=0, sep=',')
