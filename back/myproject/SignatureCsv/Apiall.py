import pandas as pd

class ApiAll:
    data1 = pd.read_csv('..\\..\\processed_csv\\processed_two\\JuvNoname.csv', sep=',', low_memory=False, header=0)
    data2 = pd.read_csv('..\\..\\processed_csv\\processed_two\\JuvIn.csv', sep=',', low_memory=False, header=0)
    data2['Juv'] = data2['JuvIn']
    data2 = data2.drop(['JuvIn'], axis=1)
    ApiAll = data1.append(data2, ignore_index=True)
    ApiAll = ApiAll.drop(['Juv'], axis=1)
    ApiAll = ApiAll.drop_duplicates(subset=['SITEID'], keep='first')
    ApiAll.to_csv('..\\..\\processed_csv\\processed_two\\ApiAll.csv', index=0, sep=',')
    #print(ApiAll)
    # data3 = ApiAll.groupby(by='SITEID')['Juv'].sum()
    # data3 = pd.DataFrame(data3)
    # data4 = pd.merge(ApiAll, data3, how='left', left_on=['SITEID'], right_on=['SITEID'])
    # data4 = data4.drop(['Juv_x'],axis=1)
    # data = data4.drop_duplicates(subset=['SITEID', 'lng', 'lat', 'Juv_y'], keep='first')