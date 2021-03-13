from rest_framework.generics import ListAPIView

from employee.models import EmployeeModel
from employee.serializers import EmployeeSerializer


class ListEmployeeView(ListAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer
