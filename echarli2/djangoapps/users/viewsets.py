# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserSerializer, UserSearchSerializer

class UserViewSet(viewsets.ModelViewSet):
    """API endpoint that allows items to be viewed or edited."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # Se obtiene de forma automática la funcionalidad de:
    # .create()
    # .update()
    # .list()
    # .delete()
    # .retrive()

class UserSearchViewSet(viewsets.ReadOnlyModelViewSet):
        """API endpoint that allows items to be viewed or edited."""
        queryset = User.objects.all()
        serializer_class = UserSearchSerializer
        permission_classes = [AllowAny]

        # Se obtiene de forma automática la funcionalidad de:
        # .create()
        # .update()
        # .list()
        # .delete()
        # .retrive()
