import pandas as pd

class AvgDayTime_count:
    AvgDayTime = pd.read_csv('..\\..\\processed_csv\\processed_one\\AvgDayTime1.csv', sep=',', low_memory=False, header=0)
    AvgDayTime2 = pd.read_csv('..\\..\\processed_csv\\processed_one\\AvgDayTime2.csv', sep=',', low_memory=False, header=0)
    AvgDayTime = pd.merge(AvgDayTime, AvgDayTime2, how='left', left_on=['Date'], right_on=['Date'])
    AvgDayTime3 = pd.read_csv('..\\..\\processed_csv\\processed_one\\AvgDayTime3.csv', sep=',', low_memory=False,header=0)
    AvgDayTime = pd.merge(AvgDayTime, AvgDayTime3, how='left', left_on=['Date'], right_on=['Date'])
    AvgDayTime4 = pd.read_csv('..\\..\\processed_csv\\processed_one\\AvgDayTime4.csv', sep=',', low_memory=False,header=0)
    AvgDayTime = pd.merge(AvgDayTime, AvgDayTime4, how='left', left_on=['Date'], right_on=['Date'])
    AvgDayTime5 = pd.read_csv('..\\..\\processed_csv\\processed_one\\AvgDayTime5.csv', sep=',', low_memory=False,
                              header=0)
    AvgDayTime = pd.merge(AvgDayTime, AvgDayTime5, how='left', left_on=['Date'], right_on=['Date'])
    AvgDayTime6 = pd.read_csv('..\\..\\processed_csv\\processed_one\\AvgDayTime6.csv', sep=',', low_memory=False,
                              header=0)
    AvgDayTime = pd.merge(AvgDayTime, AvgDayTime6, how='left', left_on=['Date'], right_on=['Date'])
    AvgDayTime7 = pd.read_csv('..\\..\\processed_csv\\processed_one\\AvgDayTime7.csv', sep=',', low_memory=False,
                              header=0)
    AvgDayTime = pd.merge(AvgDayTime, AvgDayTime7, how='left', left_on=['Date'], right_on=['Date'])
    AvgDayTime8 = pd.read_csv('..\\..\\processed_csv\\processed_one\\AvgDayTime8.csv', sep=',', low_memory=False,
                              header=0)
    AvgDayTime = pd.merge(AvgDayTime, AvgDayTime8, how='left', left_on=['Date'], right_on=['Date'])
    AvgDayTime['ONLINETIME'] = AvgDayTime['ONLINETIME_1'] + AvgDayTime['ONLINETIME_2']+ AvgDayTime['ONLINETIME_3']+ AvgDayTime['ONLINETIME_4'] + AvgDayTime['ONLINETIME_5'] + AvgDayTime['ONLINETIME_6']+AvgDayTime['ONLINETIME_7']+AvgDayTime['ONLINETIME_8']
    AvgDayTime = AvgDayTime.drop(['ONLINETIME_1','ONLINETIME_2','ONLINETIME_3','ONLINETIME_4','ONLINETIME_5','ONLINETIME_6','ONLINETIME_7','ONLINETIME_8'], axis=1)
    AvgDayTime = pd.DataFrame(AvgDayTime)
    AvgDayTime['ONLINETIME'] = AvgDayTime['ONLINETIME'].astype(int)
    AvgDayTime.to_csv('..\\..\\processed_csv\\processed_two\\AvgDayTime.csv', index=0, sep=',')
