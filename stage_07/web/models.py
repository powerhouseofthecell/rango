from django.db import models

# Create your models here.
class Favorite(models.Model):
    body = models.TextField()
    likes = models.IntegerField(default=1)

    def __str__(self):
        return f'Favorite Quote #{self.id}'
