from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from movie_app.models import Director, Movie, Review
from movie_app.serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, ReviewMovieSerializer


@api_view(['GET', 'POST'])
def director_view(request):
    if request.method == 'GET':
        director = Director.objects.all()
        serializer = DirectorSerializer(director, many=True).data
        return Response(data=serializer, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = DirectorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response({'errors': 'not found!!'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DirectorSerializer(director).data
        return Response(data=serializer, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = DirectorSerializer(director, data=request).data
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def movie_view(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True).data
        return Response(data=serializer, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response({'errors': 'not found!!'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MovieSerializer(movie).data
        return Response(data=serializer, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request).data
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def review_view(request):
    if request.method == 'GET':
        review = Review.objects.all()
        serializer = ReviewSerializer(review, many=True).data
        return Response(data=serializer, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response({'errors': 'not found!!'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ReviewSerializer(review).data
        return Response(data=serializer, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request).data
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def review_movie_view(request):
    review = Movie.objects.all()
    serializer = ReviewMovieSerializer(review, many=True).data
    return Response(data=serializer, status=status.HTTP_200_OK)
