from rest_framework import exceptions
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

            # check search query string
            query = request.GET.get('query', '')
            if len(query) == 0:
                raise ValueError

            # check language code is available
            language = request.headers['x-wanted-language']
            code = Language.objects.filter(code=language).values()[0]

            searched_companies = []
            
            # search company name using input query
            company = CompanyName.objects.filter(name__icontains=query)
            
            q = Q()
            for obj in company:
                q |= Q(company_id=obj.company_id)
            company_queryset = queryset.filter(q)
            
            # filter by language code_id
            results = company_queryset.filter(code=code['id'])
            for company in results:
                if not (company.name == ""):
                    searched_companies.append({"company_name": company.name})

            return JsonResponse({'searched_companies': searched_companies}, status=200)
        except ValueError:
            raise exceptions.ParseError("Empty Query")
        except IndexError:
            raise exceptions.ParseError("Unsupported Language")
        except Exception as error:
            return exceptions.ParseError(error)
            

class CompanyDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer