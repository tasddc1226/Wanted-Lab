from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import filters
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from .serializers import CompanySerializer
from .models import Company

class CompanyListCreateView(ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    search_fields = ['company_ko']
    filter_backends = [filters.SearchFilter]

    def filter_queryset(self, queryset):
        """
        Given a queryset, filter it with whichever filter backend is in use.

        You are unlikely to want to override this method, although you may need
        to call it either from a list view, or from a custom `get_object`
        method if you want to apply the configured filtering backend to the
        default queryset.
        """
        print("this is override func!")
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        if not queryset:
            raise ObjectDoesNotExist
        return queryset


class CompanyDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer