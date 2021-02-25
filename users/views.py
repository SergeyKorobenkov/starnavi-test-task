from django.shortcuts import get_object_or_404
from django.contrib.auth import password_validation

from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import LoginSerializer
from .serializers import RegistrationSerializer
from .serializers import UserPasswordChangeSerializer


class RegistrationAPIView(APIView):
    '''
    Registers a new user.
    '''
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

    def post(self, request):
        '''
        Creates a new User object.
        Username, email, and password are required.
        Returns a JSON web token.
        '''
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                'token': serializer.data.get('token', None),
            },
            status=status.HTTP_201_CREATED,
        )


class LoginAPIView(APIView):
    '''
    Logs in an existing user.
    '''
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        '''
        Checks is user exists.
        Email and password are required.
        Returns a JSON web token.
        '''
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdatePassword(APIView):
    '''
    An endpoint for changing password.
    '''
    permission_classes = (IsAuthenticated, )

    def put(self, request):
        if not request.user.check_password(request.data['old_password']):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if request.data['old_password'] == request.data['new_password'] == request.data['confirmed_password']:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if request.data['new_password'] != request.data['confirmed_password']:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        validators = password_validation.get_default_password_validators()

        try:
            for i in validators:
                i.validate(request.data['new_password'])

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        
        request.user.set_password(request.data['new_password'])
        request.user.save()

        return Response(status=status.HTTP_202_ACCEPTED)
