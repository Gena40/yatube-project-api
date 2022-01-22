from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework import viewsets, permissions
from rest_framework.pagination import LimitOffsetPagination
from posts.models import Post, Group, Follow
from api.serializers import PostSerializer, CommentSerializer
from api.serializers import GroupSerializer, FollowSerializer
from api.permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly)

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        this_post = get_object_or_404(Post, id=post_id)
        serializer.save(
            author=self.request.user,
            post=this_post
        )

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        this_post = get_object_or_404(Post, id=post_id)
        return this_post.comments.all()


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        current_user = self.request.user
        queryset = Follow.objects.filter(user=current_user).all()
        return queryset

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )
