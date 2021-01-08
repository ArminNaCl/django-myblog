from rest_framework.viewsets import ModelViewSet
from .serializers  import UserSerializer
from django.contrib.auth import get_user_model
User =get_user_model()


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()