# -*- coding: utf-8 -*-
from rest_framework import routers
from users.viewsets import UserViewSet, UserSearchViewSet
from mentor.viewsets import MentorViewSet
from course.viewsets import CourseViewSet, CourseSearchView

# Routers proporcionan una forma sencilla y automática para determinar
# la configuración de URLs
router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'mentor', MentorViewSet)
router.register(r'course', CourseViewSet)
router.register(r'_search/course', CourseSearchView, base_name="course-search")
router.register(r'_search/user', UserSearchViewSet)
