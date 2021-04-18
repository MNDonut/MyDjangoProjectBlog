from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True, editable=True, blank=False)

    def __str__(self):
        return f"Title: {self.title}\n, Description: {self.description}\n, Date: {self.date}\n"

    @staticmethod
    def create(title, description, date=None):
        newPost = Post(title=title, description=description, date=date)
        newPost.save()