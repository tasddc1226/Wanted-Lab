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
from .models import *
from django.db.models import Q

class CompanyListCreateView(ListCreateAPIView):
    queryset = CompanyName.objects.all()
    serializer_class = CompanySerializer

class CompanySearchView(ListAPIView):
    # resp = api.get("/search?query=링크", headers=[("x-wanted-language", "ko")])
    def get(self, request):
        try:
            queryset = CompanyName.objects.all()

            query = request.GET.get('query', '')
            language = request.headers['x-wanted-language']
            print(query, language)
            searched_companies = []

            # check language code is available
            code = Language.objects.filter(code=language).values()[0]
            if not code:
                # TODO: 존재하지 않는 language 예외 처리
                pass
            
            company = CompanyName.objects.filter(name__icontains=query)
            
            q = Q()
            for obj in company:
                q |= Q(company_id=obj.company_id)
            company_queryset = queryset.filter(q)
            
            results = company_queryset.filter(code=code['id'])
            for company in results:
                if not (company.name == ""):
                    searched_companies.append({"company_name": company.name})

            return JsonResponse({'searched_companies': searched_companies}, status=200)
        except Exception as error:
            return JsonResponse({'error': error}, status=400)
            

class CompanyDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer