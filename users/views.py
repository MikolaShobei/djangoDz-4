from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model

from users.serializers import UserSerializer

UserModel = get_user_model()


class ListUserCreate(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
