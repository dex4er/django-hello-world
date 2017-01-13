from django.conf.urls import url

import hello_blog.views

urlpatterns = [
    url(r'^$', hello_blog.views.index, name='index'),
    url(r'^note/(?P<id>\d+)$', hello_blog.views.GetNoteView.as_view(), name='note'),
]
