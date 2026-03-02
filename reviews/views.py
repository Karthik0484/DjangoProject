from django.shortcuts import render

from rest_framework import viewsets
from .models import Category, Product, User, Review, SentimentResult
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    UserSerializer,
    ReviewSerializer,
    SentimentResultSerializer
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class SentimentResultViewSet(viewsets.ModelViewSet):
    queryset = SentimentResult.objects.all()
    serializer_class = SentimentResultSerializer
