from rest_framework import viewsets

from .models import Department, Employee
from .serializers import DepartmentSerializer, EmployeeSerializer
from .pagination import DefaultPagination

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.select_related().prefetch_related('children')
    serializer_class = DepartmentSerializer
    pagination_class = DefaultPagination
    ordering_fields = ['name']
    

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = DefaultPagination
    ordering_fields = ['date_of_employment', 'department']


class DepartmentEmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    pagination_class = DefaultPagination

    def get_queryset(self):
        department_id = self.kwargs.get('department_id')
        return Employee.objects.filter(department_id=department_id)