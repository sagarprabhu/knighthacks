from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from nlpModel.models import nlpModel
from nlpModel.serializers import nlpModelSerialiser

class nlpModelViewSet(viewsets.ModelViewSet):

    queryset = nlpModel.objects.all()
    serializer_class = nlpModelSerialiser

    def get(self, request, *args, **kwargs):
        return "1"
