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
    image_url = models.CharField(max_length=300, default= "https://pixabay.com/images/id-1489825/")
