from django.urls import path, include
from .views import CompanyListCreateView, CompanySearchView, CompanyRUDView

urlpatterns = [
    path('', CompanyListCreateView.as_view(), name='companies list'),
    path('search/', CompanySearchView.as_view(), name='search company'),
    path('<str:name>/', CompanyRUDView.as_view(), name='company retrieve'),
]