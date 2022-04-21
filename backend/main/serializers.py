from dataclasses import fields
from statistics import mode
from rest_framework import serializers

from .models import Word


class WordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word
        fields = ['id', 'word', 'part_of_speech', 'description', 'inSentence']