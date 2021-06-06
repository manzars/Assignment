from django.urls import path
from todo.api.views import CreateTodoView, DeleteTodoView, TodoList

urlpatterns = [
    path('todo/create/', CreateTodoView.as_view()),
    path('todo/all/', TodoList.as_view()),
    path('todo/delete/<pk>/', DeleteTodoView.as_view()),
    # path('employee/update/<pk>/', UpdateEmployeeView.as_view())
]