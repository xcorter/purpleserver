from django.db import models

class Mark(models.Model):
    message = models.TextField()
    coordinate = models.CharField(max_length=256)
