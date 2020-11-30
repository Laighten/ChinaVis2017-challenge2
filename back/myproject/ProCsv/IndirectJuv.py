import pandas as pd

class Bianli:
    hydata = pd.read_csv('..\\..\\processed_csv\\processed_one\\hydata_8.csv', sep=',', low_memory=False, header=0)
    hydata = hydata.drop(['PERSONID'], axis=1)
    hydata_In = hydata
    In = {'SITEID': None, 'XB': None, 'CUSTOMERNAME': None, 'ONLINETIME': None,'OFFLINETIME': None,'AREAID': None, 'BIRTHDAY': None, 'timestamp': None }
    In = pd.DataFrame(In, index=[0])
    for i in range(0, len(hydata_In)):
        line = hydata_In.loc[i]
        #print(line['timestamp'])
        if line['timestamp'] >= 86400:
            In = In.append(line, ignore_index=True)
        elif line['timestamp'] >= 57600:
            #In = In.append(line, ignore_index=True)
            if line['BIRTHDAY'] < 19660000:
                In = In.append(line, ignore_index=True)
                #hydata_In = hydata_In.drop(i, axis=0)
    In.to_csv('..\\..\\processed_csv\\processed_one\\IndirectJuvDetail_8.csv', index=0, sep=',')
