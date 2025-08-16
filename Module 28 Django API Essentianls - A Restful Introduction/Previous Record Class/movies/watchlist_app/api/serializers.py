from rest_framework import serializers
from  watchlist_app import models

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MovieList
        # fields = ['name', 'description', 'active']
        fields = '__all__'  # This will include all fields in the model