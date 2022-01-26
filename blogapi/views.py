from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

"""New Imports"""
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from blogapp.models import Post
from .serializers import PostSerializer

# from blogapp.models import Post
# from .serializers import PostSerializer
#
#
# class ApiBlogObjects(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class BlogObjectsDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

"""This is new part using serializers views"""


@csrf_exempt
def post_list(request):
    if request.method == "GET":
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def post_detail(request, pk):
    try:
        print(f"id ====>{pk}")
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = PostSerializer(post)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = PostSerializer(post, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        post.delete()
        return HttpResponse(status=204)

