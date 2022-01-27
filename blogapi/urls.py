from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.ApiBlogObjects.as_view()),
    path('<int:pk>/', views.BlogObjectsDetail.as_view()),

    # """Using function based view"""
    # path('', views.post_list, name='post_list'),
    # path('<int:pk>/', views.post_detail, name='post_api')

    # """This using class based view"""
    # path('', views.PostListAPi.as_view()),
    # path('<int:pk>/', views.PostDetailApi.as_view()),

    # This is used with mixins
    # path('', views.PostList.as_view()),
    # path('<int:pk>/', views.PostDetail.as_view()),
]

urlpatterns += format_suffix_patterns(urlpatterns)
