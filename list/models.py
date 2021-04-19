from django.db import models
import datetime

class Post(models.Model):
    """Implementation of Post model"""
    # verbose name - title on the left side of input
    title = models.CharField(max_length=100, verbose_name='')
    description = models.TextField(verbose_name='')
    date = models.DateTimeField(auto_now_add=True, verbose_name='')

    def __str__(self):
        return f"Title: {self.title}\n, Description: {self.description}\n, Date: {self.date}\n"

    @staticmethod
    def create(title, description, date=None):
        newPost = Post(title=title, description=description, date=date)
        newPost.save()

    @staticmethod
    def get_by_id(id):
        obj = Post.objects.get(pk=id)
        return obj