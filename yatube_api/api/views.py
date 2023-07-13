import datetime as dt

from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from posts.models import Post

from .permissions import IsAuthor
from .serializers import CommentSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthor,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, pub_date=dt.datetime.now)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthor,)

    def get_queryset(self):
        post_pk = self.kwargs.get("post_id")
        post = get_object_or_404(Post, pk=post_pk)
        return post.comments.all()

    def perform_create(self, serializer):
        post_pk = self.kwargs.get("post_id")
        serializer.save(
            author=self.request.user,
            post=get_object_or_404(Post, pk=post_pk),
            created=dt.datetime.now,
        )
