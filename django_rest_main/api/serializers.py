from rest_framework import serializers
from students.models import student
from Employees.models import employee

class studentSerializer(serializers.ModelSerializer):
     class Meta:
          model=student
          fields="__all__"
     
class EmployeeSerializer(serializers.ModelSerializer):
     class Meta:
          model = employee
          fields="__all__"