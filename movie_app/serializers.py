from django.db.models import Avg
from rest_framework import serializers

from movie_app.models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):
    directors = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = ['name', 'directors']

    def get_directors(self, obj):
        directors = obj.directors.count()
        return directors


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ReviewMovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['title', "description", "duration", 'director', 'reviews', 'average_rating']

    def get_average_rating(self, obj):
        average_rating = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        return average_rating
