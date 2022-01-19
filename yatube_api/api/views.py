from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from posts.models import Post, Group, User, Follow
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
    permission_classes = (
        permissions.IsAuthenticated,
        IsAuthorOrReadOnly)

    def list(self, request):
        current_user = self.request.user
        following = get_object_or_404(Follow, user=current_user)
        new_queryset = User.objects.filter(following=following).all()
        serializer = FollowSerializer(new_queryset, many=True)
        return Response(serializer.data)

    # def perform_create(self, serializer):
    #     serializer.save(
    #         user=self.request.user
    #     )
