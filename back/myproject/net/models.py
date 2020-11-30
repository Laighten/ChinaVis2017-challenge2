from __future__ import unicode_literals
from django.db import models
from mongoengine import *
# Create your models here.

connect('MyData', host='127.0.0.1', port=27017)

class JuvReddata(Document):
    SITEID = IntField(max_length=45)
    lng = IntField(max_length=45)
    lat = IntField(max_length=45)
    Juv = IntField(max_length=45)
    meta = {'collection': 'JuvRed'}

class Juvdetaildata(Document):
    SITEID = IntField(max_length=45)
    XB = StringField(max_length=45)
    CUSTOMERNAME = StringField(max_length=45)
    ONLINETIME = IntField(max_length=45)
    OFFLINETIME = IntField(max_length=45)
    AREAID = IntField(max_length=45)
    BIRTHDAY = IntField(max_length=45)
    timestamp = IntField(max_length=45)
    meta = {'collection': 'Juvdetail'}


class JuvCountdata(Document):
    SITEID = IntField(max_length=45)
    TITLE = StringField(max_length=45)
    Juv_count = IntField(max_length=45)
    meta = {'collection': 'JuvCount'}

class JuvBluedata(Document):
    SITEID = IntField(max_length=45)
    lng = IntField(max_length=45)
    lat = IntField(max_length=45)
    JuvIn = IntField(max_length=45)
    meta = {'collection': 'JuvBlue'}

class ClickTime18(Document):
    SITEID = IntField(max_length=45)
    clock0_1 = IntField(max_length=45)
    clock1_2 = IntField(max_length=45)
    clock2_3 = IntField(max_length=45)
    clock3_4 = IntField(max_length=45)
    clock4_5 = IntField(max_length=45)
    clock5_6 = IntField(max_length=45)
    clock6_7 = IntField(max_length=45)
    clock7_8 = IntField(max_length=45)
    clock8_9 = IntField(max_length=45)
    clock9_10 = IntField(max_length=45)
    clock10_11 = IntField(max_length=45)
    clock11_12 = IntField(max_length=45)
    clock12_13 = IntField(max_length=45)
    clock13_14 = IntField(max_length=45)
    clock14_15 = IntField(max_length=45)
    clock15_16 = IntField(max_length=45)
    clock16_17 = IntField(max_length=45)
    clock17_18 = IntField(max_length=45)
    clock18_19 = IntField(max_length=45)
    clock19_20 = IntField(max_length=45)
    clock20_21 = IntField(max_length=45)
    clock21_22 = IntField(max_length=45)
    clock22_23 = IntField(max_length=45)
    clock23_0 = IntField(max_length=45)
    meta = {'collection': 'ClickTime18'}

class ClickTimeOver18(Document):
    SITEID = IntField(max_length=45)
    clock0_1 = IntField(max_length=45)
    clock1_2 = IntField(max_length=45)
    clock2_3 = IntField(max_length=45)
    clock3_4 = IntField(max_length=45)
    clock4_5 = IntField(max_length=45)
    clock5_6 = IntField(max_length=45)
    clock6_7 = IntField(max_length=45)
    clock7_8 = IntField(max_length=45)
    clock8_9 = IntField(max_length=45)
    clock9_10 = IntField(max_length=45)
    clock10_11 = IntField(max_length=45)
    clock11_12 = IntField(max_length=45)
    clock12_13 = IntField(max_length=45)
    clock13_14 = IntField(max_length=45)
    clock14_15 = IntField(max_length=45)
    clock15_16 = IntField(max_length=45)
    clock16_17 = IntField(max_length=45)
    clock17_18 = IntField(max_length=45)
    clock18_19 = IntField(max_length=45)
    clock19_20 = IntField(max_length=45)
    clock20_21 = IntField(max_length=45)
    clock21_22 = IntField(max_length=45)
    clock22_23 = IntField(max_length=45)
    clock23_0 = IntField(max_length=45)
    meta = {'collection': 'ClickTimeOver18'}

class AvgTimedata(Document):
    clock0_1 = IntField(max_length=45)
    clock1_2 = IntField(max_length=45)
    clock2_3 = IntField(max_length=45)
    clock3_4 = IntField(max_length=45)
    clock4_5 = IntField(max_length=45)
    clock5_6 = IntField(max_length=45)
    clock6_7 = IntField(max_length=45)
    clock7_8 = IntField(max_length=45)
    clock8_9 = IntField(max_length=45)
    clock9_10 = IntField(max_length=45)
    clock10_11 = IntField(max_length=45)
    clock11_12 = IntField(max_length=45)
    clock12_13 = IntField(max_length=45)
    clock13_14 = IntField(max_length=45)
    clock14_15 = IntField(max_length=45)
    clock15_16 = IntField(max_length=45)
    clock16_17 = IntField(max_length=45)
    clock17_18 = IntField(max_length=45)
    clock18_19 = IntField(max_length=45)
    clock19_20 = IntField(max_length=45)
    clock20_21 = IntField(max_length=45)
    clock21_22 = IntField(max_length=45)
    clock22_23 = IntField(max_length=45)
    clock23_0 = IntField(max_length=45)
    meta = {'collection': 'AvgTime'}

class AvgDayTimedata(Document):
    Date = StringField(max_length=45)
    ONLINETIME = IntField(max_length=45)

    meta = {'collection': 'AvgDayTime'}


class AgeTimeNumdata(Document):
    TIME = IntField(max_length=45)
    NUM = IntField(max_length=45)
    AGE = IntField(max_length=45)

    meta = {'collection': 'AgeTimeNum'}

class ApiAlldata(Document):
    SITEID = IntField(max_length=45)
    lng = FloatField(max_length=45)
    lat = FloatField(max_length=45)
    meta = {'collection': 'ApiAll'}

class detaildata(Document):
    SITEID = IntField(max_length=45)
    lng = FloatField(max_length=45)
    lat = FloatField(max_length=45)
    Under_age = IntField(max_length=45)
    UnnormalAge = IntField(max_length=45)
    OvertimeOnNet = IntField(max_length=45)
    ExternalPeople = IntField(max_length=45)
    MidnightOnNet = IntField(max_length=45)
    Online17_18 = IntField(max_length=45)
    age18_44 = IntField(max_length=45)
    age45_52 = IntField(max_length=45)
    age53_68 = IntField(max_length=45)
    meta = {'collection': 'geo_data'}