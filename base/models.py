from django.db import models
from ckeditor.fields import RichTextField

class BlogModel(models.Model):
    title = models.CharField(max_length=255)
    desc = RichTextField()


    def __str__(self):
        return self.title