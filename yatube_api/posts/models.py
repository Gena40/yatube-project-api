from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.fields.related import ForeignKey

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Group title',
        help_text='Enter group name'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='slug',
        help_text='short label'
    )
    description = models.TextField(
        verbose_name='description',
        help_text='Enter group description'
    )

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='posts',
        verbose_name='Группа',
        help_text='Группа, к которой будет относиться пост'
    )
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)


class Follow(models.Model):
    user = ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик'
    )
    following = ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор'
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'following'),
                name='unique_follow'
            ),
        )

    def __str__(self) -> str:
        return f'Пользователь {self.user} подписан на автора {self.following}'
