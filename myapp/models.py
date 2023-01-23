from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    img = models.ImageField(upload_to="photos")

    def __str__(self):
        return self.title
