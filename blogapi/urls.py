from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.ApiBlogObjects.as_view()),
    path('api/<int:pk>/', views.BlogObjectsDetail.as_view()),
]

urlpatterns += format_suffix_patterns(urlpatterns)
