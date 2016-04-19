from django.conf.urls import include, url
from django.contrib import admin

from hello_world import views

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
]
