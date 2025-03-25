from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'phone_number', 'email']  # Add or remove fields as needed


class LoginTokenObtain(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(LoginTokenObtain, cls).get_token(user)
        token['username'] = user.username
        return token