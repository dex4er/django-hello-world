from django.urls import include, path

import hello_blog.views


urlpatterns = [
    path('graphql/', include('hello_blog.graphql.urls')),
    path('note/<int:id>/', hello_blog.views.GetNoteView.as_view(), name='note'),
    path('', hello_blog.views.index, name='index'),
]
