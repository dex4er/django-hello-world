from django.conf.urls import include, url

from hello_blog import views
from hello_blog.views import GetNoteView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/1/', include('hello_blog.api.urls')),
    url(r'^note/(?P<id>\d+)$', GetNoteView.as_view(), name='note'),
]
