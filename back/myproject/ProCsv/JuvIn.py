import pandas as pd
class JuvIn:
    JuvIn = pd.read_csv('..\\..\\processed_csv\\processed_two\\Juv_all.csv', sep=',', low_memory=False, header=0)
    JuvIn = JuvIn.drop(['lng', 'lat'], axis=1)
    JuvIn.to_csv('..\\..\\processed_csv\\processed_two\\JuvIn.csv', index=0, sep=',')
