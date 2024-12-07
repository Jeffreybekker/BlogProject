from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.index, name='index'),
    path('posts/<str:pk>', views.post, name="post"),
]