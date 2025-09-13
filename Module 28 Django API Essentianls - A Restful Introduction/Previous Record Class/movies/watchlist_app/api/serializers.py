from rest_framework import serializers
from  watchlist_app import models


# Serializer for MovieList model
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MovieList
        # fields = ['name', 'description', 'active']
        fields = '__all__'  # This will include all fields in the model



# New serializer for Reviews model
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reviews
        fields = '__all__'