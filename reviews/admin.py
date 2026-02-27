from django.contrib import admin
from .models import Category, Product, User, Review, SentimentResult

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(User)
admin.site.register(Review)
admin.site.register(SentimentResult)
