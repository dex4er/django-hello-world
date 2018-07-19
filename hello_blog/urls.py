<<<<<<< HEAD
from django.conf.urls import include, url
=======
from django.urls import path
>>>>>>> blog

import hello_blog.views

urlpatterns = [
<<<<<<< HEAD
    url(r'^$', views.index, name='index'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/1/', include('hello_blog.api.urls')),
    url(r'^note/(?P<id>\d+)$', GetNoteView.as_view(), name='note'),
=======
    path('note/<int:id>/', hello_blog.views.GetNoteView.as_view(), name='note'),
    path('', hello_blog.views.index, name='index'),
>>>>>>> blog
]
