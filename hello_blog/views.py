from django.views.generic.base import View
from django.shortcuts import render

from hello_blog.models import Note

def index(request):
    notes = Note.objects.all()
    return render(request, "index.html", {'notes':notes})

class GetNoteView(View):
    def get(self, request, *args, **kwargs):
        note = Note.objects.get(id = kwargs['id'])
        return render(request, "note.html", {'note':note})
