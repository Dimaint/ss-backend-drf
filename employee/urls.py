from rest_framework import routers
from .views import EmployeeViewSet

router = routers.DefaultRouter()
router.register(r'employee', EmployeeViewSet)

urlpatterns = router.urls