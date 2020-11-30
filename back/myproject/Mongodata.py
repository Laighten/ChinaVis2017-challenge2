from pymongo import MongoClient
from myproject.settings import DBCONFIG
import csv

class JuvCount:
    filename = 'JuvCount.csv'
    path = '..\\processed_csv\\processed_two\\'
    JuvCount = 'JuvCount'
    colname = ['SITEID', 'TITLE', 'Juv_count']
    res = []
    max_len = 100000
    i = 1

    def __init__(self):
        self.files = []
        self.files.append(self.filename)
        self.client = MongoClient(DBCONFIG['HOST'], DBCONFIG['PORT'])
        self.db = self.client.__getattr__(DBCONFIG['NAME'])
        self.dst_JuvCount = self.db[self.JuvCount]

    def __del__(self):
        self.client.close()

    @staticmethod
    def convert_fileaffix(fileaffix):
        if len(fileaffix) == 0:
            return ''
        while fileaffix[0] == '.':
            fileaffix = fileaffix[1:]
        if '.' in fileaffix:
            return None
        else:
            return fileaffix

    def Juvdata(self):
        self.dst_JuvCount.remove({})
        self.res.clear()
        print('正在处理文件：%s' % (self.path + self.filename))
        with open(self.path + self.filename, 'r', encoding='UTF-8') as infile:
                reader = csv.reader(infile)
                next(reader)
                for row in reader:
                    self.res.append({
                        'SITEID': int(row[0]),
                        'TITLE': str(row[1]),
                        'Juv_count': float(row[2]),
                    })
                    if self.res.__len__() == self.max_len:
                        self.dst_JuvCount.insert_many(self.res)
                        self.res.clear()
        if self.res.__len__() > 0:
            self.dst_JuvCount.insert_many(self.res)
            self.res.clear()
class JuvRed:
    filename = 'JuvRed.csv'
    path = '..\\processed_csv\\processed_two\\'
    JuvRed = 'JuvRed'
    colname = ['SITEID', 'lng', 'lat', 'Juv']
    res = []
    max_len = 100000
    i = 1

    def __init__(self):
        self.files = []
        self.files.append(self.filename)
        self.client = MongoClient(DBCONFIG['HOST'], DBCONFIG['PORT'])
        self.db = self.client.__getattr__(DBCONFIG['NAME'])
        self.dst_JuvRed = self.db[self.JuvRed]

    def __del__(self):
        self.client.close()

    @staticmethod
    def convert_fileaffix(fileaffix):
        if len(fileaffix) == 0:
            return ''
        while fileaffix[0] == '.':
            fileaffix = fileaffix[1:]
        if '.' in fileaffix:
            return None
        else:
            return fileaffix

    def JuvNo(self):
        self.dst_JuvRed.remove({})
        self.res.clear()
        print('正在处理文件：%s' % (self.path + self.filename))
        with open(self.path + self.filename, 'r', encoding='UTF-8') as infile:
            reader = csv.reader(infile)
            next(reader)
            for row in reader:
                self.res.append({
                    'SITEID': int(row[0]),
                    'lng': row[1],
                    'lat': row[2],
                    'Juv':int(row[3]),
                })
                if self.res.__len__() == self.max_len:
                    self.dst_JuvRed.insert_many(self.res)
                    self.res.clear()
        if self.res.__len__() > 0:
            self.dst_JuvRed.insert_many(self.res)
            self.res.clear()
class JuvBlue:
    filename = 'JuvBlue.csv'
    path = '..\\processed_csv\\processed_two\\'
    JuvBlue = 'JuvBlue'
    colname = ['SITEID', 'lng', 'lat', 'JuvIn']
    res = []
    max_len = 100000
    i = 1

    def __init__(self):
        self.files = []
        self.files.append(self.filename)
        self.client = MongoClient(DBCONFIG['HOST'], DBCONFIG['PORT'])
        self.db = self.client.__getattr__(DBCONFIG['NAME'])
        self.dst_JuvBlue = self.db[self.JuvBlue]

    def __del__(self):
        self.client.close()

    @staticmethod
    def convert_fileaffix(fileaffix):
        if len(fileaffix) == 0:
            return ''
        while fileaffix[0] == '.':
            fileaffix = fileaffix[1:]
        if '.' in fileaffix:
            return None
        else:
            return fileaffix

    def JuvInf(self):
        self.dst_JuvBlue.remove({})
        self.res.clear()
        print('正在处理文件：%s' % (self.path + self.filename))
        with open(self.path + self.filename, 'r', encoding='UTF-8') as infile:
            reader = csv.reader(infile)
            next(reader)
            for row in reader:
                self.res.append({
                    'SITEID': int(row[0]),
                    'lng': row[1],
                    'lat': row[2],
                    'JuvIn': int(row[3]),
                })
                if self.res.__len__() == self.max_len:
                    self.dst_JuvBlue.insert_many(self.res)
                    self.res.clear()
        if self.res.__len__() > 0:
            self.dst_JuvBlue.insert_many(self.res)
            self.res.clear()
