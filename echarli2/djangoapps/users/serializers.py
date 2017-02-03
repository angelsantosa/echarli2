from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    """User Serializer"""
    class Meta:
        model = User
        fields = ('id','first_name','last_name')

class UserSearchSerializer(serializers.ModelSerializer):
    """User Serializer"""
    class Meta:
        model = User
        fields = ('id','first_name','last_name')

class UserDetailsSerializer(serializers.ModelSerializer):

    """
    User model w/o password
    """
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'lang_key')
        read_only_fields = ('email', )
