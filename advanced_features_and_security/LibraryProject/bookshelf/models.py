from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"


class Document(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        permissions = [
            ('can_view', 'Can view document'),
            ('can_create', 'Can create document'),
            ('can_edit', 'Can edit document'),
            ('can_delete', 'Can delete document'),
        ]

    def __str__(self):
        return self.title
