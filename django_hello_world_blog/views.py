from django import views
from django.shortcuts import render

from . import models


def index(request):
    notes = models.Note.objects.all()
    return render(request, 'index.html', {'notes': notes})


class GetNoteView(views.generic.base.View):
    def get(self, request, *args, **kwargs):
        note = models.Note.objects.get(id=kwargs['id'])
        return render(request, 'note.html', {'note': note})
