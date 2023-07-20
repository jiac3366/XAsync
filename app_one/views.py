from app_one.serializer import PersonSerializer
from app_one.models import Person
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    pagination_class = LimitOffsetPagination
