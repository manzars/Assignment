from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from todo.models import Todo
from todo.api.serializers import TodoCreateSerializer
from rest_framework.response import Response

class CreateTodoView(generics.CreateAPIView):
    model = Todo
    permission_classes = [IsAuthenticated]
    serializer_class = TodoCreateSerializer

class DeleteTodoView(generics.DestroyAPIView):
    model = Todo
    queryset = Todo.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = TodoCreateSerializer

class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoCreateSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        print(request.user)
        queryset = self.get_queryset()
        queryset = queryset.filter(user = request.user)
        serializer = TodoCreateSerializer(queryset, many=True)
        return Response(serializer.data)