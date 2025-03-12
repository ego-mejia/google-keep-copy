from django.db import models

# Create your models here.
class Tag(models.Model):
    """Tag what will be assigned to each Note."""

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
class Note(models.Model):
    """Note created by user."""

    title = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    tags= models.ManyToManyField(Tag, blank=True) #Allows notes without a Tag.

    def __str__(self):
        return self.title
