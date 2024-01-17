from rest_framework import serializers
from .classes import RegisterUserRequest

class AuthorizingResponseSerializer(serializers.Serializer):
    status = serializers.CharField()
    description = serializers.CharField()
    username = serializers.CharField()
    scope = serializers.CharField()

class RegisterUserRequestSerializer(serializers.Serializer):
    username = serializers.CharField(max_length = 30)
    password = serializers.CharField(min_length = 8)
    scope = serializers.CharField()
    is_superuser = serializers.CharField(max_length=1,min_length = 1)

    def create(self, validated_data):
        return RegisterUserRequest(**validated_data)
    
class RegisterUserResponseSerializer(serializers.Serializer):
    code = serializers.CharField()
    message = serializers.CharField()
