import pandas as pd
from datetime import datetime

class GeoTime:
    ApiAll = pd.read_csv('..\\..\\processed_csv\\processed_two\\ApiAll.csv', sep=',', low_memory=False, header=0)
    hydata_all = pd.read_csv('..\\..\\processed_csv\\processed_two\\hydata_count.csv', sep=',', low_memory=False, header=0)
    # ApiAll = ApiAll.drop(['lng', 'lat'], axis=1)

    #接纳未成年人上网数量（直接接纳和间接接纳）
    Juv_0 = pd.read_csv('..\\..\\processed_csv\\processed_two\\Juv_0.csv', sep=',', low_memory=False, header=0)
    Injuv = pd.read_csv('..\\..\\processed_csv\\processed_two\\Injuv.csv', sep=',', low_memory=False, header=0)
    Injuv = Injuv.drop(['timestamp'], axis=1)
    Juv = Juv_0.append(Injuv, ignore_index=True)
    Juv = Juv.drop_duplicates()
    M = Juv['SITEID'].value_counts()
    dict_m = {'SITEID': M.index, 'Under_age': M.values}
    df_m = pd.DataFrame(dict_m)
    merged1 = pd.merge(ApiAll, df_m, how='left', left_on=['SITEID'], right_on=['SITEID'])
    merged1.fillna(0, inplace=True)
    merged1[['Under_age']] = merged1[['Under_age']].astype(int)
    #print(merged1)

    #统计 age>68岁的人数
    # hydata_all[['BIRTHDAY']] = hydata_all[['BIRTHDAY']].astype(int)
    Be_age = hydata_all[hydata_all['BIRTHDAY'] < 19480000]
    Be_age = Be_age[Be_age['BIRTHDAY'] >= 19000000]
    M = Be_age['SITEID'].value_counts()
    dict_m = {'SITEID': M.index, 'UnnormalAge': M.values}
    df_m = pd.DataFrame(dict_m)
    merged2 = pd.merge(merged1, df_m, how='left', left_on=['SITEID'], right_on=['SITEID'])
    merged2.fillna(0, inplace=True)
    merged2[['UnnormalAge']] = merged2[['UnnormalAge']].astype(int)
    #print(merged2)

    # 单次连续上网超过48小时的人数
    hydata_all[['timestamp']] = hydata_all[['timestamp']].astype(int)
    Is_time = hydata_all[hydata_all['timestamp'] >= 172800]
    M = Is_time['SITEID'].value_counts()
    dict_m = {'SITEID': M.index, 'OvertimeOnNet': M.values}
    df_m = pd.DataFrame(dict_m)
    merged3 = pd.merge(merged2, df_m, how='left', left_on=['SITEID'], right_on=['SITEID'])
    merged3.fillna(0, inplace=True)
    merged3[['OvertimeOnNet']] = merged3[['OvertimeOnNet']].astype(int)
    #print(merged3)

    # 外来人口上网次数
    hydata_all[['AREAID']] = hydata_all[['AREAID']].astype(int)
    foreign = hydata_all[(hydata_all['AREAID'] < 510200) | (hydata_all['AREAID'] >= 510299)]
    M = foreign['SITEID'].value_counts()
    dict_m = {'SITEID': M.index, 'ExternalPeople': M.values}
    df_m = pd.DataFrame(dict_m)
    merged4 = pd.merge(merged3, df_m, how='left', left_on=['SITEID'], right_on=['SITEID'])
    merged4.fillna(0, inplace=True)
    merged4[['ExternalPeople']] = merged4[['ExternalPeople']].astype(int)

    # 每个网吧24点以后上网的人数
    hydata_all[['ONLINETIME']] = hydata_all[['ONLINETIME']].astype(str)
    a = hydata_all[['ONLINETIME']].astype(float)
    b = a / 10000
    b = b.astype(int)
    c = b % 100
    hydata_all['MidnightOnNet'] = c
    late_time = hydata_all[(hydata_all['MidnightOnNet'] >= 0) & (hydata_all['MidnightOnNet'] <= 4)]
    Online17_18 = hydata_all[(hydata_all['MidnightOnNet'] >= 17) & (hydata_all['MidnightOnNet'] <= 18)]
    M = late_time['SITEID'].value_counts()
    dict_m = {'SITEID': M.index, 'MidnightOnNet': M.values}
    df_m = pd.DataFrame(dict_m)
    merged5 = pd.merge(merged4, df_m, how='left', left_on=['SITEID'], right_on=['SITEID'])
    merged5.fillna(0, inplace=True)
    merged5[['MidnightOnNet']] = merged5[['MidnightOnNet']].astype(int)

    M1 = Online17_18['SITEID'].value_counts()
    dict_m = {'SITEID': M1.index, 'Online17_18': M1.values}
    df_m = pd.DataFrame(dict_m)
    merged6 = pd.merge(merged5, df_m, how='left', left_on=['SITEID'], right_on=['SITEID'])
    merged6.fillna(0, inplace=True)
    merged6[['Online17_18']] = merged6[['Online17_18']].astype(int)
    #print(merged5)

    # age18_44
    age1 = hydata_all[hydata_all['BIRTHDAY'] >= 19720000]
    age1 = age1[age1['BIRTHDAY'] <= 19981100]
    M = age1['SITEID'].value_counts()
    dict_m = {'SITEID': M.index, 'age18_44': M.values}
    df_m = pd.DataFrame(dict_m)
    merged7 = pd.merge(merged6, df_m, how='left', left_on=['SITEID'], right_on=['SITEID'])
    merged7.fillna(0, inplace=True)
    merged7[['age18_44']] = merged7[['age18_44']].astype(int)

    # age45_52
    age2 = hydata_all[hydata_all['BIRTHDAY'] >= 19640000]
    age2 = age2[age2['BIRTHDAY'] <= 19711231]
    M = age2['SITEID'].value_counts()
    dict_m = {'SITEID': M.index, 'age45_52': M.values}
    df_m = pd.DataFrame(dict_m)
    merged8 = pd.merge(merged7, df_m, how='left', left_on=['SITEID'], right_on=['SITEID'])
    merged8.fillna(0, inplace=True)
    merged8[['age45_52']] = merged8[['age45_52']].astype(int)

    # age53_68
    age3 = hydata_all[hydata_all['BIRTHDAY'] >= 19480000]
    age3 = age3[age3['BIRTHDAY'] <= 19631231]
    M = age3['SITEID'].value_counts()
    dict_m = {'SITEID': M.index, 'age53_68': M.values}
    df_m = pd.DataFrame(dict_m)
    merged9 = pd.merge(merged8, df_m, how='left', left_on=['SITEID'], right_on=['SITEID'])
    merged9.fillna(0, inplace=True)
    merged9[['age53_68']] = merged9[['age53_68']].astype(int)
    merged9.to_csv('..\\..\\processed_csv\\processed_two\\GeoTime.csv', index=0, sep=',')



