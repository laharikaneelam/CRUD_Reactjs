from myapp.viewsets import employeeList
from rest_framework import routers

router=routers.DefaultRouter()
router.register('employee',employeeList)
