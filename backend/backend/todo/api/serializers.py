from rest_framework import serializers
from django.contrib.auth.models import User
from todo.models import Todo

class TodoCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ('pk', 'user', 'title', 'date', 'desc',)

    def create(self, validated_data):
        todo = Todo(**validated_data)
        todo.save()
        return todo