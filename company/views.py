from rest_framework.generics import ListAPIView, CreateAPIView, get_object_or_404, RetrieveUpdateDestroyAPIView

from company.models import CompanyModel
from company.serializers import CompanySerializer
from employee.serializers import EmployeeSerializer


class ListCompanyView(ListAPIView):
    serializer_class = CompanySerializer

    def get_queryset(self):
        qs = CompanyModel.objects.all()
        city = self.request.query_params.get('city')
        if city:
            qs = qs.filter(city__iexact=city)
        return qs


class EmployeeCreateView(CreateAPIView):
    serializer_class = EmployeeSerializer

    def perform_create(self, serializer):
        company_id = self.kwargs.get('pk')
        company = get_object_or_404(CompanyModel, pk=company_id)
        serializer.save(company=company)


class RetrieveUpdateDeleteCompanyView(RetrieveUpdateDestroyAPIView):
    queryset = CompanyModel.objects.all()
    serializer_class = CompanySerializer
