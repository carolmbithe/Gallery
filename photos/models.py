from django.db import models

# Create your models here.
class Image(models.Model):
    # image=models 
    image_name=models.CharField(max_length =30)
    image_description=models.CharField(max_length=30)
    # image location
    # image category
