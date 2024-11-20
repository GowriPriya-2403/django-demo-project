from django.db import models

class Movie(models.Model):     #db model definition
    title=models.CharField(max_length=20)
    description=models.TextField()
    language=models.CharField(max_length=20)
    year=models.IntegerField()
    poster=models.ImageField(upload_to="images")
