from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.fields import ReadOnlyField
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,
                                     required=True,)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_staff']

    def create(self, validated_data):
        validated_data['password'] = make_password(
            validated_data.get('password'))
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data['password'] = make_password(
            validated_data.get('password'))
        return super().update(instance, validated_data)
