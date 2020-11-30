import pymongo
from django.http import HttpResponse,JsonResponse
from bson.json_util import dumps
from . import models
from . import serializers
from rest_framework_mongoengine import generics,viewsets
from rest_framework.response import Response
import json
import simplejson

class JuvRedListView(viewsets.ModelViewSet):
    def list(self, request, format=None):
        if request.method == 'GET':
            qs = models.JuvReddata.objects.all()
            data_list = []
            for i in qs:
                data = []
                data.append(i.SITEID)
                data.append(i.lng)
                data.append(i.lat)
                data.append(i.Juv)
                data_list.append(data)
            return JsonResponse(
                data_list, safe=False
            )
class JuvCountListView(viewsets.ModelViewSet):
    def list(self, request, format=None):
        if request.method == 'GET':
            data_list = []
            key = ['SITEID', 'TITLE', 'Juv_count']
            qs = models.JuvCountdata.objects.all().order_by('-Juv_count')
            for i in qs:
                data = []
                data.append(i.SITEID)
                data.append(i.TITLE)
                data.append(i.Juv_count)
                dic = dict(zip(key, data))

                data_list.append(dic)
            return JsonResponse(
                data_list, safe=False
            )

class JuvdetailListView(viewsets.ModelViewSet):
    def list(self, request, format=None):
        if request.method == 'GET':
            data_list = []
            key = ['SITEID', 'XB', 'CUSTOMERNAME', 'ONLINETIME', 'OFFLINETIME', 'AREAID', 'BIRTHDAY', 'timestamp']
            qs = models.Juvdetaildata.objects.all().order_by('-timestamp')
            for i in qs:
                data = []
                data.append(i.SITEID)
                data.append(i.XB)
                data.append(i.CUSTOMERNAME)
                data.append(i.ONLINETIME)
                data.append(i.OFFLINETIME)
                data.append(i.AREAID)
                data.append(i.BIRTHDAY)
                data.append(i.timestamp)
                dic = dict(zip(key, data))

                data_list.append(dic)
            return JsonResponse(
                data_list, safe=False
            )

class JuvBlueListView(viewsets.ModelViewSet):
    def list(self, request, format=None):
        if request.method == 'GET':
            qs = models.JuvBluedata.objects.all()
            data_list = []
            for i in qs:
                data = []
                data.append(i.SITEID)
                data.append(i.lng)
                data.append(i.lat)
                data.append(i.JuvIn)
                data_list.append(data)
            return JsonResponse(
                data_list, safe=False
            )
class ClickTimeListView(viewsets.ModelViewSet):

    def list(self, request, format=None):
        if request.method == 'POST':
            data_list = []
            req = simplejson.loads(request.body)
            for i in req:
                data = []
                for j in i:
                    va1 = []
                    va2 = []
                    qs1 = models.ClickTime18.objects.get(SITEID=j)
                    qs2 = models.ClickTimeOver18.objects.get(SITEID=j)

                    #print (j)
                    va1.append(qs1.clock0_1)
                    va1.append(qs1.clock1_2)
                    va1.append(qs1.clock2_3)
                    va1.append(qs1.clock3_4)
                    va1.append(qs1.clock4_5)
                    va1.append(qs1.clock5_6)
                    va1.append(qs1.clock6_7)
                    va1.append(qs1.clock7_8)
                    va1.append(qs1.clock8_9)
                    va1.append(qs1.clock9_10)
                    va1.append(qs1.clock10_11)
                    va1.append(qs1.clock11_12)
                    va1.append(qs1.clock12_13)
                    va1.append(qs1.clock13_14)
                    va1.append(qs1.clock14_15)
                    va1.append(qs1.clock15_16)
                    va1.append(qs1.clock16_17)
                    va1.append(qs1.clock17_18)
                    va1.append(qs1.clock18_19)
                    va1.append(qs1.clock19_20)
                    va1.append(qs1.clock20_21)
                    va1.append(qs1.clock21_22)
                    va1.append(qs1.clock22_23)
                    va1.append(qs1.clock23_0)
                    #data.append(va1)
                    va2.append(qs2.clock0_1)
                    va2.append(qs2.clock1_2)
                    va2.append(qs2.clock2_3)
                    va2.append(qs2.clock3_4)
                    va2.append(qs2.clock4_5)
                    va2.append(qs2.clock5_6)
                    va2.append(qs2.clock6_7)
                    va2.append(qs2.clock7_8)
                    va2.append(qs2.clock8_9)
                    va2.append(qs2.clock9_10)
                    va2.append(qs2.clock10_11)
                    va2.append(qs2.clock11_12)
                    va2.append(qs2.clock12_13)
                    va2.append(qs2.clock13_14)
                    va2.append(qs2.clock14_15)
                    va2.append(qs2.clock15_16)
                    va2.append(qs2.clock16_17)
                    va2.append(qs2.clock17_18)
                    va2.append(qs2.clock18_19)
                    va2.append(qs2.clock19_20)
                    va2.append(qs2.clock20_21)
                    va2.append(qs2.clock21_22)
                    va2.append(qs2.clock22_23)
                    va2.append(qs2.clock23_0)
                    data.append(va1)
                    data.append(va2)
                data_list.append(data)
            return JsonResponse(
                data_list, safe=False
            )
