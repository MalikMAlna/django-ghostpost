from django.db import models


class Post(models.Model):
    b_or_r = models.BooleanField()
    content = models.CharField(max_length=280)
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)
    created = models.DateTimeField()
