import pandas as pd

class Juvdetail:
    Juvdetail = pd.read_csv('..\\..\\processed_csv\\processed_two\\IndirectJuvDetail.csv', sep=',', low_memory=False, header=0)
    Juvdetail['AREAID'] = Juvdetail['AREAID'].astype(int)
    Juvdetail['BIRTHDAY'] = Juvdetail['BIRTHDAY'].astype(int)
    #Juvdetail = Juvdetail[Juvdetail['timestamp'] > 432000]
    Juvdetail['timestamp'] = Juvdetail['timestamp'] / 86400
    Juvdetail['timestamp'] = Juvdetail['timestamp'].astype(int)
    Juvdetail = Juvdetail[Juvdetail['timestamp'] > 3]
    Juvdetail = Juvdetail[Juvdetail['timestamp'] <= 90]
    Juvdetail.to_csv('..\\..\\processed_csv\\processed_two\\Juvdetail.csv', index=0, sep=',')
