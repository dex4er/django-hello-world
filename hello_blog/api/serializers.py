import hello_blog.models as models
import django.contrib.auth.models as auth_models

from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['name']

class NoteSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', queryset=auth_models.User.objects.all())
    category = serializers.SlugRelatedField(slug_field='name', queryset=models.Category.objects.all())

    class Meta:
        model = models.Note
        fields = ['user', 'category', 'keywords', 'title', 'date', 'content']
