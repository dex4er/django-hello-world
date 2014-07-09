from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Note(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    content = models.TextField(max_length=50000)
