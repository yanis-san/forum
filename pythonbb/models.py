from django.db import models

class Forum(models.Model):

    title = models.CharField(max_length=45)
    slug = models.SlugField(max_length=60)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)


class Thread(models.Model):
    title = models.CharField(max_length=45)
    slug = models.SlugField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)

class Message(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)