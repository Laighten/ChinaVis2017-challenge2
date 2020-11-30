import pandas as pd
import time

class Scatterplot:
    da = pd.read_csv('..\\..\\processed_csv\\processed_one\\hydata_8.csv', sep=',', low_memory=False, header=0)

    hydata = da.drop(['PERSONID'], axis=1)
    hydata[['ONLINETIME']] = hydata[['ONLINETIME']].astype(str)
    hydata[['OFFLINETIME']] = hydata[['OFFLINETIME']].astype(str)
    timestamp1 = hydata['ONLINETIME'].apply(lambda x: time.mktime(time.strptime(x, '%Y%m%d%H%M%S')))
    timestamp2 = hydata['OFFLINETIME'].apply(lambda x: time.mktime(time.strptime(x, '%Y%m%d%H%M%S')))
    hydata['timestamp'] = timestamp2 - timestamp1

    hydata = hydata.drop(['SITEID', 'XB', 'CUSTOMERNAME','ONLINETIME','OFFLINETIME' ,'AREAID'], axis=1)

    AgeTimeNum1 = pd.DataFrame({'AGE': '', 'TIME': '', 'NUM': ''}, index=[0])
    AgeTimeNum = pd.DataFrame({'AGE': '', 'TIME': '', 'NUM': '' }, index=[0])

    AgeTimeNum['AGE'] = 12
    hydata = hydata[hydata['BIRTHDAY'] < 20031100]
    age12 = hydata[hydata['BIRTHDAY'] >= 20021100]
    length = len(age12)
    AgeTimeNum['NUM'] = length
    age12 = (age12['timestamp'].sum()) / length
    AgeTimeNum['TIME'] = age12
    AgeTimeNum1 = AgeTimeNum1.append(AgeTimeNum, ignore_index=True)

    AgeTimeNum['AGE'] = 16
    hydata = hydata[hydata['BIRTHDAY'] < 19991100]
    age16 = hydata[hydata['BIRTHDAY'] >= 19981100]
    length = len(age16)
    AgeTimeNum['NUM'] = length
    age16 = (age16['timestamp'].sum()) / length
    AgeTimeNum['TIME'] = age16
    AgeTimeNum1 = AgeTimeNum1.append(AgeTimeNum, ignore_index=True)

    #print(AgeTimeNum)
    AgeTimeNum['AGE'] = 20
    hydata = hydata[hydata['BIRTHDAY'] < 19961100]
    age20 = hydata[hydata['BIRTHDAY'] >= 19951100]
    length = len(age20)
    AgeTimeNum['NUM'] = length
    age20 = (age20['timestamp'].sum()) / length
    AgeTimeNum['TIME'] = age20
    AgeTimeNum1 = AgeTimeNum1.append(AgeTimeNum, ignore_index=True)


    AgeTimeNum['AGE'] = 24
    hydata = hydata[hydata['BIRTHDAY'] < 19921100]
    age24 = hydata[hydata['BIRTHDAY'] >= 19911100]
    length = len(age24)
    AgeTimeNum['NUM'] = length
    age24 = (age24['timestamp'].sum()) / length
    AgeTimeNum['TIME'] = age24
    AgeTimeNum1 =AgeTimeNum1.append(AgeTimeNum, ignore_index=True)

    AgeTimeNum['AGE'] = 28
    hydata = hydata[hydata['BIRTHDAY'] < 19881100]
    age28 = hydata[hydata['BIRTHDAY'] >= 19871100]
    length = len(age28)
    AgeTimeNum['NUM'] = length
    age28 = (age28['timestamp'].sum()) / length
    AgeTimeNum['TIME'] = age28
    AgeTimeNum1 =AgeTimeNum1.append(AgeTimeNum, ignore_index=True)

    AgeTimeNum['AGE'] = 32
    hydata = hydata[hydata['BIRTHDAY'] < 19841100]
    age32 = hydata[hydata['BIRTHDAY'] >= 19831100]
    length = len(age32)
    AgeTimeNum['NUM'] = length
    age32 = (age32['timestamp'].sum()) / length
    AgeTimeNum['TIME'] = age32
    AgeTimeNum1 =AgeTimeNum1.append(AgeTimeNum, ignore_index=True)

    AgeTimeNum['AGE'] = 36
    hydata = hydata[hydata['BIRTHDAY'] < 19801100]
    age36 = hydata[hydata['BIRTHDAY'] >= 19791100]
    length = len(age36)
    AgeTimeNum['NUM'] = length
    age36 = (age36['timestamp'].sum()) / length
    AgeTimeNum['TIME'] = age36
    AgeTimeNum1 =AgeTimeNum1.append(AgeTimeNum, ignore_index=True)

    AgeTimeNum['AGE'] = 40
    hydata = hydata[hydata['BIRTHDAY'] < 19761100]
    age40 = hydata[hydata['BIRTHDAY'] >= 19751100]
    length = len(age40)
    AgeTimeNum['NUM'] = length
    age40 = (age40['timestamp'].sum()) / length
    AgeTimeNum['TIME'] = age40
    AgeTimeNum1 =AgeTimeNum1.append(AgeTimeNum, ignore_index=True)

    AgeTimeNum['AGE'] = 44
    hydata = hydata[hydata['BIRTHDAY'] < 19721100]
    age44 = hydata[hydata['BIRTHDAY'] >= 19711100]
    length = len(age44)
    AgeTimeNum['NUM'] = length
    age44 = (age44['timestamp'].sum()) / length
    AgeTimeNum['TIME'] = age44
    AgeTimeNum1 = AgeTimeNum1.append(AgeTimeNum, ignore_index=True)

    AgeTimeNum['AGE'] = 48
    hydata = hydata[hydata['BIRTHDAY'] < 19681100]
    age48 = hydata[hydata['BIRTHDAY'] >= 19671100]
    length = len(age48)
    AgeTimeNum['NUM'] = length
    age48 = (age48['timestamp'].sum()) / length
    AgeTimeNum['TIME'] = age48
    AgeTimeNum1 = AgeTimeNum1.append(AgeTimeNum, ignore_index=True)

    AgeTimeNum['AGE'] = 52
    hydata = hydata[hydata['BIRTHDAY'] < 19641100]
    age52 = hydata[hydata['BIRTHDAY'] >= 19631100]
    length = len(age52)
    AgeTimeNum['NUM'] = length
    age52 = (age52['timestamp'].sum()) / length
    AgeTimeNum['TIME'] = age52
    AgeTimeNum1 = AgeTimeNum1.append(AgeTimeNum, ignore_index=True)

    AgeTimeNum['AGE'] = 56
    hydata = hydata[hydata['BIRTHDAY'] < 19601100]
    age56 = hydata[hydata['BIRTHDAY'] >= 19591100]
    length = len(age56)
    AgeTimeNum['NUM'] = length
    age56 = (age56['timestamp'].sum()) / length
    AgeTimeNum['TIME'] = age56
    AgeTimeNum1 = AgeTimeNum1.append(AgeTimeNum, ignore_index=True)

    AgeTimeNum['AGE'] = 60
    hydata = hydata[hydata['BIRTHDAY'] < 19561100]
    age60 = hydata[hydata['BIRTHDAY'] >= 19551100]
    length = len(age60)
    AgeTimeNum['NUM'] = length
    age60 = (age60['timestamp'].sum()) / length
    AgeTimeNum['TIME'] = age60
    AgeTimeNum1 = AgeTimeNum1.append(AgeTimeNum, ignore_index=True)

    AgeTimeNum1 = AgeTimeNum1.drop(0, axis=0)
    #AgeTimeNum1['TIME'] = AgeTimeNum1['TIME'].astype(int)
    c = AgeTimeNum1['TIME']
    b = c / 60
    AgeTimeNum1['TIME'] = b.astype(int)

    AgeTimeNum1.to_csv('..\\..\\processed_csv\\processed_one\\AgeTimeNum8.csv', index=0, sep=',')


