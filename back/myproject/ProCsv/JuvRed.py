import pandas as pd

class JuvRed:
    JuvRed = pd.read_csv('..\\..\\processed_csv\\processed_two\\DirectJuvTime.csv', sep=',', low_memory=False, header=0)
    JuvRed = JuvRed.drop(['TITLE'], axis=1)
    #JuvNogeo = JuvNogeo.drop(676, axis=0)
    JuvRed.to_csv('..\\..\\processed_csv\\processed_two\\JuvRed.csv', index=0, sep=',')