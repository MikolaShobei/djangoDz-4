from rest_framework.generics import ListCreateAPIView, CreateAPIView, get_object_or_404
from django.contrib.auth import get_user_model

from company.serializers import CompanySerializer
from users.serializers import UserSerializer

UserModel = get_user_model()


class ListUserCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class CompanyCreateView(CreateAPIView):
    serializer_class = CompanySerializer

    def perform_create(self, serializer):
        user_id = self.kwargs.get('pk')
        user = get_object_or_404(UserModel, pk=user_id)
        serializer.save(user=user)
