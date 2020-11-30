import pandas as pd

class Juv_0:
    Juv1 = pd.read_csv('..\\..\\processed_csv\\processed_one\\hydata_1.csv', sep=',', low_memory=False, header=0)
    Juv1 = Juv1.drop(['PERSONID'],axis=1)
    Juv1 = Juv1[Juv1['BIRTHDAY'] >= 19000000]
    Juv1 = Juv1[Juv1['BIRTHDAY'] <= 20160000]
    Juv1 = Juv1[Juv1['BIRTHDAY'] >= 19990000]

    Juv2 = pd.read_csv('..\\..\\processed_csv\\processed_one\\hydata_2.csv', sep=',', low_memory=False, header=0)
    Juv2 = Juv2.drop(['PERSONID'], axis=1)
    Juv2 = Juv2[Juv2['BIRTHDAY'] >= 19000000]
    Juv2 = Juv2[Juv2['BIRTHDAY'] <= 20160000]
    Juv2 = Juv2[Juv2['BIRTHDAY'] >= 19990000]

    Juv3 = pd.read_csv('..\\..\\processed_csv\\processed_one\\hydata_3.csv', sep=',', low_memory=False, header=0)
    Juv3 = Juv3.drop(['PERSONID'], axis=1)
    Juv3 = Juv3[Juv3['BIRTHDAY'] >= 19000000]
    Juv3 = Juv3[Juv3['BIRTHDAY'] <= 20160000]
    Juv3 = Juv3[Juv3['BIRTHDAY'] >= 19990000]

    Juv4 = pd.read_csv('..\\..\\processed_csv\\processed_one\\hydata_4.csv', sep=',', low_memory=False, header=0)
    Juv4 = Juv4.drop(['PERSONID'], axis=1)
    Juv4 = Juv4[Juv4['BIRTHDAY'] >= 19000000]
    Juv4 = Juv4[Juv4['BIRTHDAY'] <= 20160000]
    Juv4 = Juv4[Juv4['BIRTHDAY'] >= 19990000]

    Juv5 = pd.read_csv('..\\..\\processed_csv\\processed_one\\hydata_5.csv', sep=',', low_memory=False, header=0)
    Juv5 = Juv5.drop(['PERSONID'], axis=1)
    Juv5 = Juv5[Juv5['BIRTHDAY'] >= 19000000]
    Juv5 = Juv5[Juv5['BIRTHDAY'] <= 20160000]
    Juv5 = Juv5[Juv5['BIRTHDAY'] >= 19990000]

    Juv6 = pd.read_csv('..\\..\\processed_csv\\processed_one\\hydata_6.csv', sep=',', low_memory=False, header=0)
    Juv6 = Juv6.drop(['PERSONID'], axis=1)
    Juv6 = Juv6[Juv6['BIRTHDAY'] >= 19000000]
    Juv6 = Juv6[Juv6['BIRTHDAY'] <= 20160000]
    Juv6 = Juv6[Juv6['BIRTHDAY'] >= 19990000]

    Juv7 = pd.read_csv('..\\..\\processed_csv\\processed_one\\hydata_7.csv', sep=',', low_memory=False, header=0)
    Juv7 = Juv7.drop(['PERSONID'], axis=1)
    Juv7 = Juv7[Juv7['BIRTHDAY'] >= 19000000]
    Juv7 = Juv7[Juv7['BIRTHDAY'] <= 20160000]
    Juv7 = Juv7[Juv7['BIRTHDAY'] >= 19990000]

    Juv8 = pd.read_csv('..\\..\\processed_csv\\processed_one\\hydata_8.csv', sep=',', low_memory=False, header=0)
    Juv8 = Juv8.drop(['PERSONID'], axis=1)
    Juv8 = Juv8[Juv8['BIRTHDAY'] >= 19000000]
    Juv8 = Juv8[Juv8['BIRTHDAY'] <= 20160000]
    Juv8 = Juv8[Juv8['BIRTHDAY'] >= 19990000]

    Juv_0 = Juv1.append(Juv2, ignore_index=True)
    Juv_0 = Juv_0.append(Juv3, ignore_index=True)
    Juv_0 = Juv_0.append(Juv4, ignore_index=True)
    Juv_0 = Juv_0.append(Juv5, ignore_index=True)
    Juv_0 = Juv_0.append(Juv6, ignore_index=True)
    Juv_0 = Juv_0.append(Juv7, ignore_index=True)
    Juv_0 = Juv_0.append(Juv8, ignore_index=True)

    Juv_0 = Juv_0.drop(['timestamp'], axis=1)
    M = Juv_0['SITEID'].value_counts()
    dict_m = {'SITEID': M.index, 'cishu': M.values}
    df_m = pd.DataFrame(dict_m)
    N = pd.read_csv('..\\..\\processed_csv\\processed_one\\wangba.csv', sep=',', low_memory=False, header=0)
    direct_Juv = pd.merge(N, df_m, how='left', left_on=['SITEID'], right_on=['SITEID'])
    direct_Juv.fillna(0, inplace=True)
    direct_Juv['cishu'] = direct_Juv['cishu'].astype(int)
    direct_Juv = direct_Juv[direct_Juv['cishu'] != 0]
    direct_Juv = direct_Juv.drop(['Unnamed: 4'], axis=1)
    direct_Juv.to_csv('..\\..\\processed_csv\\processed_two\\DirectJuvTime.csv', index=0, sep=',')
    Juv_0.to_csv('..\\..\\processed_csv\\processed_two\\DirectJuvDetail.csv', index=0, sep=',')