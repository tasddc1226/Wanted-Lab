from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            'id',
            'company_ko',
            'company_en',
            'company_ja',
            'tag_ko',
            'tag_en',
            'tag_ja'
        ]