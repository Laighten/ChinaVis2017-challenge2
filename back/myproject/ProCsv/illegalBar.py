import pandas as pd

#筛选出直接接纳未成年人上网的网吧和利用成年人身份证间接接纳未成年人上网
class juveniles:
    hydata = pd.read_csv('..\\..\\processed_csv\\processed_two\\DirectJuvDetail.csv', sep=',', low_memory=False, header=0)

    hydata3 = pd.read_csv('..\\..\\processed_csv\\processed_two\\IndirectJuvDetail.csv', sep=',', low_memory=False, header=0)
    hydata3 = hydata3.drop(0, axis=0)
    wangba = pd.read_csv('..\\..\\processed_csv\\processed_one\\wangba.csv', sep=',', low_memory=False, header=0)
    wangba = wangba.drop(['Unnamed: 4'], axis=1)
    young = hydata

    #将每个网吧的未成年人上网人数追加到每个网吧后面
    num = young['SITEID'].value_counts()
    dict_m = {'SITEID': num.index, 'Juv': num.values}
    df_m = pd.DataFrame(dict_m)
    merged_Juv = pd.merge(wangba, df_m, how='left', left_on=['SITEID'], right_on=['SITEID'])
    merged_Juv.fillna(0, inplace=True)
    merged_Juv[['Juv']] = merged_Juv[['Juv']].astype(int)

    #将间接接纳未成年上网的网吧统计出来
    num2 = hydata3['SITEID'] .value_counts()
    dict_m = {'SITEID': num2.index, 'JuvIn': num2.values}
    df_m = pd.DataFrame(dict_m)
    merged_JuvIn = pd.merge(merged_Juv, df_m, how='left', left_on=['SITEID'], right_on=['SITEID'])
    merged_JuvIn.fillna(0, inplace=True)
    merged_JuvIn[['JuvIn']] = merged_JuvIn[['JuvIn']].astype(int)
    merged_JuvIn = merged_JuvIn[merged_JuvIn['JuvIn'] >= 5]
    # In = {'SITEID':None,'TITLE':None,'lng':None,'lat':None,'Juv':None,'JuvIn':None}
    # In = pd.DataFrame(In, index=[0])
    # for i in range(0,len(merged_JuvIn)):
    #     line = merged_JuvIn.loc[i]
    #     if line['Juv'] != 0 | line['JuvIn'] >= 5:
    #         In = In.append(line, ignore_index=True)
    merged_JuvIn = merged_JuvIn.drop(0, axis=0)
    Juv_1 = merged_JuvIn
    Juv_1['Juv_count'] = Juv_1['Juv'] + Juv_1['JuvIn']
    Juv_1 = Juv_1.drop(['JuvIn', 'Juv'], axis=1)
    Juv_1 = Juv_1[Juv_1['Juv_count'] > 0]
    Juv_1.to_csv('..\\..\\processed_csv\\processed_two\\Juv_all.csv', index=0, sep=',')
    merged_JuvIn = merged_JuvIn.drop(['Juv_count'], axis=1)
    merged_JuvIn.to_csv('..\\..\\processed_csv\\processed_two\\Juv.csv', index=0, sep=',')
