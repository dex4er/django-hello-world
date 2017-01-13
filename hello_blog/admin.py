from django.contrib import admin

import hello_blog.models


class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(hello_blog.models.Category, CategoryAdmin)


class NoteAdmin(admin.ModelAdmin):
    pass

admin.site.register(hello_blog.models.Note, NoteAdmin)
