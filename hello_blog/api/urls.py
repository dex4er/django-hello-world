import hello_blog.api.views as views

from django.urls import include, path
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'category', views.CategoryViewSet)
router.register(r'note', views.NoteViewSet)


urlpatterns = [
    path('category/<name>/', views.CategoryNameView.as_view()),
    path('', include(router.urls)),
]
