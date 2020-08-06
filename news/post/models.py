from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    creation_date = models.DateTimeField(auto_now_add=True)
    count_upvotes = models.IntegerField(default=0, editable=False)
    author_name = models.CharField(max_length=255)

    class Meta:
        ordering = ["creation_date", "title"]


class Comment(models.Model):
    author_name = models.CharField(max_length=255)
    content = models.CharField(max_length=1024)
    creation_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
