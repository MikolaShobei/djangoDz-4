from django.urls import path

from users.views import ListUserCreateView, CompanyCreateView

urlpatterns = [
    path('', ListUserCreateView.as_view()),
    path('<int:pk>/company', CompanyCreateView.as_view())
]
