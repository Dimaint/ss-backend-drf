from employee.models import Employee
from rest_framework import serializers


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ['last_name', 'first_name', 'phone']