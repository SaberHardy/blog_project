from rest_framework import serializers
from blogapp.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = '__all__'
        exclude = ('likes',)