class ClickTime18:
    filename = 'ClickTime18.csv'
    path = '..\\processed_csv\\processed_two\\'
    ClickTime18 = 'ClickTime18'
    colname = ['SITEID', 'clock0_1', 'clock1_2', 'clock2_3', 'clock3_4', 'clock4_5', 'clock5_6', 'clock6_7',
               'clock7_8', 'clock8_9', 'clock9_10','clock10_11', 'clock11_12', 'clock12_13', 'clock13_14',
               'clock14_15', 'clock15_16', 'clock16_17', 'clock17_18', 'clock18_19', 'clock19_20', 'clock20_21'
               , 'clock21_22', 'clock22_23', 'clock23_0']
    res = []
    max_len = 100000
    i = 1

    def __init__(self):
        self.files = []
        self.files.append(self.filename)
        self.client = MongoClient(DBCONFIG['HOST'], DBCONFIG['PORT'])
        self.db = self.client.__getattr__(DBCONFIG['NAME'])
        self.dst_ClickTime18 = self.db[self.ClickTime18]

    def __del__(self):
        self.client.close()

    @staticmethod
    def convert_fileaffix(fileaffix):
        if len(fileaffix) == 0:
            return ''
        while fileaffix[0] == '.':
            fileaffix = fileaffix[1:]
        if '.' in fileaffix:
            return None
        else:
            return fileaffix

    def Time18(self):
        self.dst_ClickTime18.remove({})
        self.res.clear()
        print('正在处理文件：%s' % (self.path + self.filename))
        with open(self.path + self.filename, 'r', encoding='UTF-8') as infile:
            reader = csv.reader(infile)
            next(reader)
            for row in reader:
                self.res.append({
                    'SITEID': int(row[0]),
                    'clock0_1': int(row[1]),
                    'clock1_2': int(row[2]),
                    'clock2_3': int(row[3]),
                    'clock3_4': int(row[4]),
                    'clock4_5': int(row[5]),
                    'clock5_6': int(row[6]),
                    'clock6_7': int(row[7]),
                    'clock7_8': int(row[8]),
                    'clock8_9': int(row[9]),
                    'clock9_10': int(row[10]),
                    'clock10_11': int(row[11]),
                    'clock11_12': int(row[12]),
                    'clock12_13': int(row[13]),
                    'clock13_14': int(row[14]),
                    'clock14_15': int(row[15]),
                    'clock15_16': int(row[16]),
                    'clock16_17': int(row[17]),
                    'clock17_18': int(row[18]),
                    'clock18_19': int(row[19]),
                    'clock19_20': int(row[20]),
                    'clock20_21': int(row[21]),
                    'clock21_22': int(row[22]),
                    'clock22_23': int(row[23]),
                    'clock23_0': int(row[24]),
                })
                if self.res.__len__() == self.max_len:
                    self.dst_ClickTime18.insert_many(self.res)
                    self.res.clear()
        if self.res.__len__() > 0:
            self.dst_ClickTime18.insert_many(self.res)
            self.res.clear()

