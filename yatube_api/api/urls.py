from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, PostViewSet


router = routers.DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(
    r"posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comment"
)

urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
]
