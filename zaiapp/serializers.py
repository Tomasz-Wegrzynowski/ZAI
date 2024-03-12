from rest_framework import serializers
from .models import Film

class FilmModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id', 'tytul', 'rok', 'opis', 'premiera', 'imdb_points']

    def create(self, validated_data):
        return Film.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.tytul = validated_data.get('tytul', instance.tytul)
        instance.rok = validated_data.get('rok', instance.rok)
        instance.opis = validated_data.get('opis', instance.opis)
        instance.premiera = validated_data.get('premiera', instance.premiera)
        instance.imdb_points = validated_data.get('imdb_points', instance.imdb_points)
        instance.save()
        return instance