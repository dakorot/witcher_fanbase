from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    publication_date = models.DateField(null=False)

    def __str__(self):
        return f"{self.title} {self.content}"
