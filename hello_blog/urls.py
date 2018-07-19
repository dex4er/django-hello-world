from django.urls import path

import hello_blog.views

urlpatterns = [
    path('note/<int:id>/', hello_blog.views.GetNoteView.as_view(), name='note'),
    path('', hello_blog.views.index, name='index'),
]
