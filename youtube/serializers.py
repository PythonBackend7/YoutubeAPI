from rest_framework import serializers
from accounts.serializers import CustomUserSerializer
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    hashtags = HashtagSerializer(many=True, read_only=True)
    authors = CustomUserSerializer(read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Video
        fields = '__all__'
