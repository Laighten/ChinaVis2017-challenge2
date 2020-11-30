from rest_framework_mongoengine import serializers
from mongoengine import *
from . import models

class JuvRedSerializer(serializers.DocumentSerializer):
    class Meta:
        model = models.JuvReddata
        fields = '__all__'

class JuvBlueSerializer(serializers.DocumentSerializer):
    class Meta:
        model = models.JuvBluedata
        fields = '__all__'

class JuvdetailSerializer(serializers.DocumentSerializer):
    class Meta:
        model = models.Juvdetaildata
        fields = '__all__'

class JuvCountSerializer(serializers.DocumentSerializer):
    class Meta:
        model = models.JuvCountdata
        fields = '__all__'

class ClickTime18Serializer(serializers.DocumentSerializer):
    class Meta:
        model = models.ClickTime18
        fields = '__all__'

class ClickTimeOver18Serializer(serializers.DocumentSerializer):
    class Meta:
        model = models.ClickTimeOver18
        fields = '__all__'

class AvgTimeSerializer(serializers.DocumentSerializer):
    class Meta:
        model = models.AvgTimedata
        fields = '__all__'

class AvgDayTimeSerializer(serializers.DocumentSerializer):
    class Meta:
        model = models.AvgDayTimedata
        fields = '__all__'

class ApiAllSerializer(serializers.DocumentSerializer):
    class Meta:
        model = models.ApiAlldata
        fields = ('SITEID', 'lng', 'lat')

class detailSerializer(serializers.DocumentSerializer):
    class Meta:
        model = models.detaildata
        fields = ('SITEID', 'NumOnNet', 'NumOnNet_OverTen', 'UnnormalAge', 'Under_age',
                  'OvertimeOnNet', 'ExternalPeople', 'MidnightOnNet', 'age18_35', 'age35_68')

