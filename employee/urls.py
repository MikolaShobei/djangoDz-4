from django.urls import path

from employee.views import ListEmployeeView

urlpatterns = [
    path('', ListEmployeeView.as_view())
]
