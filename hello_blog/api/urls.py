import hello_blog.api.views as views

from django.conf.urls import include, url
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'category', views.CategoryViewSet)
router.register(r'note', views.NoteViewSet)


urlpatterns = [
    url('^category/(?P<name>[a-z]+)/$', views.CategoryNameView.as_view()),
    url(r'^', include(router.urls)),
]
