from .models import Employee
from rest_framework import viewsets
from rest_framework import permissions
from employee.serializers import EmployeeSerializer
class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Employee to be viewed or edited.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # permission_classes = [permissions.IsAuthenticated]