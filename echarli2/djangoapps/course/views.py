from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin
from drf_haystack.generics import HaystackGenericAPIView

from .models import Course
from .serializers import CourseSerializer, CourseSearcherSerializer

class CourseSearchView(ListModelMixin, HaystackGenericAPIView):

    serializer_class = CourseSearcherSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
