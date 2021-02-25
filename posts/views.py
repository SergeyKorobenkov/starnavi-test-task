import datetime

from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny


from users.models import User
from .models import Post, Likes


class LikesToPost(generics.GenericAPIView):
    '''
    Class to like/unlike posts
    If there is no likes to post from user, create like.
    Else remove like from DB.
    '''
    permission_classes = [IsAuthenticated]

    def user_logger(self, request):
        if request.user.is_authenticated:
            request.user.last_activity = datetime.datetime.now()
            request.user.save()
            return 
        else:
            return 

    def post(self, request):
        self.user_logger(request)
        post_item = get_object_or_404(Post, id=request.data['post_id'])

        try:
            like, created = Likes.objects.get_or_create(
                who_like_it=request.user, 
                liked_post=post_item)
            
            if created:
                return JsonResponse(
                    {'status':'created'}, 
                    status=status.HTTP_201_CREATED)
            
            else:
                like.delete()
                return JsonResponse(
                    {'status':'like was deleted from post'}, 
                    status=status.HTTP_202_ACCEPTED)
            
        except:
            return JsonResponse(
                {'status': 'any problems with like features'}, 
                status=status.HTTP_400_BAD_REQUEST)


class PostsWorker(generics.GenericAPIView):
    '''
    Class for work with post.
    In this version can only create new posts, 
    but in feature it can be upgraded with another features
    like edit, delete or recieving posts.
    '''
    permission_classes = [IsAuthenticated]

    def user_logger(self, request):
        if request.user.is_authenticated:
            request.user.last_activity = datetime.datetime.now()
            request.user.save()
            return 
        else:
            return 
    
    def post(self, request):
        self.user_logger(request)

        try:
            new_post, created = Post.objects.get_or_create(
                author=request.user,
                text=request.data['text']
                )
            
            if created:
                return JsonResponse(
                    {'status':'created'}, 
                    status=status.HTTP_201_CREATED)

            else:
                return JsonResponse(
                    {'status':'already exists'}, 
                    status=status.HTTP_302_FOUND)

        except:
            return JsonResponse(
                {'status': 'any problems with post features'}, 
                status=status.HTTP_400_BAD_REQUEST)


class Analytics(generics.GenericAPIView):
    '''
    There is function that can count number of likes 
    which was made in time period.
    '''
    def get(self, request):
        try:
            dates = dict(request.query_params)

            like_count = Likes.objects.filter(
                like_time__range=[
                    dates['date_from'][0], 
                    dates['date_to'][0]]
                    ).count()

            return JsonResponse(
                {'status':'recieved', 
                'like_by_period':f'{like_count}'}, 
                status=status.HTTP_200_OK)
        
        except:
            return JsonResponse(
                {'status': 'any problems with Analytics features'}, 
                status=status.HTTP_400_BAD_REQUEST)


class UserActivities(generics.GenericAPIView):
    '''
    There is method which can say user activities like
    last login time and last request time.
    '''
    def get(self, request):
        try:
            username = request.query_params['username']
            user = get_object_or_404(User, username=username)

            return JsonResponse(
                {'status':'user found',
                'last login':f'{user.last_login}',
                'last activity':f'{user.last_activity}'},
                status=status.HTTP_200_OK
                )
        
        except:
            return JsonResponse(
                {'status': 'any problems with UserActivities features'}, 
                status=status.HTTP_400_BAD_REQUEST)
