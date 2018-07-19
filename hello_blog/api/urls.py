import hello_blog.api.views as views

from django.urls import include, path, re_path
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view


router = routers.DefaultRouter()
router.register(r'category', views.CategoryViewSet)
router.register(r'note', views.NoteViewSet)

schema_view = get_swagger_view(title='Hello Blog API')


urlpatterns = [
    re_path('^$', schema_view),
    path('category/<str:name>/', views.CategoryNameView.as_view()),
    path('', include(router.urls)),
]
