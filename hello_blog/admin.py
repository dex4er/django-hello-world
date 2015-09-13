from django.contrib import admin

import hello_blog.models as models

from django.db.models import Count


class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Category, CategoryAdmin)


class NoteAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Note, NoteAdmin)


class UserNotesReportAdmin(admin.ModelAdmin):
    actions = None
    list_display = ['user__username', 'category__name', 'n']
    list_display_links = None
    readonly_fields = ['user', 'category', 'n']

    def user__username(self):
        pass

    def category__name(self):
        pass

    def get_queryset(self, request):
        qs = models.Note.objects.order_by('user', 'category').values('user__username', 'category__name').annotate(n=Count('*'))
        print(qs.query)
        return qs

    def has_add_permission(self, request):
        return False

admin.site.register(models.UserNotesReport, UserNotesReportAdmin)
