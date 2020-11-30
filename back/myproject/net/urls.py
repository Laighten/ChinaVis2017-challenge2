from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls import url 
from .views import *

urlpatterns = [
    #直接接纳未成年的网吧
    path('JuvRed', JuvRedListView.as_view({'get': 'list'}), name='JuvRed'),
    #间接接纳未成年人的网吧
    path('JuvBlue', JuvBlueListView.as_view({'get': 'list'}),name='JuvBlue'),
    #详细界面间接接纳未成年人详情
    path('Juvdetail', JuvdetailListView.as_view({'get': 'list'}), name='Juvdetail'),
    #详细界面的网吧违法次数
    path('JuvCount', JuvCountListView.as_view({'get': 'list'}), name='JuvCount'),
    path('ClickTime', ClickTimeListView.as_view({'post': 'list'}), name='ClickTime'),
    path('AvgTime', AvgTimeListView.as_view({'get': 'list'}), name='AvgTime'),
    path('AvgDayTime', AvgDayTimeListView.as_view({'get': 'list'}), name='AvgDayTime'),
    path('AgeTimeNum', AgeTimeNumListView.as_view({'get': 'list'}), name='AgeTimeNum'),
    path('ApiAll', ApiAllListView.as_view({'get': 'list'}), name='ApiAll'),
    path('detail', DetailView.as_view({'post': 'list'}), name='raw_data1'),
]
