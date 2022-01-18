from django.urls import path, include
from .views import *

urlpatterns = [
    path('registrations/', UserRegisterView.as_view(), name='register'),
]
