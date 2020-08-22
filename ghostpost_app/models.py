from django.db import models
from django.utils import timezone


# Create your models here.
class Ghostpost(models.Model):
    text = models.CharField(max_length=80)
    boasts = models.BooleanField()
    post_date = models.DateTimeField(default=timezone.now)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    
    def added(self):
        return self.upvotes + self.downvotes


    def __str__(self):
        return self.text

