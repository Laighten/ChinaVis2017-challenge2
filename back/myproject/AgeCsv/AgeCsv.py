import pandas as pd

class AgeCsv:
    hydata = pd.read_csv('..\\..\\processed_csv\\processed_two\\hydata_count.csv', sep=',', low_memory=False, header=0)
    hydata['BIRTHDAY'] = hydata['BIRTHDAY'].astype(int)
    age18 = hydata[hydata['BIRTHDAY'] >= 19980000]
    age18 = len(age18)
    hydata = hydata[hydata['BIRTHDAY'] < 19980000]
    age18_30 = hydata[hydata['BIRTHDAY'] >= 19860000]
    age18_30 = len(age18_30)
    hydata = hydata[hydata['BIRTHDAY'] < 19860000]
    age30_40 = hydata[hydata['BIRTHDAY'] >= 19760000]
    age30_40 = len(age30_40)
    hydata = hydata[hydata['BIRTHDAY'] < 19760000]
    age40_60 = hydata[hydata['BIRTHDAY'] >= 19560000]
    age40_60 = len(age40_60)
    age60 = hydata[hydata['BIRTHDAY'] < 19560000]
    age60 = len(age60)

    print(age18, age18_30, age30_40, age40_60, age60)