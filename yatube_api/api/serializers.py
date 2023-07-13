from rest_framework import serializers


from posts.models import Comment, Follow, Group, Post


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("id", "title", "slug", "description")


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    following = serializers.SlugRelatedField(
        slug_field="username", read_only=True
    )

    class Meta:
        model = Follow
        fields = ("id", "user", "following")
        read_only_fields = ("user", "following")


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field="username", read_only=True
    )

    class Meta:
        model = Post
        fields = ("id", "author", "text", "pub_date", "image", "group")
        read_only_fields = ("pub_date",)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field="username", read_only=True
    )

    class Meta:
        model = Comment
        fields = ("id", "author", "text", "created", "post")
        read_only_fields = ("created", "post")
