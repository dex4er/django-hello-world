from django.contrib import admin

import hello_blog.models as models



class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Category, CategoryAdmin)



class NoteAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Note, NoteAdmin)


class UserNotesReportAdmin(admin.ModelAdmin):
    actions = None
    list_display = ['user_username', 'category_name', 'n']
    list_display_links = None
    readonly_fields = list_display

    def has_add_permission(self, request):
        return False

admin.site.register(models.UserNotesReport, UserNotesReportAdmin)
