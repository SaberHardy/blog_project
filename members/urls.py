from django.urls import path, include
from .views import *

urlpatterns = [
    path('registrations/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
]
