from rest_framework import serializers

class LoginResponseSerializer(serializers.Serializer):
    status = serializers.CharField()
    description = serializers.CharField()
    username = serializers.CharField()
    scope = serializers.CharField()
