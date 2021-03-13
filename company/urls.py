from django.urls import path

from .views import LIstCompanyView, EmployeeCreateView

urlpatterns = [
    path('', LIstCompanyView.as_view()),
    path('<int:pk>/employee', EmployeeCreateView.as_view())
]
