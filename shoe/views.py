import io
import pandas as pd
import ast
from rest_framework import viewsets, views
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.parsers import MultiPartParser
from .serializers import ShoeSerializer
from django.conf import settings
from sqlalchemy import create_engine
from .models import Shoe
from django.contrib.postgres.fields import ArrayField
import django_filters

class ShoeViewSet(viewsets.ModelViewSet):

    __basic_fields = ('sku', 'name','details','price')

    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields

class CsvView(views.APIView):

    parser_classes = (MultiPartParser,)

    def post(self, request, format=None):

        if 'file' not in request.data:
            raise ParseError("Empty content")
        f = request.data['file']

        data = io.StringIO(str(f.read(),'utf-8') ) 
        df=pd.read_csv(data, sep=';')
        df = df.apply(self.__calculate_discount, axis=1)
        df = df.drop('promotion', axis=1)
        df = df.apply(self.__string_list_to_list, axis=1)

        user = settings.DATABASES['default']['USER']
        password = settings.DATABASES['default']['PASSWORD']
        host = settings.DATABASES['default']['HOST']
        database_name = settings.DATABASES['default']['NAME']

        database_url = 'postgresql://{user}:{password}@{host}:5432/{database_name}'.format(
            user=user,
            password=password,
            host=host,
            database_name=database_name,
        )

        engine = create_engine(database_url, echo=False)

        df.to_sql(Shoe._meta.db_table, con=engine, if_exists='append', index=False)

        return Response(status='201')

    def __calculate_discount(self, line):
        line['price'] = line['price'] - (line['price']*line['promotion']/100)
        return line
    
    def __string_list_to_list(self, line):
        line['tags'] = ast.literal_eval(line['tags'])
        return line
