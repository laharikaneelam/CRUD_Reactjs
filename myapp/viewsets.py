from rest_framework import viewsets
from . import models
from . import serializers

class employeeList(viewsets.ModelViewSet):
    queryset=models.employees.objects.all()
    serializer_class=serializers.employeeSerializer
