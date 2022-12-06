from django.core.validators import FileExtensionValidator
from django.db import models
import random


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to='image/')
    file = models.FileField(
        upload_to='video/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])]
    )
    create_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=random.randint(10000, 1000000))
    likes_percentage = models.IntegerField(default=random.randint(70, 100))
    dislikes_percentage = models.IntegerField(default=random.randint(0, 20))

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
        ordering = ['-create_at']

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField(max_length=300)
    created_on = models.DateTimeField(auto_now_add=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['-created_on']

    def __str__(self):
        return self.text


