from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from movie_app.models import Director, Movie, Review
from movie_app.serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, ReviewMovieSerializer


@api_view(['GET'])
def director_view(request):
    director = Director.objects.all()
    serializer = DirectorSerializer(director, many=True).data
    return Response(data=serializer, status=status.HTTP_200_OK)


@api_view(['GET'])
def director_detail_view(request, id):
    director = Director.objects.get(id=id)
    serializer = DirectorSerializer(director).data
    return Response(data=serializer, status=status.HTTP_200_OK)


@api_view(['GET'])
def movie_view(request):
    movie = Movie.objects.all()
    serializer = MovieSerializer(movie, many=True).data
    return Response(data=serializer, status=status.HTTP_200_OK)


@api_view(['GET'])
def movie_detail_view(request, id):
    movie = Movie.objects.get(id=id)
    serializer = MovieSerializer(movie).data
    return Response(data=serializer, status=status.HTTP_200_OK)


@api_view(['GET'])
def review_view(request):
    review = Review.objects.all()
    serializer = ReviewSerializer(review, many=True).data
    return Response(data=serializer, status=status.HTTP_200_OK)


@api_view(['GET'])
def review_detail_view(request, id):
    review = Review.objects.get(id=id)
    serializer = ReviewSerializer(review).data
    return Response(data=serializer, status=status.HTTP_200_OK)


@api_view(['GET'])
def review_movie_view(request):
    review = Movie.objects.all()
    serializer = ReviewMovieSerializer(review, many=True).data
    return Response(data=serializer, status=status.HTTP_200_OK)
