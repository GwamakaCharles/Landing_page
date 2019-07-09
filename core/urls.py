from django.urls import path
from .views import PostView
from . import views

urlpatterns = [
    path('', views.PostView, name='PostView'),
]