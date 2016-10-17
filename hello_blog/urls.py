from django.conf.urls import url

from hello_blog import views
from hello_blog.views import GetNoteView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^note/(?P<id>\d+)$', GetNoteView.as_view(), name='note'),
]
