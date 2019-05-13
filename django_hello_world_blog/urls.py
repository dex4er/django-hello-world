from django.urls import path

from . import views

urlpatterns = [
    path('note/<int:id>/', views.GetNoteView.as_view(), name='note'),
    path('', views.index, name='index'),
]
