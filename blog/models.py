from django.conf import settings
from django.db import models
from django.utils import timezone


# post && publisher model
class Post(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField()

    def publish(self):
        self.published_date = timezone.now()

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)


class Publish(models.Model):
    author = models.ForeignKey(Author, related_name='reservation', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='reservation', on_delete=models.CASCADE)
