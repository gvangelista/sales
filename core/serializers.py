from rest_framework import serializers
from core import models


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Employee
        fields = '__all__'
