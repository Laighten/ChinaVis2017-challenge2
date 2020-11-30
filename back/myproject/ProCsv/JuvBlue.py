import pandas as pd

class JuvBlue:
    JuvBlue = pd.read_csv('..\\..\\processed_csv\\processed_two\\IndirectJuvTime.csv', sep=',', low_memory=False, header=0)
    JuvBlue = JuvBlue.drop(['TITLE'], axis=1)
    #JuvNogeo = JuvNogeo.drop(676, axis=0)
    JuvBlue.to_csv('..\\..\\processed_csv\\processed_two\\JuvBlue.csv', index=0, sep=',')