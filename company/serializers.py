from rest_framework import serializers
from .models import *

class CompanySerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source="name")
    class Meta:
        model = CompanyName
        fields = ['company_name']

class CompanyRetrieveSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source="name")
    class Meta:
        model = CompanyName
        fields = ['company_name', 'tags']