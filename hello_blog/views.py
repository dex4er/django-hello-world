from django import views
from django.shortcuts import render

import hello_blog.models


def index(request):
    notes = hello_blog.models.Note.objects.all()
    return render(request, 'index.html', {'notes': notes})


class GetNoteView(views.generic.base.View):
    def get(self, request, *args, **kwargs):
        note = hello_blog.models.Note.objects.get(id=kwargs['id'])
        return render(request, 'note.html', {'note': note})