class AvgTimeListView(viewsets.ModelViewSet):
    def list(self, request, format=None):
        if request.method == 'GET':
            qs = models.AvgTimedata.objects.all()
            data_list = []
            for i in qs:
                data_list.append(i.clock0_1)
                data_list.append(i.clock1_2)
                data_list.append(i.clock2_3)
                data_list.append(i.clock3_4)
                data_list.append(i.clock4_5)
                data_list.append(i.clock5_6)
                data_list.append(i.clock6_7)
                data_list.append(i.clock7_8)
                data_list.append(i.clock8_9)
                data_list.append(i.clock9_10)
                data_list.append(i.clock10_11)
                data_list.append(i.clock11_12)
                data_list.append(i.clock12_13)
                data_list.append(i.clock13_14)
                data_list.append(i.clock14_15)
                data_list.append(i.clock15_16)
                data_list.append(i.clock16_17)
                data_list.append(i.clock17_18)
                data_list.append(i.clock18_19)
                data_list.append(i.clock19_20)
                data_list.append(i.clock20_21)
                data_list.append(i.clock21_22)
                data_list.append(i.clock22_23)
                data_list.append(i.clock23_0)

            return JsonResponse(
                data_list, safe=False
            )
class AvgDayTimeListView(viewsets.ModelViewSet):
    def list(self, request, format=None):
        if request.method == 'GET':
            qs = models.AvgDayTimedata.objects.all()
            data_list = []
            for i in qs:
                data = []
                data.append(i.Date)
                data.append(i.ONLINETIME)
                data_list.append(data)
            return JsonResponse(
                data_list, safe=False
            )

class AgeTimeNumListView(viewsets.ModelViewSet):
    def list(self, request, format=None):
        if request.method == 'GET':
            qs = models.AgeTimeNumdata.objects.all()
            data_list = []
            for i in qs:
                data = []
                data.append(i.TIME)
                data.append(i.NUM)
                data.append(i.AGE)
                data_list.append(data)
            return JsonResponse(
                data_list, safe=False
            )

class ApiAllListView(viewsets.ModelViewSet):
    queryset = models.ApiAlldata.objects.all()
    serializer_class = serializers.ApiAllSerializer

class DetailView(viewsets.ModelViewSet):
    def list(self, request, format=None):
        if request.method == 'POST':
            data_list = []
            key = ['SITEID','lng','lat','Under_age','UnnormalAge','OvertimeOnNet','ExternalPeople','MidnightOnNet',
               'Online17_18','age18_44','age45_52','age53_68']
            req = simplejson.loads(request.body)
            for i in req:
                data = []
                for j in i:
                    va = []
                    qs = models.detaildata.objects.get(SITEID=j)
                    va.append(qs.SITEID)
                    va.append(qs.lng)
                    va.append(qs.lat)
                    va.append(qs.Under_age)
                    va.append(qs.UnnormalAge)
                    va.append(qs.OvertimeOnNet)
                    va.append(qs.ExternalPeople)
                    va.append(qs.MidnightOnNet)
                    va.append(qs.Online17_18)
                    va.append(qs.age18_44)
                    va.append(qs.age45_52)
                    va.append(qs.age53_68)
                    dic = dict(zip(key, va))
                    data.append(dic)
                data_list.append(data)
            return JsonResponse(
                data_list, safe=False
            )