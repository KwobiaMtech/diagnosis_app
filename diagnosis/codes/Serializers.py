from rest_framework import serializers
from codes.models import Codes, ICD


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
