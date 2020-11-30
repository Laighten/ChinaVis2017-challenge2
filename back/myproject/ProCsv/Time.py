import pandas as pd
from datetime import datetime

class GeoTime:

    da = pd.read_csv('..\\..\\processed_csv\\processed_two\\hydata_count.csv', sep=',', low_memory=False, header=0)

    da3 = pd.read_csv('..\\..\\processed_csv\\processed_two\\Juv_1.csv', sep=',', low_memory=False, header=0)

    da['ONLINETIME'] = da[['ONLINETIME']].astype(str)
    da['ONLINETIME'] = [datetime.strptime(x, '%Y%m%d%H%M%S') for x in da['ONLINETIME']]
    da = da.drop(['XB', 'CUSTOMERNAME', 'AREAID', 'BIRTHDAY'], axis=1)
    da['ONLINETIME'] = [datetime.strftime(x, '%H') for x in da['ONLINETIME']]
    da['ONLINETIME'] = da['ONLINETIME'].astype(int)
    da3 = da3.drop(['TITLE','lng','lat','Juv_count'], axis=1)
    merged1 = da3
    for i in range(0, 24):
       dal = da[da['ONLINETIME'] == i]
       M = dal['SITEID'].value_counts()
       dict_m = {'SITEID': M.index, i: M.values}
       df_m = pd.DataFrame(dict_m)
       merged1 = pd.merge(merged1, df_m, how='left', left_on=['SITEID'], right_on=['SITEID'])
       merged1.fillna(0, inplace=True)
       merged1[i] = merged1[i].astype(int)

    merged1.to_csv('..\\..\\processed_csv\\processed_two\\JuvTime.csv', index=0, sep=',')
