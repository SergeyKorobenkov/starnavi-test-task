from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('like-post/', views.LikesToPost.as_view(), name='likes'),
    path('new-post/', views.PostsWorker.as_view(), name='create post'),
    path('analitics/', views.Analytics.as_view(), name='analytics'),
    path('user-stats/', views.UserActivities.as_view(), name='user stats'),
]


