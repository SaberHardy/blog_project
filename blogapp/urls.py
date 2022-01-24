from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name="article-detail"),
    path('create/', AddPostView.as_view(), name="create"),
    path('article/update/<int:pk>/', UpdatePostView.as_view(), name="update-article"),
    path('delete/<int:pk>/remove', DeletePostView.as_view(), name="delete-post"),
    path('add_category/', AddCategoryView.as_view(), name="add-category"),
    path('category/<str:cats>/', category_view, name="category"),
    path('category_list_view/', category_list_view, name="category_list_view"),
    path('like/<int:pk>/', like_unlike_post, name="like_post"),
    path('add_comment/<int:pk>/comment/', AddCommentView.as_view(), name="add_comment"),

]
