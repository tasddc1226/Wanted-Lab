from django.urls import path, include
from .views import CompanyListCreateView, CompanyDetailView, CompanySearchView

urlpatterns = [
    path('companies/', CompanyListCreateView.as_view(), name='companies list'),
    path('companies/<int:pk>/', CompanyDetailView.as_view(), name='companies detail'),
    path('companies/search/', CompanySearchView.as_view(), name='search company'),
]