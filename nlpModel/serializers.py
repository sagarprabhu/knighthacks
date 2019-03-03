from rest_framework import serializers
from .models import nlpModel

class nlpModelSerialiser(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = nlpModel
        fields = ('question',)

