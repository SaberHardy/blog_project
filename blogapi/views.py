from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from blogapp.models import Post
from .serializers import PostSerializer


class ApiBlogObjects(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class BlogObjectsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
