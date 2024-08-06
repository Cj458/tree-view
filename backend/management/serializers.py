from rest_framework import serializers
from .models import Department, Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'full_name', 'position', 'date_of_employment', 'salary', 'department']


class DepartmentSerializer(serializers.ModelSerializer):
    # employees = EmployeeSerializer(many=True, read_only=True)
    children = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = ['id', 'name', 'children']

    # def get_employees(self, obj):
    #     employees = obj.employees.all()[:10]  # Limit to 10 employees
    #     return EmployeeSerializer(employees, many=True).data

    def get_children(self, obj):
        children = Department.objects.filter(parent=obj).select_related().prefetch_related('employees')
        return DepartmentSerializer(children, many=True).data

