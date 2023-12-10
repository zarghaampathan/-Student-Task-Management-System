# tasks/urls.py
from django.urls import path
from . import views
from .views import task_list


urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task/new/', views.task_new, name='task_new'),
    path('task/<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('', task_list, name='task_list'),
]
