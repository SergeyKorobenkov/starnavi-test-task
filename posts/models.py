import datetime

from django.db import models

from users.models import User


class Likes(models.Model):
    who_like_it = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='liker',
        )
    liked_post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='liked_post_id')
    like_time = models.DateTimeField(default=datetime.datetime.now(), verbose_name="when it liked")

    def __str__(self):
        return self.who_like_it.username

    class Meta:
        ordering = ['-like_time']
        unique_together = ('who_like_it', 'liked_post')


class Post(models.Model):
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='post_author',
        )
    text = models.TextField(
        null=False, 
        blank=True, 
        )
    pub_date = models.DateTimeField("date published", auto_now_add=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['-pub_date']
