import email
from rest_framework import serializers
from .models import CustomUser,Item
from rest_framework_simplejwt.tokens import RefreshToken


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','username', 'email','password','full_name','age','gender', 'is_active', 'is_staff')

    def create(self, validated_data):
        password = validated_data.pop('password')
        username = validated_data.pop('username')
        user = CustomUser.objects.create_user(username=username, **validated_data)
        user.set_password(password)
        user.save()
        return user

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('key', 'value')

