from rest_framework.routers import DefaultRouter
from .views import DepartmentEmployeeViewSet, DepartmentViewSet, EmployeeViewSet

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'departments/(?P<department_id>\d+)/employees', DepartmentEmployeeViewSet, basename='department-employees')

router.register(r'employees', EmployeeViewSet)


urlpatterns = router.urls
