from django.db import models

# Create your models here.

class Introduction(models.Model):
    heading = models.CharField(max_length=100)
    body = models.TextField() 
    img = models.ImageField(upload_to='pics')
    learn = models.BooleanField(default=False)