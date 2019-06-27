from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from employee.models import Employee
from employee.serializers import EmployeeSerializer


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsAdminUser,)


class EmployeeRetrieveDestroy(generics.RetrieveDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsAdminUser,)
    lookup_field = 'email'

