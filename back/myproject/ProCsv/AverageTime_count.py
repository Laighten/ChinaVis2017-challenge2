import pandas as pd

class AverageTime_count:
    AverageTime = pd.read_csv('..\\..\\processed_csv\\processed_one\\AvgTime1.csv', sep=',', low_memory=False, header=0)
    AverageTime2 = pd.read_csv('..\\..\\processed_csv\\processed_one\\AvgTime2.csv', sep=',', low_memory=False,
                               header=0)
    AverageTime = pd.merge(AverageTime, AverageTime2, how='left', left_on=['ID'], right_on=['ID'])
    AverageTime3 = pd.read_csv('..\\..\\processed_csv\\processed_one\\AvgTime3.csv', sep=',', low_memory=False,
                               header=0)
    AverageTime = pd.merge(AverageTime, AverageTime3, how='left', left_on=['ID'], right_on=['ID'])
    AverageTime4 = pd.read_csv('..\\..\\processed_csv\\processed_one\\AvgTime4.csv', sep=',', low_memory=False,
                               header=0)
    AverageTime = pd.merge(AverageTime, AverageTime4, how='left', left_on=['ID'], right_on=['ID'])
    AverageTime5 = pd.read_csv('..\\..\\processed_csv\\processed_one\\AvgTime5.csv', sep=',', low_memory=False,
                               header=0)
    AverageTime = pd.merge(AverageTime, AverageTime5, how='left', left_on=['ID'], right_on=['ID'])

    AverageTime6 = pd.read_csv('..\\..\\processed_csv\\processed_one\\AvgTime6.csv', sep=',', low_memory=False,
                               header=0)
    AverageTime = pd.merge(AverageTime, AverageTime6, how='left', left_on=['ID'], right_on=['ID'])

    AverageTime7 = pd.read_csv('..\\..\\processed_csv\\processed_one\\AvgTime7.csv', sep=',', low_memory=False,
                               header=0)
    AverageTime = pd.merge(AverageTime, AverageTime7, how='left', left_on=['ID'], right_on=['ID'])

    AverageTime8 = pd.read_csv('..\\..\\processed_csv\\processed_one\\AvgTime8.csv', sep=',', low_memory=False,
                               header=0)
    AverageTime = pd.merge(AverageTime, AverageTime8, how='left', left_on=['ID'], right_on=['ID'])
    AverageTime['ONLINETIME'] = (AverageTime['ONLINETIME_1']+AverageTime['ONLINETIME_2']+AverageTime['ONLINETIME_3']+AverageTime['ONLINETIME_4']+AverageTime['ONLINETIME_5']+AverageTime['ONLINETIME_6']+AverageTime['ONLINETIME_7']+AverageTime['ONLINETIME_8'])/8
    AverageTime = AverageTime.drop(['ONLINETIME_1','ONLINETIME_2','ONLINETIME_3','ONLINETIME_4','ONLINETIME_5','ONLINETIME_6','ONLINETIME_7','ONLINETIME_8'], axis=1)
    AverageTime['ONLINETIME'] = AverageTime['ONLINETIME'].astype(int)
    AverageTime = pd.DataFrame(AverageTime)
    AverageTime.set_index('ID', inplace=True)
    Ha = pd.DataFrame()
    Ha = Ha.append(AverageTime['ONLINETIME'], ignore_index=True)

    Ha.to_csv('..\\..\\processed_csv\\processed_two\\AvgTime.csv', index=0, sep=',')