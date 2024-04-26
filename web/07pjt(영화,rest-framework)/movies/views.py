from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Actor,Movie,Review
from .serializers import ActorListSerializer, MovieListSerializer, ActorSerializer, ReviewListSerializer, MovieSerializer,ReviewSerializer
from rest_framework import serializers, status



# Create your views here.
@api_view(['GET'])
def actor_list(request):
    actors = Actor.objects.all()
    serializer = ActorListSerializer(actors, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def actor_detail(request, pk):
    actor = Actor.objects.get(pk=pk)
    serializer = ActorSerializer(actor)
    return Response(serializer.data)




@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def review_detail(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method =='GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    elif request.method =='PUT':
        serializer = ReviewSerializer(instance=review, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    elif request.method =='DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['POST'])
def create_review(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializer = ReviewSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data)