class ClickTimeOver18:
    filename = 'ClickTimeOver18.csv'
    path = '..\\processed_csv\\processed_two\\'
    ClickTimeOver18 = 'ClickTimeOver18'
    colname = ['SITEID', 'clock0_1', 'clock1_2', 'clock2_3', 'clock3_4', 'clock4_5', 'clock5_6', 'clock6_7',
               'clock7_8', 'clock8_9', 'clock9_10','clock10_11', 'clock11_12', 'clock12_13', 'clock13_14',
               'clock14_15', 'clock15_16', 'clock16_17', 'clock17_18', 'clock18_19', 'clock19_20', 'clock20_21'
               , 'clock21_22', 'clock22_23', 'clock23_0']
    res = []
    max_len = 100000
    i = 1

    def __init__(self):
        self.files = []
        self.files.append(self.filename)
        self.client = MongoClient(DBCONFIG['HOST'], DBCONFIG['PORT'])
        self.db = self.client.__getattr__(DBCONFIG['NAME'])
        self.dst_ClickTimeOver18 = self.db[self.ClickTimeOver18]

    def __del__(self):
        self.client.close()

    @staticmethod
    def convert_fileaffix(fileaffix):
        if len(fileaffix) == 0:
            return ''
        while fileaffix[0] == '.':
            fileaffix = fileaffix[1:]
        if '.' in fileaffix:
            return None
        else:
            return fileaffix

    def TimeOver18(self):
        self.dst_ClickTimeOver18.remove({})
        self.res.clear()
        print('正在处理文件：%s' % (self.path + self.filename))
        with open(self.path + self.filename, 'r', encoding='UTF-8') as infile:
            reader = csv.reader(infile)
            next(reader)
            for row in reader:
                self.res.append({
                    'SITEID': int(row[0]),
                    'clock0_1': int(row[1]),
                    'clock1_2': int(row[2]),
                    'clock2_3': int(row[3]),
                    'clock3_4': int(row[4]),
                    'clock4_5': int(row[5]),
                    'clock5_6': int(row[6]),
                    'clock6_7': int(row[7]),
                    'clock7_8': int(row[8]),
                    'clock8_9': int(row[9]),
                    'clock9_10': int(row[10]),
                    'clock10_11': int(row[11]),
                    'clock11_12': int(row[12]),
                    'clock12_13': int(row[13]),
                    'clock13_14': int(row[14]),
                    'clock14_15': int(row[15]),
                    'clock15_16': int(row[16]),
                    'clock16_17': int(row[17]),
                    'clock17_18': int(row[18]),
                    'clock18_19': int(row[19]),
                    'clock19_20': int(row[20]),
                    'clock20_21': int(row[21]),
                    'clock21_22': int(row[22]),
                    'clock22_23': int(row[23]),
                    'clock23_0': int(row[24]),
                })
                if self.res.__len__() == self.max_len:
                    self.dst_ClickTimeOver18.insert_many(self.res)
                    self.res.clear()
        if self.res.__len__() > 0:
            self.dst_ClickTimeOver18.insert_many(self.res)
            self.res.clear()

class AvgTime:
    filename = 'AvgTime.csv'
    path = '..\\processed_csv\\processed_two\\'
    AvgTime = 'AvgTime'
    colname = [ 'clock0_1', 'clock1_2', 'clock2_3', 'clock3_4', 'clock4_5', 'clock5_6', 'clock6_7',
               'clock7_8', 'clock8_9', 'clock9_10','clock10_11', 'clock11_12', 'clock12_13', 'clock13_14',
               'clock14_15', 'clock15_16', 'clock16_17', 'clock17_18', 'clock18_19', 'clock19_20', 'clock20_21'
               , 'clock21_22', 'clock22_23', 'clock23_0']
    res = []
    max_len = 100000
    i = 1

    def __init__(self):
        self.files = []
        self.files.append(self.filename)
        self.client = MongoClient(DBCONFIG['HOST'], DBCONFIG['PORT'])
        self.db = self.client.__getattr__(DBCONFIG['NAME'])
        self.dst_AvgTime = self.db[self.AvgTime]

    def __del__(self):
        self.client.close()

    @staticmethod
    def convert_fileaffix(fileaffix):
        if len(fileaffix) == 0:
            return ''
        while fileaffix[0] == '.':
            fileaffix = fileaffix[1:]
        if '.' in fileaffix:
            return None
        else:
            return fileaffix

    def Atime(self):
        self.dst_AvgTime.remove({})
        self.res.clear()
        print('正在处理文件：%s' % (self.path + self.filename))
        with open(self.path + self.filename, 'r', encoding='UTF-8') as infile:
            reader = csv.reader(infile)
            next(reader)
            for row in reader:
                self.res.append({
                    'clock0_1': row[0],
                    'clock1_2': row[1],
                    'clock2_3': row[2],
                    'clock3_4': row[3],
                    'clock4_5': row[4],
                    'clock5_6': row[5],
                    'clock6_7': row[6],
                    'clock7_8': row[7],
                    'clock8_9': row[8],
                    'clock9_10': row[9],
                    'clock10_11': row[10],
                    'clock11_12': row[11],
                    'clock12_13': row[12],
                    'clock13_14': row[13],
                    'clock14_15': row[14],
                    'clock15_16': row[15],
                    'clock16_17': row[16],
                    'clock17_18': row[17],
                    'clock18_19': row[18],
                    'clock19_20': row[19],
                    'clock20_21': row[20],
                    'clock21_22': row[21],
                    'clock22_23': row[22],
                    'clock23_0': row[23],
                })
                if self.res.__len__() == self.max_len:
                    self.dst_AvgTime.insert_many(self.res)
                    self.res.clear()
        if self.res.__len__() > 0:
            self.dst_AvgTime.insert_many(self.res)
            self.res.clear()

