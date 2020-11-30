import pandas as pd

class DataClear_count:
    Juv1 = pd.read_csv('..\\..\\processed_csv\\processed_one\\hydata_1.csv', sep=',', low_memory=False, header=0)
    Juv1 = Juv1.drop(['PERSONID'],axis=1)


    Juv2 = pd.read_csv('..\\..\\processed_csv\\processed_one\\hydata_2.csv', sep=',', low_memory=False, header=0)
    Juv2 = Juv2.drop(['PERSONID'], axis=1)


    Juv3 = pd.read_csv('..\\..\\processed_csv\\processed_one\\hydata_3.csv', sep=',', low_memory=False, header=0)
    Juv3 = Juv3.drop(['PERSONID'], axis=1)

    Juv4 = pd.read_csv('..\\..\\processed_csv\\processed_one\\hydata_4.csv', sep=',', low_memory=False, header=0)
    Juv4 = Juv4.drop(['PERSONID'], axis=1)


    Juv5 = pd.read_csv('..\\..\\processed_csv\\processed_one\\hydata_5.csv', sep=',', low_memory=False, header=0)
    Juv5 = Juv5.drop(['PERSONID'], axis=1)


    Juv6 = pd.read_csv('..\\..\\processed_csv\\processed_one\\hydata_6.csv', sep=',', low_memory=False, header=0)
    Juv6 = Juv6.drop(['PERSONID'], axis=1)


    Juv7 = pd.read_csv('..\\..\\processed_csv\\processed_one\\hydata_7.csv', sep=',', low_memory=False, header=0)
    Juv7 = Juv7.drop(['PERSONID'], axis=1)


    Juv8 = pd.read_csv('..\\..\\processed_csv\\processed_one\\hydata_8.csv', sep=',', low_memory=False, header=0)
    Juv8 = Juv8.drop(['PERSONID'], axis=1)


    Juv_0 = Juv1.append(Juv2, ignore_index=True)
    Juv_0 = Juv_0.append(Juv3, ignore_index=True)
    Juv_0 = Juv_0.append(Juv4, ignore_index=True)
    Juv_0 = Juv_0.append(Juv5, ignore_index=True)
    Juv_0 = Juv_0.append(Juv6, ignore_index=True)
    Juv_0 = Juv_0.append(Juv7, ignore_index=True)
    Juv_0 = Juv_0.append(Juv8, ignore_index=True)

    #Juv_0 = Juv_0.drop(['timestamp'], axis=1)
    Juv_0.to_csv('..\\..\\processed_csv\\processed_two\\hydata_count.csv', index=0, sep=',')