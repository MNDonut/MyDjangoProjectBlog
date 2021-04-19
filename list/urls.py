from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('<str:slug>/', views.main, name='main'),
    path('post/<int:id>/', views.post_by_id, name='by_id'),
    path('post/<int:id>/edit/', views.edit_by_id, name="edit_id")
]