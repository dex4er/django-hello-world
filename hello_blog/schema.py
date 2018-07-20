from django.contrib import auth
from graphene_django import DjangoObjectType

import graphene

import hello_blog.models


class UserType(DjangoObjectType):
    class Meta:
        model = auth.models.User


class CategoryType(DjangoObjectType):
    class Meta:
        model = hello_blog.models.Category


class NoteType(DjangoObjectType):
    class Meta:
        model = hello_blog.models.Note


class Query(graphene.ObjectType):
    user = graphene.Field(
        UserType,
        id=graphene.Int(),
        username=graphene.String(),
    )
    user_set = graphene.List(UserType)

    category = graphene.Field(
        CategoryType,
        id=graphene.Int(),
        name=graphene.String(),
    )
    category_set = graphene.List(CategoryType)

    note = graphene.Field(
        NoteType,
        id=graphene.Int(),
        title=graphene.String(),
    )
    note_set = graphene.List(NoteType)

    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')
        username = kwargs.get('username')

        if id is not None:
            return auth.models.User.objects.get(pk=id)

        if username is not None:
            return auth.models.User.objects.get(username=username)

        return None

    def resolve_user_set(self, info):
        return auth.models.User.objects.all()

    def resolve_category(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return hello_blog.models.Category.objects.get(pk=id)

        if name is not None:
            return hello_blog.models.Category.objects.get(name=name)

        return None

    def resolve_category_set(self, info):
        return hello_blog.models.Category.objects.all()

    def resolve_note(self, info, **kwargs):
        id = kwargs.get('id')
        title = kwargs.get('title')

        if id is not None:
            return hello_blog.models.Note.objects.get(pk=id)

        if title is not None:
            return hello_blog.models.Note.objects.get(title=title)

        return None

    def resolve_note_set(self, info):
        return hello_blog.models.Note.objects.all()


schema = graphene.Schema(query=Query)
