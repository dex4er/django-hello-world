from django.db import models
from django.db.models import Count, F
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return self.name


class Note(models.Model):
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    keywords = models.CharField(max_length=400)
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    content = models.TextField(max_length=50000)

    def __unicode__(self):
        return self.title


class UserNotesReportManager(models.Manager):
    def get_queryset(self):
        return Note.objects \
            .annotate(user_username=F('user__username'), category_name=F('category__name')) \
            .values('user_username', 'category_name') \
            .order_by('user_username', 'category_name') \
            .annotate(n=Count('*'))


class UserNotesReport(models.Model):
    user_username = models.CharField(max_length=30, primary_key=True)
    category_name = models.CharField(max_length=100, primary_key=True)
    n = models.IntegerField()

    objects = UserNotesReportManager()
