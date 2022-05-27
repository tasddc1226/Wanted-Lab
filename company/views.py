from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView
)

from .serializers import (
    CompanyRetrieveSerializer,
    CompanySerializer,
    CompanyCreateSerializer
)
from .models import *
import json

class CompanyListCreateView(ListCreateAPIView):
    """
    [새로운 회사 등록]
        - header의 x-wanted-language 언어값에 따라 등록된 회사를 해당 언어로 출력

    endpoint url : api/v1/companies/
    method : POST
    header : ko(x-wanted-language)
    """
    queryset = CompanyName.objects.all()
    serializer_class = CompanyRetrieveSerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        language = self.request.headers['x-wanted-language']

        tmp = queryset.order_by('-id').first()
        obj = queryset.filter(company_id=tmp.company_id, code__code=language).first()
        return obj

    def post(self, request):
        body = json.loads(request.body.decode('utf-8'))
        company = Company.objects.create()

        for code, value in body.items():
            print(code, value)
            value['company'] = company
            value['code'], _ = Language.objects.get_or_create(code=code)
            CompanyName.objects.create(**value)
        
        obj = self.get_object()
        serializer = self.get_serializer(obj)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CompanySearchView(ListAPIView):
    """
    [회사명 자동완성]
        - 회사명의 일부만 들어가도 검색 가능
        - header의 x-wanted-language 언어값에 따라 해당 언어로 출력
    
    endpoint url : api/v1/companies/search/
    method : GET
    input query : 링크
    header : ko(x-wanted-language)
    """
    queryset = CompanyName.objects.all()
    serializer_class = CompanySerializer
    
    def get(self, request):
        query = request.GET.get('query', '')
        language = request.headers['x-wanted-language']
        
        # search company name using input query
        objs = CompanyName.objects.filter(name__icontains=query)
        
        # filter by language
        objs = objs.filter(code__code=language)
        serializer = self.get_serializer(objs, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)


class CompanyRUDView(RetrieveUpdateDestroyAPIView):
    """
    [회사 이름으로 회사 검색]
        - header의 x-wanted-language 언어값에 따라 해당 언어로 출력

    endpoint url : api/v1/companies/<str:name>/
    method : GET
    header : ko(x-wanted-language)
    """
    queryset = CompanyName.objects.all()
    serializer_class = CompanyRetrieveSerializer
    lookup_field = 'name'

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        name = self.kwargs[self.lookup_field]
        language = self.request.headers['x-wanted-language']

        tmp = queryset.filter(name=name).first()
        if tmp is None:
            return None
        obj = queryset.filter(company_id=tmp.company_id, code__code=language).first()
        return obj

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(obj)

        serializer_data = serializer.data
        serializer_data['tags'] = serializer_data['tags'].split('|')
        return Response(serializer_data, status=status.HTTP_200_OK)