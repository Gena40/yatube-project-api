from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from posts.models import Comment, Post, Group, Follow, User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post', 'created')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    following = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'following')


class FollowSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(read_only=True)
    # following = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='following'
    # )
    following = UserSerializer(many=True, read_only=True)

    class Meta:
        fields = ('user', 'following')
        model = Follow
        read_only_fields = ('user',)

    # def create(self, validated_data):
    #     print('************* create')
    #     author_name = self.initial_data.get('following')
    #     author = get_object_or_404(User, username=author_name)
    #     flw = Follow.objects.create(
    #         user=validated_data.get('user'),
    #         following=author
    #     )
    #     return flw
