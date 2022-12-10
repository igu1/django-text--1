from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class BlogModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    desc = RichTextField()
    created = models.DateTimeField(auto_created=True)


    def __str__(self):
        return self.title


class CommentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created = models.DateTimeField(auto_created=True, null=True, blank=True)

    def __str__(self):
        return self.user.username