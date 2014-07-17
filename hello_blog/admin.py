from django.contrib import admin

from hello_blog.models import Category, Note

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)

class NoteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Note, NoteAdmin)
