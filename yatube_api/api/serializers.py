from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from posts.models import Comment, Post


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Post
        fields = ("id", "author", "text", "pub_date", "image", "group")
        read_only_fields = ("id", "author", "pub_date")


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field="username"
    )

    class Meta:
        model = Comment
        fields = ("id", "author", "text", "created", "post")
        read_only_fields = ("id", "author", "created", "post")
