from django.urls import re_path, include, path

from .views import RegistrationAPIView
from .views import LoginAPIView
from .views import UpdatePassword

urlpatterns = [
    re_path(r'^registration/?$', RegistrationAPIView.as_view(), name='user_registration'),
    re_path(r'^login/?$', LoginAPIView.as_view(), name='user_login'),
    path('pass-change/', UpdatePassword.as_view(), name='user_change_pass'),
]