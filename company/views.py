from rest_framework.generics import ListAPIView, CreateAPIView, get_object_or_404

from company.models import CompanyModel
from company.serializers import CompanySerializer
from employee.serializers import EmployeeSerializer


class LIstCompanyView(ListAPIView):
    required = CompanyModel.objects.all()
    serializer_class = CompanySerializer


class EmployeeCreateView(CreateAPIView):
    serializer_class = EmployeeSerializer

    def perform_create(self, serializer):
        company_id = self.kwargs.get('pk')
        company = get_object_or_404(CompanyModel, pk=company_id)
        serializer.save(company=company)
