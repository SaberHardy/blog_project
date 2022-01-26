from rest_framework import serializers
from blogapp.models import Post
import datetime


# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         # fields = '__all__'
#         exclude = ('likes',)
class PostSerializer(serializers.Serializer):
    # id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=True, max_length=255)
    title_tag = serializers.CharField(required=True, allow_blank=True, )
    author = serializers.ReadOnlyField(read_only=True)
    body = serializers.CharField()
    post_date = serializers.DateField(initial=datetime.date.today)
    category = serializers.CharField(max_length=255, default="Uncategorized")
    snippet = serializers.CharField(max_length=255)
    likes = serializers.StringRelatedField(many=True)
    header_image = serializers.ImageField()

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validate_data):
        instance.title = validate_data.get('title', instance.title)
        instance.title_tag = validate_data.get('title_tag', instance.title_tag)
        instance.author = validate_data.get('author', instance.author)
        instance.body = validate_data.get('body', instance.body)
        instance.post_date = validate_data.get('post_date', instance.post_date)
        instance.category = validate_data.get('category', instance.category)
        instance.snippet = validate_data.get('snippet', instance.snippet)
        instance.likes = validate_data.get('likes', instance.likes)
        instance.header_image = validate_data.get('header_image', instance.header_image)
        instance.save()
        return instance