class AvgDayTime:
    filename = 'AvgDayTime.csv'
    path = '..\\processed_csv\\processed_two\\'
    AvgDayTime = 'AvgDayTime'
    colname = ['Date', 'ONLINETIME']
    res = []
    max_len = 100000
    i = 1

    def __init__(self):
        self.files = []
        self.files.append(self.filename)
        self.client = MongoClient(DBCONFIG['HOST'], DBCONFIG['PORT'])
        self.db = self.client.__getattr__(DBCONFIG['NAME'])
        self.dst_AvgDayTime = self.db[self.AvgDayTime]

    def __del__(self):
        self.client.close()

    @staticmethod
    def convert_fileaffix(fileaffix):
        if len(fileaffix) == 0:
            return ''
        while fileaffix[0] == '.':
            fileaffix = fileaffix[1:]
        if '.' in fileaffix:
            return None
        else:
            return fileaffix

    def ADtime(self):
        self.dst_AvgDayTime.remove({})
        self.res.clear()
        print('正在处理文件：%s' % (self.path + self.filename))
        with open(self.path + self.filename, 'r', encoding='UTF-8') as infile:
            reader = csv.reader(infile)
            next(reader)
            for row in reader:
                self.res.append({
                    'Date': row[0],
                    'ONLINETIME': row[1],
                })
                if self.res.__len__() == self.max_len:
                    self.dst_AvgDayTime.insert_many(self.res)
                    self.res.clear()
        if self.res.__len__() > 0:
            self.dst_AvgDayTime.insert_many(self.res)
            self.res.clear()

class AgeTimeNum:
    filename = 'AgeTimeNum.csv'
    path = '..\\processed_csv\\processed_two\\'
    AgeTimeNum = 'AgeTimeNum'
    colname = ['TIME','NUM','AGE']
    res = []
    max_len = 100000
    i = 1

    def __init__(self):
        self.files = []
        self.files.append(self.filename)
        self.client = MongoClient(DBCONFIG['HOST'], DBCONFIG['PORT'])
        self.db = self.client.__getattr__(DBCONFIG['NAME'])
        self.dst_AgeTimeNum = self.db[self.AgeTimeNum]

    def __del__(self):
        self.client.close()

    @staticmethod
    def convert_fileaffix(fileaffix):
        if len(fileaffix) == 0:
            return ''
        while fileaffix[0] == '.':
            fileaffix = fileaffix[1:]
        if '.' in fileaffix:
            return None
        else:
            return fileaffix

    def ATN(self):
        self.dst_AgeTimeNum.remove({})
        self.res.clear()
        print('正在处理文件：%s' % (self.path + self.filename))
        with open(self.path + self.filename, 'r', encoding='UTF-8') as infile:
            reader = csv.reader(infile)
            next(reader)
            for row in reader:
                self.res.append({
                    'TIME': int(row[0]),
                    'NUM': int(row[1]),
                    'AGE': int (row[2]),

                })
                if self.res.__len__() == self.max_len:
                    self.dst_AgeTimeNum.insert_many(self.res)
                    self.res.clear()
        if self.res.__len__() > 0:
            self.dst_AgeTimeNum.insert_many(self.res)
            self.res.clear()

class Juvdetail:
    filename = 'Juvdetail.csv'
    path = '..\\processed_csv\\processed_two\\'
    Juvdetail = 'Juvdetail'
    colname = ['SITEID', 'XB', 'CUSTOMERNAME', 'ONLINETIME', 'OFFLINETIME', 'AREAID', 'BIRTHDAY', 'timestamp']
    res = []
    max_len = 100000
    i = 1

    def __init__(self):
        self.files = []
        self.files.append(self.filename)
        self.client = MongoClient(DBCONFIG['HOST'], DBCONFIG['PORT'])
        self.db = self.client.__getattr__(DBCONFIG['NAME'])
        self.dst_Juvdetail = self.db[self.Juvdetail]

    def __del__(self):
        self.client.close()

    @staticmethod
    def convert_fileaffix(fileaffix):
        if len(fileaffix) == 0:
            return ''
        while fileaffix[0] == '.':
            fileaffix = fileaffix[1:]
        if '.' in fileaffix:
            return None
        else:
            return fileaffix

    def Detail(self):
        self.dst_Juvdetail.remove({})
        self.res.clear()
        print('正在处理文件：%s' % (self.path + self.filename))
        with open(self.path + self.filename, 'r', encoding='UTF-8') as infile:
            reader = csv.reader(infile)
            next(reader)
            for row in reader:
                self.res.append({
                    'SITEID': row[0],
                    'XB': row[1],
                    'CUSTOMERNAME': row[2],
                    'ONLINETIME': row[3],
                    'OFFLINETIME': row[4],
                    'AREAID': row[5],
                    'BIRTHDAY': row[6],
                    'timestamp': int(row[7]),
                })
                if self.res.__len__() == self.max_len:
                    self.dst_Juvdetail.insert_many(self.res)
                    self.res.clear()
        if self.res.__len__() > 0:
            self.dst_Juvdetail.insert_many(self.res)
            self.res.clear()

