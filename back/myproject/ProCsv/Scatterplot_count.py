import pandas as pd

class Scatterplot_count:
    AgeTimeNum1 = pd.read_csv('..\\..\\processed_csv\\processed_one\\AgeTimeNum1.csv', sep=',', low_memory=False, header=0)
    AgeTimeNum2 = pd.read_csv('..\\..\\processed_csv\\processed_one\\AgeTimeNum2.csv', sep=',', low_memory=False, header=0)
    AgeTimeNum = pd.merge(AgeTimeNum1, AgeTimeNum2, how='left', left_on=['AGE'], right_on=['AGE'])
    AgeTimeNum3 = pd.read_csv('..\\..\\processed_csv\\processed_one\\AgeTimeNum3.csv', sep=',', low_memory=False,
                              header=0)
    AgeTimeNum = pd.merge(AgeTimeNum, AgeTimeNum3, how='left', left_on=['AGE'], right_on=['AGE'])
    AgeTimeNum4 = pd.read_csv('..\\..\\processed_csv\\processed_one\\AgeTimeNum4.csv', sep=',', low_memory=False,
                              header=0)
    AgeTimeNum = pd.merge(AgeTimeNum, AgeTimeNum4, how='left', left_on=['AGE'], right_on=['AGE'])
    AgeTimeNum5 = pd.read_csv('..\\..\\processed_csv\\processed_one\\AgeTimeNum5.csv', sep=',', low_memory=False,
                              header=0)
    AgeTimeNum = pd.merge(AgeTimeNum, AgeTimeNum5, how='left', left_on=['AGE'], right_on=['AGE'])
    AgeTimeNum6 = pd.read_csv('..\\..\\processed_csv\\processed_one\\AgeTimeNum6.csv', sep=',', low_memory=False,
                              header=0)
    AgeTimeNum = pd.merge(AgeTimeNum, AgeTimeNum6, how='left', left_on=['AGE'], right_on=['AGE'])
    AgeTimeNum7 = pd.read_csv('..\\..\\processed_csv\\processed_one\\AgeTimeNum7.csv', sep=',', low_memory=False,
                              header=0)
    AgeTimeNum = pd.merge(AgeTimeNum, AgeTimeNum7, how='left', left_on=['AGE'], right_on=['AGE'])
    AgeTimeNum8 = pd.read_csv('..\\..\\processed_csv\\processed_one\\AgeTimeNum8.csv', sep=',', low_memory=False,
                              header=0)
    AgeTimeNum = pd.merge(AgeTimeNum, AgeTimeNum8, how='left', left_on=['AGE'], right_on=['AGE'])

    AgeTimeNum['TIME'] = (AgeTimeNum['TIME_1']+AgeTimeNum['TIME_2']+AgeTimeNum['TIME_3']+AgeTimeNum['TIME_4']+AgeTimeNum['TIME_5']+AgeTimeNum['TIME_6']+AgeTimeNum['TIME_7']+AgeTimeNum['TIME_8'])/8

    AgeTimeNum['NUM'] = (AgeTimeNum['NUM_1']+AgeTimeNum['NUM_2']+AgeTimeNum['NUM_3']+AgeTimeNum['NUM_4']+AgeTimeNum['NUM_5']+AgeTimeNum['NUM_6']+AgeTimeNum['NUM_7']+AgeTimeNum['NUM_8'])/8
    AgeTimeNum = AgeTimeNum.drop(['TIME_1', 'NUM_1', 'TIME_2', 'NUM_2' ,'TIME_3','NUM_3', 'TIME_4', 'NUM_4','TIME_5', 'NUM_5','TIME_6', 'NUM_6','TIME_7', 'NUM_7','TIME_8', 'NUM_8'],axis=1)
    #AgeTimeNum['TIME'] = AgeTimeNum['TIME']+ AgeTimeNum['TIME']+AgeTimeNum['TIME']
    AgeTimeNum['TIME'] = AgeTimeNum['TIME'].astype(int)
    AgeTimeNum['NUM'] = AgeTimeNum['NUM'].astype(int)
    t = AgeTimeNum['AGE']
    AgeTimeNum = AgeTimeNum.drop(['AGE'], axis=1)
    AgeTimeNum['AGE'] = t
    AgeTimeNum.to_csv('..\\..\\processed_csv\\processed_two\\AgeTimeNum.csv', index=0, sep=',')