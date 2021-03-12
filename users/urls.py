from django.urls import path

from users.views import ListUserCreate

urlpatterns = [
    path('', ListUserCreate.as_view())
]
