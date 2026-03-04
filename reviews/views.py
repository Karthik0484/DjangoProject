from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
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
    permission_classes = [IsAuthenticated] 


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]


class SentimentResultViewSet(viewsets.ModelViewSet):
    queryset = SentimentResult.objects.all()
    serializer_class = SentimentResultSerializer
    permission_classes = [IsAuthenticated]
