from django.contrib import admin

import hello_blog.models


@admin.register(hello_blog.models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(hello_blog.models.Note)
class NoteAdmin(admin.ModelAdmin):
    pass
