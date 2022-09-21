from rest_framework.routers import DefaultRouter

from core import viewset

router = DefaultRouter()
router.register('employee', viewset.EmployeeViewSet)
router.register('department', viewset.DepartmentViewSet)

urlpatterns = router.urls
