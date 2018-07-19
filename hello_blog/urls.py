from django.urls import include, path

import hello_blog.views

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/1/', include('hello_blog.api.urls')),
    path('note/<int:id>/', hello_blog.views.GetNoteView.as_view(), name='note'),
    path('', hello_blog.views.index, name='index'),
]
