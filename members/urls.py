from django.contrib.auth import views as auth_views
from django.urls import path
from .views import *

urlpatterns = [
    path('registrations/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),

    # in this path it not working very good so we need to create our own view"""
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html')),
    # """My new class view""",
    path('password/', PasswordChangeView.as_view(template_name='registration/change_password.html')),
    path('password_success/', password_success, name="password_success"),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name="profile"),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name="edit_profile_page"),

]
