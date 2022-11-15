from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()

    def get_email(self, obj):
        return obj.author.email
    
    def get_title(self, obj):
        return obj.post.title

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'body', 'email', 'title')
    