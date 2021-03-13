from django.urls import path

from users.views import ListUserCreateView, CompanyCreateView, RetrieveUpdateDestroyUserView

urlpatterns = [
    path('', ListUserCreateView.as_view(), name='list_create_user'),
    path('/<int:pk>/company', CompanyCreateView.as_view(), name='create_company'),
    path('/<int:pk>', RetrieveUpdateDestroyUserView.as_view(), name='retrieve_Update_destroy_user')
]
