from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import filters
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView
)
from .serializers import CompanySerializer
from .models import Company

class CompanyListCreateView(ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanySearchView(ListAPIView):
    # resp = api.get("/search?query=링크", headers=[("x-wanted-language", "ko")])
    def get(self, request):
        try:
            query = request.GET.get('query', '')
            language = request.headers['x-wanted-language']
            searched_companies = []

            company_ko = Company.objects.filter(company_ko__icontains=query).exists()
            
            if language == 'ko' and company_ko:
                companies = Company.objects.filter(company_ko__icontains=query)
                for company in companies:
                    searched_companies.append({
                        'company_name' : company.company_ko
                    })


            return JsonResponse({'searched_companies': searched_companies}, status=200)
        except Exception as error:
            return JsonResponse({'error': error}, status=400)

class CompanyDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer