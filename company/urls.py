from django.urls import path, include
from .views import CompanyListCreateView, CompanyDetailView

urlpatterns = [
    path('companies/', CompanyListCreateView.as_view(), name='companies list'),
    path('companies/<int:pk>/', CompanyDetailView.as_view(), name='companies detail'),
]