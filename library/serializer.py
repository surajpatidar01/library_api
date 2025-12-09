from rest_framework import serializers
from .models import Book,Task
from django.contrib.auth.models import User


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(queryset=Book.objects.all(),slug_field='title')
    user = serializers.SlugRelatedField(queryset=User.objects.all(),slug_field='username')

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['user']
