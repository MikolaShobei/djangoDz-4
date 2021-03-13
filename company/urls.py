from django.urls import path

from .views import ListCompanyView, EmployeeCreateView, RetrieveUpdateDeleteCompanyView

urlpatterns = [
    path('', ListCompanyView.as_view(), name='company_list'),
    path('/<int:pk>/employee', EmployeeCreateView.as_view(), name='create_employee'),
    path('/<int:pk>', RetrieveUpdateDeleteCompanyView.as_view(), name='retrieve_update_delete_company')

]
