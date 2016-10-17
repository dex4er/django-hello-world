from django.http import HttpResponse


def index(request):
    return HttpResponse("<html><head></head><body>Hello, world!</body></html>")
