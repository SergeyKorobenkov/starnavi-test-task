import datetime

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny

from users.models import User
from .decorators import user_activity_log





class Index(generics.GenericAPIView):

    permission_classes = [IsAuthenticated]

    def wrapper(self, request):
        if request.user.is_authenticated:
            request.user.last_activity = datetime.datetime.now()
            request.user.save()
            return 
        else:
            return 

    
    def get(self, request):
        print(request.user)
        print(request.user.last_login)
        self.wrapper(request)
        print(request.user.last_activity)
        return JsonResponse({'1':'2'}, status=200)
