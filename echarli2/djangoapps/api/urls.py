from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .routers import router
from course import views

urlpatterns = [
    url(r'^', include(router.urls)),
]
