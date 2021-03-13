from django.urls import path

from employee.views import ListEmployeeView, RetrieveUpdateDestroyEmployeeView

urlpatterns = [
    path('', ListEmployeeView.as_view(), name='list_employee'),
    path('/<int:pk>', RetrieveUpdateDestroyEmployeeView.as_view(), name='retrieve_update_destroy_employee')
]
