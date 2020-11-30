import pandas as pd
class JuvNogeo:
    JuvNogeo = pd.read_csv('..\\..\\processed_csv\\processed_two\\Juv.csv', sep=',', low_memory=False, header=0)
    JuvNogeo = JuvNogeo[JuvNogeo['Juv'] > 0]
    JuvNogeo = JuvNogeo.drop(['lng', 'lat', 'JuvIn'], axis=1)
    #JuvNogeo = JuvNogeo.drop(676, axis=0)
    #print(JuvNogeo)
    JuvNogeo.to_csv('..\\..\\processed_csv\\processed_two\\JuvNogeo.csv', index=0, sep=',')