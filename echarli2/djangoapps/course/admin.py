from django.contrib import admin
from .models import Course, CourseResource, CourseSchedule

# Register your models here or die :)

admin.site.register(Course)
admin.site.register(CourseResource)
admin.site.register(CourseSchedule)
