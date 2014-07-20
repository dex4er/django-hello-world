from django.conf.urls import patterns, url

from hello_blog import views
from hello_blog.views import GetNoteView

from haystack.forms import SearchForm
from haystack.views import SearchView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^note/(?P<id>\d+)$', GetNoteView.as_view(), name='note'),
]

urlpatterns += patterns('haystack.views',
    url(r'^search/', SearchView(
        form_class=SearchForm,
    ), name='haystack_search'),
)
