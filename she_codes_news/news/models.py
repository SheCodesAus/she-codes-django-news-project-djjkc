from django.contrib.auth import get_user_model
from email.mime import image
from django.db import models


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    image_url = models.CharField(max_length=300, default= "https://picsum.photos/200/300")

    def snippet(self):
        return self.content[:50] + '...'

class Author(models.Model):
    user = models.OneToOneField(get_user_model(),on_delete=models.CASCADE)
    author = user.name

    def get_absolute_url(self):
        return reverse("author", kwargs={'pk':self.pk})

    def __str__(self):
        return self.author.username
        