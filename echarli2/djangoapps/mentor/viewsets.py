# -*- coding: utf-8 -*-
from rest_framework import viewsets

from .models import Mentor
from .serializers import MentorSerializer

class MentorViewSet(viewsets.ModelViewSet):
    """API endpoint that allows items to be viewed or edited."""
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer

    # Se obtiene de forma automática la funcionalidad de:
    # .create()
    # .update()
    # .list()
    # .delete()
    # .retrive()