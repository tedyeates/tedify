from rest_framework import serializers
from music.models import Genre

class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = ['name', 'description']