class ApiAll:
    filename = 'ApiAll.csv'
    path = '..\\processed_csv\\processed_two\\'
    ApiAll = 'ApiAll'
    colname = ['SITEID', 'lng', 'lat']
    res = []
    max_len = 100000
    i = 1

    def __init__(self):
        self.files = []
        self.files.append(self.filename)
        self.client = MongoClient(DBCONFIG['HOST'], DBCONFIG['PORT'])
        self.db = self.client.__getattr__(DBCONFIG['NAME'])
        self.dst_ApiAll = self.db[self.ApiAll]

    def __del__(self):
        self.client.close()

    @staticmethod
    def convert_fileaffix(fileaffix):
        if len(fileaffix) == 0:
            return ''
        while fileaffix[0] == '.':
            fileaffix = fileaffix[1:]
        if '.' in fileaffix:
            return None
        else:
            return fileaffix

    def All(self):
        self.dst_ApiAll.remove({})
        self.res.clear()
        print('正在处理文件：%s' % (self.path + self.filename))
        with open(self.path + self.filename, 'r', encoding='UTF-8') as infile:
            reader = csv.reader(infile)
            next(reader)
            for row in reader:
                self.res.append({
                    'SITEID': int(row[0]),
                    'lng': row[1],
                    'lat': row[2],

                })
                if self.res.__len__() == self.max_len:
                    self.dst_ApiAll.insert_many(self.res)
                    self.res.clear()
        if self.res.__len__() > 0:
            self.dst_ApiAll.insert_many(self.res)
            self.res.clear()

class geo_data:
    filename = 'GeoTime.csv'
    path = '..\\processed_csv\\processed_two\\'
    c_raw1 = 'geo_data'
    colname = ['SITEID','lng','lat','Under_age','UnnormalAge','OvertimeOnNet','ExternalPeople','MidnightOnNet',
               'Online17_18','age18_44','age45_52','age53_68']
    res = []
    max_len = 100000
    i = 1

    def __init__(self):
        self.files = []
        self.files.append(self.filename)
        self.client = MongoClient(DBCONFIG['HOST'], DBCONFIG['PORT'])
        self.db = self.client.__getattr__(DBCONFIG['NAME'])
        self.dst_raw1 = self.db[self.c_raw1]

    def __del__(self):
        self.client.close()

    def data_geo(self):
        self.dst_raw1.remove({})
        self.res.clear()
        print('正在处理文件：%s' % (self.path + self.filename))
        with open(self.path + self.filename, 'r', encoding='UTF-8') as infile:
                reader = csv.reader(infile)
                next(reader)
                for row in reader:
                    self.res.append({
                        '_id': self.i,
                        'SITEID': int(row[0]),
                        'lng': float(row[1])if row[1] != '' and row[1].find('N/A') == -1 else None,
                        'lat': float(row[2])if row[2] != '' and row[2].find('N/A') == -1 else None,
                        'Under_age': int(row[3]),
                        'UnnormalAge': int(row[4]),
                        'OvertimeOnNet': int(row[5]),
                        'ExternalPeople': int(row[6]),
                        'MidnightOnNet': int(row[7]),
                        'Online17_18': int(row[8]),
                        'age18_44': int(row[9]),
                        'age45_52': int(row[10]),
                        'age53_68': int(row[11]),

                    })
                    self.i = self.i+1
                    if self.res.__len__() == self.max_len:
                        self.dst_raw1.insert_many(self.res)
                        self.res.clear()
        if self.res.__len__() > 0:
            self.dst_raw1.insert_many(self.res)
            self.res.clear()
