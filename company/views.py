from rest_framework import exceptions
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
    queryset = CompanyName.objects.all()
    serializer_class = CompanyCreateSerializer

    def post(self, request):
        body = json.loads(request.body.decode('utf-8'))
        company = Company.objects.create()

        for code, value in body.items():
            print(code, value)
            value['company'] = company
            value['code'], _ = Language.objects.get_or_create(code=code)
            CompanyName.objects.create(**value)
        
        # TODO: 생성 후 요청된 헤더 언어값에 따라 리턴하기
        return Response(status=status.HTTP_201_CREATED)


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
        code = Language.objects.filter(code=language).values()[0]
        
        # search company name using input query
        objs = CompanyName.objects.filter(name__icontains=query)
        
        # filter by language code_id
        objs = objs.filter(code=code['id'])
        serializer = CompanySerializer(objs, many=True)

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
        # TODO: 없는 회사에 대한 404 예외처리
        queryset = self.filter_queryset(self.get_queryset())
        name = self.kwargs[self.lookup_field]
        language = self.request.headers['x-wanted-language']
        code = Language.objects.filter(code=language).values()[0]

        tmp = queryset.filter(name=name).first()
        obj = queryset.filter(company_id=tmp.company_id, code=code['id']).first()
        return obj

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer(obj)

        serializer_data = serializer.data
        serializer_data['tags'] = serializer_data['tags'].split('|')
        return Response(serializer_data, status=status.HTTP_200_OK)