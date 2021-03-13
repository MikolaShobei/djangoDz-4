from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from employee.models import EmployeeModel
from employee.serializers import EmployeeSerializer


class ListEmployeeView(ListAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer


class RetrieveUpdateDestroyEmployeeView(RetrieveUpdateDestroyAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer
