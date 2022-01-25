from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=256)
    post_content = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('blog_app:detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    date_published = models.DateTimeField(auto_now_add=True)
    comment_content = models.TextField()

    def __str__(self) -> str:
        return self.post.title

    def get_absolute_url(self):
        return reverse('blog_app:detail', kwargs={'pk': self.post.pk})
