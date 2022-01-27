from django.shortcuts import render
from rest_framework import generics, status, mixins
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from blogapp.models import Post
from .serializers import PostSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view

"""This is new part using serializers views"""

# @csrf_exempt
# @api_view(['GET', 'POST'])
# def post_list(request, format=None):
#     if request.method == "GET":
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
#
#     elif request.method == "POST":
#         # data = JSONParser().parse(request)
#         serializer = PostSerializer(data=request.data)
#         # serializer = PostSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @csrf_exempt

# @api_view(['GET', 'PUT', 'DELETE'])
# def post_detail(request, pk, format=None):
#     try:
#         post = Post.objects.get(pk=pk)
#     except Post.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == "GET":
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#
#     elif request.method == "PUT":
#         # data = JSONParser().parse(request)
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == "DELETE":
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

"""Using class based views"""

# class PostListAPi(APIView):
#     """Get all posts serialized"""
#
#     def get(self, request, format=None):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(data=serializer.data)
#
#     def post(self, request, format=None):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class PostDetailApi(APIView):
#     def get_object(self, pk):
#         try:
#             return Post.objects.get(pk=pk)
#         except Post.DoesNotExist:
#             return Http404
#
#     def get(self, request, pk, format=None):
#         post = self.get_object(pk)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         post = self.get_object(pk)
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         post = self.get_object(pk)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

"""Using mixins"""

#
# class PostList(mixins.ListModelMixin,
#                mixins.CreateModelMixin,
#                generics.GenericAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class PostDetail(mixins.RetrieveModelMixin,
#                  mixins.UpdateModelMixin,
#                  mixins.DestroyModelMixin,
#                  generics.GenericAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

"""Using Generic class based views"""


class ApiBlogObjects(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class BlogObjectsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
