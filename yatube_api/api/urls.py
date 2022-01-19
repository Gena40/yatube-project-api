from rest_framework.routers import SimpleRouter
from django.urls import path, include
from api.views import PostViewSet, CommentViewSet
from api.views import GroupViewSet, FollowViewSet


app_name = 'api'

router = SimpleRouter()
router.register(r'v1/posts', PostViewSet)
router.register(r'v1/groups', GroupViewSet)
router.register(
    r'v1/follow',
    FollowViewSet,
    basename='follow'
)
router.register(
    r'v1/posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)

urlpatterns = [
    path('', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
