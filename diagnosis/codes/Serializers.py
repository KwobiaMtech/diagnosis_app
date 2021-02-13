from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Codes, ICD


class SaveCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Codes
        fields = ['id', 'created', 'category_code', 'diagnosis_code', 'full_code', 'ab_description',
                  'full_description',
                  'category_title', 'ICD']


class GetCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Codes
        fields = ['id', 'created', 'category_code', 'diagnosis_code', 'full_code', 'ab_description',
                  'full_description',
                  'category_title']


class ICDSerializer(serializers.ModelSerializer):
    class Meta:
        model = ICD
        fields = ['id', 'name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
