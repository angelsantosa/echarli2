from rest_framework import serializers

from .models import Mentor

class MentorSerializer(serializers.ModelSerializer):
    """Mentor Serializer"""
    class Meta:
        model = Mentor
        fields = ('__all__')
        