from django.db import models

import django_hello_world.models


class Category(django_hello_world.models.Model):
    id = models.AutoField(db_column='category_id', primary_key=True)
    name = models.CharField(max_length=100, help_text='Category name')

    class Meta:
        db_table = 'category'
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Note(django_hello_world.models.Model):
    id = models.AutoField(db_column='note_id', primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='notes', related_query_name='node')
    keywords = models.CharField(max_length=400)
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    content = models.TextField(max_length=50000)

    class Meta:
        db_table = 'note'

    def __str__(self):
        return self.title
